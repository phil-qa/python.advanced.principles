/*
   Tidy.c

   Delete .o or .obj files
   chmod u+x .sh files
*/

#define _CRT_SECURE_NO_WARNINGS
#include <windows.h>
#include "Win32Specifics.h"
#define S_IXUSR (0)
#define unlink _unlink
#define chmod  _chmod

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <sys/stat.h>

/* Local Prototypes */
void HandleDirectory (const char *DirName);
void HandleFile (const char *FileName);

/* Python specifics
   #include "Python.h"
   Add a TidyMethods array to include "TidyDir"
   Add a PyMethodDef struct called Tidy_module
   Add a PyInit_Tidy

   Most work is to be done on main():
      change to TidyDir
      change the prototype to take and return pointers to Python objects
      convert the parameter handling in main to use PyArg_ParseTuple
      check that the return values are converted into Python objects
          return TRUE on success and FALSE on error
      check that any error messages use PySys_WriteStderr()
*/

int main (int argc, char *argv[])
{
   const char *dir = "";    /* avoids an "unitialised" warning */

   if (argc > 1) {
      struct stat sbuf;
      dir = argv[1];

      if ( stat(dir, &sbuf) < 0 ) {
          fprintf (stderr,"Unable to open %s: %s\n",
                           dir, strerror(errno));
          return 1;
      }

      if ( ! sbuf.st_mode & S_IFDIR ) {
          fprintf (stderr,"%s is not a directory\n", dir);
          return 1;
      }

   }
   else {
      dir = ".";
   }

   HandleDirectory(dir);

   return 0;

}  /* main */

void HandleDirectory (const char *DirName)
{
   DIR *theDir;
   struct dirent *dentp;

   fprintf (stderr,"HandleDirectory on %s\n", DirName);
   /*
    * Go through the directory, processing all the entries
    */
   if ( (theDir = opendir(DirName)) != NULL )
   {
      while((dentp=readdir(theDir)))
      {
         struct stat sbuf;
         char pathName[FILENAME_MAX+1];

         /* Skip . and .. */
         if ( !strcmp(dentp->d_name, "." ) ||
              !strcmp(dentp->d_name, ".." ))
             continue;

         sprintf(pathName, "%s/%s", DirName, dentp->d_name);
         if ( stat(pathName, &sbuf) < 0 ) {
            fprintf (stderr,"Unable to open %s: %s\n",
                             pathName, strerror(errno));
            continue;
         }

         if ( sbuf.st_mode & S_IFDIR )
             HandleDirectory(pathName);      /* Recursion */
         else
             HandleFile(pathName);

      }

      closedir(theDir);
   }
   else {
      fprintf (stderr,"Unable to open %s: %s\n",
                     DirName, strerror(errno));
   }

}  /* HandleDirectory */


void HandleFile (const char * FileName)
{
    /* Are we interested in this file? */
    size_t len = strlen(FileName);

	if (len > 4 && !strcmp(&FileName[len-4], ".obj")) {
        printf ("Deleting %s...\n", FileName);
        if (unlink (FileName) == -1)
            fprintf (stderr,"Unable to unlink %s: %s\n",
                             FileName, strerror(errno));
    }
    else if (!strcmp(&FileName[len-3], ".sh")) {

        struct stat statbuf;

        if (stat(FileName, &statbuf) == -1) {
            fprintf (stderr,"Unable to stat %s: %s\n",
                             FileName, strerror(errno));
        }
        else {
            statbuf.st_mode |= S_IXUSR;
            printf ("Adding execute access to %s\n", FileName);

            if (chmod(FileName, statbuf.st_mode) == -1)
                fprintf (stderr,"Unable to chmod %s: %s\n",
                         FileName, strerror(errno));
        }
    }

}  /* HandleFile */

