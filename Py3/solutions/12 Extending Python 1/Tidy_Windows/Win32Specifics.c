/*
   Win32Specifics.c


   Copyright (c) 2004,2011 Clive Darke

       You may distribute under the terms of the GNU General Public License

   From egres 1.6
   Based on yash Version 2.09
   readdir fixed for multiple directories February 2011

*/
#define _CRT_SECURE_NO_WARNINGS
#include <windows.h>
#include <conio.h>
#include <winsock.h>
#include <io.h>
#include <fcntl.h>
#include <sys/types.h>
#include "Win32Specifics.h"

/* Local Definitions */

/* Local types */
typedef struct handles
{
   HANDLE hStdIn;
   HANDLE hStdOut;
   HANDLE hStdErr;
}  StdHandles;


/* Local Off-stack */
static DWORD g_dwConsoleMode = 0xff;   // Used in OS_ReadFromConsole
static BOOL g_IsNT;

static char g_szTempDir [MAX_PATH] = {0};

/* Local Prototypes */
static void HandleError (DWORD dwErrorNo, const char *pszMsg);
static int opt_handling (int argc, char * const argv[], const char *optstring);

static BOOL bPrintFileDetails (const DWORD dwAttr, HANDLE hOut,
                               char *szFilename, HANDLE hErr);

/* getopt globals */
int opterr = 0;
int optind = 1;  /* 1 because that is the first arg to parse (CBD) */
int optopt = 0;
char *optarg = NULL;

static size_t optpos = 0;   /* CBD */

/* Inode handling globals */
typedef struct
{
	HANDLE hFile;
    BY_HANDLE_FILE_INFORMATION Info;
} Inode;

Inode g_Inode = {0};

/* ----------------------------------------------------------------- */

void  OS_Setup (void)
{
   OSVERSIONINFO OsVer;
   DWORD dwMachineSize = MAX_COMPUTERNAME_LENGTH + 1;

   GetConsoleMode (GetStdHandle(STD_INPUT_HANDLE), &g_dwConsoleMode);

   GetTempPath(MAX_PATH, g_szTempDir);

   /* Are we Win NT? */

   OsVer.dwOSVersionInfoSize = sizeof(OSVERSIONINFO);
   GetVersionEx (&OsVer);

   if ( OsVer.dwPlatformId == VER_PLATFORM_WIN32_NT )
      g_IsNT = TRUE;
   else
      g_IsNT = FALSE;

}  /* OS_Setup */

/* -----------------------------------------------------------------
   DIR is typedef'ed to HANDLE
   struct dirent has WIN32_FIND_DATA fData and dname
   ----------------------------------------------------------------- */

DIR *opendir(const char *name)
{
   char pName[MAX_PATH+1];

   DIR *pdir = malloc(sizeof(DIR));
   if ( !pdir )
      return NULL;

   pdir->pdirent = malloc (sizeof(struct dirent));
   if ( !pdir->pdirent )
      return NULL;

   sprintf (pName, "%s\\*", name);
   pdir->hFile = FindFirstFile (pName, &pdir->pdirent->fData);
   pdir->pdirent->d_name = pdir->pdirent->fData.cFileName;

   pdir->bFindFirst = TRUE;

   return pdir;

}  /* opendir */

struct dirent *readdir(DIR *hDir)
{
   if (!hDir)
      return NULL;

   if ( hDir->bFindFirst ) {
      hDir->bFindFirst = FALSE;
   }
   else
   {
      if ( !FindNextFile (hDir->hFile, &hDir->pdirent->fData) )
         return NULL;

      hDir->pdirent->d_name = hDir->pdirent->fData.cFileName;
   }

   return hDir->pdirent;

}  /* readdir */

int closedir (DIR *hDir)
{

   FindClose (hDir->hFile);

   if ( hDir )
   {
      free (hDir->pdirent);
	  free (hDir);
   }

   return 0;

}  /* closedir */

/* ----------------------------------------------------------------
   Required because Windows 'open' does not allow a directory
   to be opened.

   _open_osfhandle()

   ---------------------------------------------------------------- */

HANDLE Win32open (const char *pszFilename, int mode)
{
   HANDLE hFile;
   DWORD dwAccess = 0;
   DWORD dwFlags  = 0;
   DWORD dwFileAttributes = 0;

   if ( mode == O_RDONLY )
      dwAccess = GENERIC_READ;

   /* Is this a directory? */

   dwFileAttributes = GetFileAttributes (pszFilename);

   if ( dwFileAttributes == -1 )
      return INVALID_HANDLE_VALUE;

   else if (dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY)
      dwFlags |= FILE_FLAG_BACKUP_SEMANTICS;

   hFile = CreateFile (pszFilename, dwAccess, FILE_SHARE_READ,
                       NULL, OPEN_EXISTING, dwFlags, NULL);

   if ( hFile == INVALID_HANDLE_VALUE )
   {
      char szErr[FILENAME_MAX+80];
      sprintf (szErr, "Unable to open %s", pszFilename);
      HandleError (GetLastError(), szErr);
      return INVALID_HANDLE_VALUE;
   }

   return hFile;

}  /* Win32open */

/* ----------------------------------------------------------------- */

BOOL Win_GetInodeData (const char *szName)
{
   if (g_Inode.hFile)
	   CloseHandle (g_Inode.hFile);

   g_Inode.hFile = Win32open (szName, O_RDONLY);

   if (g_Inode.hFile == (HANDLE)-1)
      g_Inode.hFile = 0;

   return GetFileInformationByHandle(g_Inode.hFile, &g_Inode.Info);

}  /* Win_GetInodeData */

/* Return TRUE if files are the same, otherwise FALSE */

BOOL Win_CompareInodes (const char *szName)
{
   BY_HANDLE_FILE_INFORMATION Info = {0};

   GetFileInformationByHandle(Win32open (szName, O_RDONLY), &Info);

   if (Info.dwVolumeSerialNumber == g_Inode.Info.dwVolumeSerialNumber &&
       Info.nFileIndexHigh       == g_Inode.Info.nFileIndexHigh &&
       Info.nFileIndexLow        == g_Inode.Info.nFileIndexLow )
       return TRUE;
   else
      return FALSE;

}  /* Win_CompareInodes */

/* -----------------------------------------------------------------
     Specific version for egres
     Arguments:
      flags is expected to be empty
      errfunc is expected to be NULL

  This version returns the number of files found
   ----------------------------------------------------------------- */

int glob (const char *pattern, int flags,
          int errfunc(const char *epath, int eerrno),
          glob_t *pglob)
{
   WIN32_FIND_DATA fData;
   HANDLE hFile;
   int i = 0;

   hFile = FindFirstFile (pattern, &fData);

   if ( hFile == INVALID_HANDLE_VALUE )
   {
      DWORD dwErr = GetLastError ();
      fprintf (stderr, "Unable to find specified files %s", pattern);
      HandleError (dwErr, pattern);
      return i;
   }

   do
   {

      size_t iLen = strlen (fData.cFileName)+1;
      if (iLen <= 0)
         break;
      pglob->gl_pathv[i] = malloc (iLen);
      if (!pglob->gl_pathv[i])
      {
         fprintf (stderr, "Out of memory whilst globbing\n");
         return i;
      }

      strcpy (pglob->gl_pathv[i], fData.cFileName);
   }
   while (FindNextFile (hFile, &fData));

   FindClose (hFile);

   return i;

}  /* glob */

void globfree(glob_t *pglob)
{
   int i;

   for (i = 0; pglob->gl_pathv[i]; i++)
   {
      free (pglob->gl_pathv[i]);
   }


}  /* globfree */

/* -----------------------------------------------------------------
   Recursive !  Allows multiple directories
   ----------------------------------------------------------------- */

int mkdir (const char *path, mode_t mode)
{
   char drive[_MAX_DRIVE];
   char dir  [_MAX_DIR];   // For initial loop
   char fname[_MAX_FNAME];
   char ext  [_MAX_EXT];

   _splitpath (path, drive, dir, fname, ext);
   if ( dir[0] )
   {
      dir[strlen(dir)-1] = '\0';      // Remove final '/'
      mkdir (dir, mode);
   }

   if (!CreateDirectory (path, NULL))
   {
      DWORD iErr = GetLastError();

      return -1;
   }
   else
      return 0;

}   /* mkdir */

/* -----------------------------------------------------------------
   Assume READ/WRITE
   ----------------------------------------------------------------- */

void * mmap (void *start, size_t length, int prot, int flags, int fd, off_t offset)
{
   HANDLE hObject, hFile;
   void *pMap = (void *)MAP_FAILED;
   DWORD dwProtect = PAGE_READONLY;

   if ( flags == MAP_PRIVATE )
      dwProtect = PAGE_WRITECOPY;

   /* Convert Unix style file descriptor into a Win32 HANDLE */
   hFile = (HANDLE)_get_osfhandle( fd );

   hObject = CreateFileMapping (hFile, NULL,
                                dwProtect, 0, (DWORD)length, NULL);

   if (hObject)
   {
      DWORD dwAccess = FILE_MAP_READ;

      if ( flags == MAP_PRIVATE )
         dwAccess = FILE_MAP_COPY;

      pMap = MapViewOfFile (hObject, dwAccess, 0, offset, length);


      if ( !pMap )
         pMap = (void *)MAP_FAILED;
   }

   if (pMap == (void *)MAP_FAILED)
     HandleError (GetLastError(), "Unable to mmap");

   return pMap;

}  /* mmap */

int munmap (void *start, size_t length)
{
   BOOL bResult = FALSE;

   if ( start )
      bResult = UnmapViewOfFile (start);

   if (bResult)
      return 0;
   else
      return -1;

}  /* munmap */

/* ----------------------------------------------------------------- */

int getopt(int argc, char * const argv[], const char *optstring)
{
   int iRetn;

   optarg = NULL;

   if (argv[optind] && argv[optind][optpos] == '-')
   {
      /* New argument */
      optpos = 1;
      iRetn = opt_handling (argc, argv, optstring);
   }
   else
   {
      /* Another option in the same argument, or end of options */
      if ( optpos && argv[optind][optpos] )
         iRetn = opt_handling (argc, argv, optstring);
      else
         iRetn = EOF;
   }

   return iRetn;

}  /* getopt */

/* ----------------------------------------------------------------- */

static int opt_handling (int argc, char * const argv[], const char *optstring)
{
   int iRetn = EOF;

   if (argv[optind][optpos] != '-')
   {
      char *opt = strchr (optstring, argv[optind][optpos]);

      if (opt == NULL)
      {
         iRetn = '?';
         optopt = *optstring;
      }
      else
      {
         iRetn = *opt;
         optpos++;

         opt++;
         if ( *opt == ':')
         {
            /* Get next argument NOT FULLY IMPLEMENTED */
            if (argv[optind][optpos])
               optarg = &argv[optind][optpos];
            else
            {
               optind++;
               optarg = argv[optind];
               if ( !optarg )
                  iRetn = ':';
            }

            optind++;
            optpos = 0;

         }

         if ( !argv[optind][optpos] )
         {
            optind++;
            optpos = 0;
         }


      }
   }

   return iRetn;

}  /* opt_handling */

/* ----------------------------------------------------------------- */

BOOL OS_IsInteractive (HANDLE hIn)
{

   return (g_dwConsoleMode != 0xff);

}  /* OS_IsInteractive */

/* ----------------------------------------------------------------- */

void OS_GetScreenSize (HANDLE hOut, int *pWidth, int *pHeight)
{
   CONSOLE_SCREEN_BUFFER_INFO Info = {0};
   BOOL bRetn;
   HANDLE hToUse;

   hToUse = hOut;

   bRetn = GetConsoleScreenBufferInfo (hToUse, &Info);

   if ( bRetn )
   {
      *pWidth =  Info.srWindow.Right;
      *pHeight = Info.srWindow.Bottom - Info.srWindow.Top - 2;
   }

}   /* OS_GetScreenSize */

/* ----------------------------------------------------------------- */

void   OS_Name (char *buf, size_t count)
{
   OSVERSIONINFO OsVer;

   OsVer.dwOSVersionInfoSize = sizeof(OSVERSIONINFO);
   GetVersionEx (&OsVer);

   if ( OsVer.dwPlatformId == VER_PLATFORM_WIN32_NT )
   {
      sprintf (buf, "WinNT%d", OsVer.dwMajorVersion);
   }
   else
   {
      if (OsVer.dwMinorVersion == 0)
         strcpy (buf, "Win95");
      else
         strcpy (buf, "Win98");
   }

}  /* OS_Name */

/* ---------------------------------------------------------------- */

HANDLE OS_CreateStdOutFile (char *pszFilename, BOOL bAppend, HANDLE hErr)
{

   HANDLE hOutFile;
   DWORD dwFlags;
   SECURITY_ATTRIBUTES sa ;

   sa.nLength = sizeof (SECURITY_ATTRIBUTES);
   sa.lpSecurityDescriptor = NULL;
   sa.bInheritHandle = TRUE;

   if ( bAppend )
      dwFlags = OPEN_ALWAYS;
   else
      dwFlags = CREATE_ALWAYS;

   hOutFile = CreateFile (pszFilename, GENERIC_WRITE, FILE_SHARE_WRITE,
                              &sa, dwFlags, 0, NULL);

   if ( hOutFile == INVALID_HANDLE_VALUE )
   {
      char szErr[FILENAME_MAX+80];
      sprintf (szErr, "Unable to open %s\n", pszFilename);
      HandleError (GetLastError(), szErr);
   }
   else
   {
      if ( bAppend )
         SetFilePointer (hOutFile, 0, NULL, FILE_END);
   }

   return hOutFile;

}  /*  OS_CreateStdOutFile */

/* ---------------------------------------------------------------- */

HANDLE OS_OpenStdInFile (char *pszFilename, HANDLE hErr)
{
   SECURITY_ATTRIBUTES sa;
   HANDLE hInFile;

   sa.nLength = sizeof (SECURITY_ATTRIBUTES);
   sa.lpSecurityDescriptor = NULL;
   sa.bInheritHandle = TRUE;

   hInFile = CreateFile (pszFilename, GENERIC_READ, FILE_SHARE_READ,
                         &sa, OPEN_EXISTING, 0, NULL);

   if ( hInFile == INVALID_HANDLE_VALUE )
   {
      char szErr[FILENAME_MAX+80];
      sprintf (szErr, "Unable to open %s\n", pszFilename);
      HandleError (GetLastError(), szErr);
   }

   return hInFile;

}  /* OS_OpenStdInFile */

/* ---------------------------------------------------------------- */

void OS_CloseHandle (HANDLE hHandle)
{
   /* GetHandleInformation is unsupported on Win95/98/Me */

   if ( g_IsNT )
   {
      DWORD dwInfo;

      if (GetHandleInformation (hHandle, &dwInfo))
         CloseHandle (hHandle);
   }
   else
   {
      CloseHandle (hHandle);
   }

}  /* OS_CloseHandle */

/* ----------------------------------------------------------------- */


void OS_GetPid (char *szPid)
{
   DWORD dwTid = GetCurrentThreadId ();

   if ( !g_IsNT )
   {
      dwTid ^= 0xfff70000;
   }

   sprintf (szPid, "%d", dwTid);

}  /* OS_GetPid */

/* -----------------------------------------------------------------

   ----------------------------------------------------------------- */

char *basename (char *path)
{
   char drive    [_MAX_DRIVE];
   char dir      [_MAX_DIR];
   char ext      [_MAX_EXT];
   char basename [_MAX_FNAME];
   char *ptr;

   _splitpath (path, drive, dir, basename, ext);

   ptr = path + strlen(drive) + strlen(dir);

   return ptr;

 }   /* OS_basename */


/* -----------------------------------------------------------------

   ----------------------------------------------------------------- */

BOOL OS_isdir (const char *path, HANDLE hErr)
{
   DWORD dwFileAttributes = 0;

   dwFileAttributes = GetFileAttributes (path);

   if ( dwFileAttributes == -1 )
      return 0;
   else
      return (dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY);

}  /* OS_isdir */

/* ----------------------------------------------------------------- */


BOOL OS_isfile (const char *path, HANDLE hErr)
{
   DWORD dwFileAttributes = 0;

   dwFileAttributes = GetFileAttributes (path);

   if ( dwFileAttributes == -1 )
      return 0;
   else
      return !(dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY);

}  /* OS_isfile */

/* ----------------------------------------------------------------- */

BOOL OS_CheckFileAccess (const char *szFilename, int iMode)
{
   int mode;

   switch (iMode)
   {
      case PERM_EXISTS:
         mode = 0;
         break;
      case PERM_WRITE:
         mode = 2;
         break;
      case PERM_READ:
         mode = 4;
         break;
      case PERM_READ_WRITE:
         mode = 6;
         break;
      case PERM_EXECUTE:
         mode = 4;         /* No execute permission on Win */
         break;
      default:
         return FALSE;
   }

   if ( _access (szFilename, mode) == 0 )
      return TRUE;
   else
      return FALSE;

}  /* OS_CheckFileAccess */

/* ----------------------------------------------------------------- */

static void HandleError (DWORD dwErrorNo, const char *pszMsg)
{
   if ( dwErrorNo )
	{
      char oserr [256] = {0};
      DWORD dwSize;

      dwSize = FormatMessage (FORMAT_MESSAGE_FROM_SYSTEM,
                     NULL, dwErrorNo,
                     MAKELANGID(LANG_NEUTRAL, SUBLANG_DEFAULT),
                     oserr, 255, NULL);

      /* FormatMessage puts \r\n on EOL */
      fprintf (stderr, "%s: %s", pszMsg, oserr);

   }

}  // HandleError

// --------------------------------------------------------------------
