/*
   Tidy.c

   Delete .o files
   chmod u+x .sh files
*/
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <dirent.h>
#include <sys/stat.h>
#include "Python.h"

/* Local Prototypes */
void HandleDirectory (const char *DirName);
void HandleFile (const char *FileName);

/* Python specifics
   #include "python.h"
   Add a TidyMethods array to include "TidyDir"
   Add a PyMethodDef struct called Tidy_module
   Add a PyInit_tidy

   Most work is to be done on main():
      change to TidyDir
      change the prototype to take and return pointers to Python objects
      convert the parameter handling in main to use PyArg_ParseTuple
      check that the return values are converted into Python objects
          return TRUE on success and FALSE on error
      check that any error messages use PySys_WriteStderr()
*/

PyObject * TidyDir(PyObject *, PyObject *);

static PyMethodDef TidyMethods[] = {
    {"TidyDir", TidyDir, METH_VARARGS,"Simple Example."},
    {NULL, NULL, 0, NULL}
};

static PyModuleDef Tidy_module = {
   PyModuleDef_HEAD_INIT,
   "Tidy",
   NULL,
   -1,
   TidyMethods
};

PyMODINIT_FUNC PyInit_Tidy(void)
{
    return PyModule_Create(&Tidy_module);
}

/*
int main (int argc, char *argv[])
*/
static PyObject * TidyDir(PyObject *self, PyObject *args)
{
   const char *dir = "";    /* avoids an "unintialised" warning */
   if (!PyArg_ParseTuple(args,"z",&dir))
       return NULL;

   if (dir) {
      struct stat sbuf;

      if ( stat(dir, &sbuf) < 0 ) {
          PySys_WriteStderr("Unable to open %s: %s\n",
                            dir, strerror(errno));
          Py_RETURN_FALSE;
      }
      if ( !S_ISDIR(sbuf.st_mode) ) {
          PySys_WriteStderr("%s is not a directory\n", dir);
          Py_RETURN_FALSE;
      }
   }
   else {
      dir = ".";
   }

   HandleDirectory(dir);

   Py_RETURN_TRUE;

}  /* main */

static void HandleDirectory (const char *DirName)
{
   DIR *theDir;
   struct dirent *dentp;

   PySys_WriteStderr("HandleDirectory on %s\n", DirName);
   /*
    * Go through the directory, processing all the entries
    */
   if ( (theDir = opendir(DirName)) != NULL )
   {
      while((dentp=readdir(theDir)))
      {
         struct stat sbuf;
         char pathName[PATH_MAX+1];

         /* Skip . and .. */
         if ( !strcmp(dentp->d_name, "." ) ||
              !strcmp(dentp->d_name, ".." ))
             continue;

         sprintf(pathName, "%s/%s", DirName, dentp->d_name);
         if ( stat(pathName, &sbuf) < 0 ) {
            PySys_WriteStderr("Unable to open %s: %s\n",
                               pathName, strerror(errno));
            continue;
         }

         if ( S_ISDIR(sbuf.st_mode) )
             HandleDirectory(pathName);      /* Recursion */
         else
             HandleFile(pathName);

      }

      closedir(theDir);
   }
   else {
      PySys_WriteStderr("Unable to open %s: %s\n",
                        DirName, strerror(errno));
   }

}  /* HandleDirectory */


static void HandleFile (const char * FileName)
{
    /* Are we interested in this file? */
    size_t len = strlen(FileName);

    if (!strcmp(&FileName[len-2], ".o")) {
        printf ("Deleting %s...\n", FileName);
        if (unlink (FileName) == -1)
            PySys_WriteStderr("Unable to unlink %s: %s\n",
                               FileName, strerror(errno));
    }
    else if (!strcmp(&FileName[len-3], ".sh")) {

        struct stat statbuf;

        if (stat(FileName, &statbuf) == -1) {
            PySys_WriteStderr("Unable to stat %s: %s\n",
                               FileName, strerror(errno));
        }
        else {
            statbuf.st_mode |= S_IXUSR;
            printf ("Adding execute access to %s\n", FileName);

            if (chmod(FileName, statbuf.st_mode) == -1)
                PySys_WriteStderr("Unable to chmod %s: %s\n",
                               FileName, strerror(errno));
        }
    }

}  /* HandleFile */

