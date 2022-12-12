/*
   Win32Specifics.h
      Version 1.0

      egres version, based on yash v1.14

*/

#ifndef _INCLUDE_WIN32SPECIFICS
#define _INCLUDE_WIN32SPECIFICS

#define _CRT_SECURE_NO_WARNINGS
#include <windows.h>
#include <process.h>
#include <stdio.h>
#include <io.h>
#include <stdlib.h>
#include <malloc.h>

#define LINE_TERMINATOR    "\r\n"
#define MAX_LINE (256)

#define S_IFIFO     (0)             // Not on Windows
#define PROT_READ   (0)
#define PROT_WRITE  (1)
#define MAP_PRIVATE (1)
#define MAP_FAILED  ((void *)(-1))

#define PERM_EXISTS     (0)
#define PERM_WRITE      (2)
#define PERM_READ       (4)
#define PERM_READ_WRITE (6)
#define PERM_EXECUTE    (8)

#define alloca _alloca

typedef DWORD pid_t;
typedef DWORD mode_t;

typedef long off_t;



struct dirent
{
   WIN32_FIND_DATA fData;
   char *d_name;
};

typedef struct
{
    struct dirent *pdirent;
	HANDLE hFile;
	BOOL bFindFirst;
} DIR;

typedef struct
{
   char *gl_pathv[];

} glob_t;

/* getopt globals */
extern int   opterr;
extern int   optind;
extern int   optopt;
extern char *optarg;

/* egres Prototypes */
DIR  * opendir(const char *name);
struct dirent *readdir(DIR *dir);
int    closedir (DIR *dir);
int    glob (const char *pattern, int flags,
             int errfunc(const char *epath, int eerrno),
             glob_t *pglob);
void   globfree(glob_t *pglob);
int    mkdir (const char *path, mode_t mode);
void * mmap (void *start, size_t length, int prot, int flags, int fd, off_t offset);
int    munmap (void *start, size_t length);
char * basename (char *path);
int    getopt(int argc, char * const argv[], const char *optstring);
HANDLE Win32open (const char *pszFilename, int mode);
BOOL   Win_GetInodeData  (const char *szName);
BOOL   Win_CompareInodes (const char *szName);

/* yash Prototypes */
int    OS_chdir            (const char *path, HANDLE hErr);
int    OS_rmdir            (const char *path, HANDLE hErr);
BOOL   OS_isdir            (const char *path, HANDLE hErr);
BOOL   OS_isfile           (const char *path, HANDLE hErr);

void   OS_GetPid           (char *szPid);
void   OS_Setup            (void);
void   OS_Shutdown         (void);
BOOL   OS_IsInteractive    (HANDLE hIn);

void   OS_GetScreenSize    (HANDLE hOut, int *pWidth, int *pHeight);
void   OS_Name             (char *buf, size_t count);
BOOL   OS_CheckFileAccess  (const char *szFilename, int iMode);

#endif  /* _INCLUDE_WIN32SPECIFICS */
