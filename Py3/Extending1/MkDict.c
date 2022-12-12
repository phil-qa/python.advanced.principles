/* Delegate version */
#include <string.h>
#include <Python.h>

// TODO: Insert prototype here

/* ------------------------------------------------------------------ */

// Globals
static PyMethodDef MkDictMethods[] = {
    {"MkDict",  MkDict, METH_VARARGS, "Create a dictionary from two lists."},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

static struct PyModuleDef MkDict_module = {
   PyModuleDef_HEAD_INIT,
   "MkDict",  /* name of module */
   NULL,      /* module documentation, may be NULL */
   -1,        /* size of per-interpreter state of the module,
                or -1 if the module keeps state in global variables. */
   MkDictMethods
};

/* Module entry point */

PyMODINIT_FUNC
PyInit_MkDict(void)
{
    return PyModule_Create(&MkDict_module);
}

/* ----------------------------------------------------------------------------------------------- */

PyObject * MkDict(PyObject *self, PyObject *args)
{
	PyObject * RetnDict = PyDict_New();

	// TODO: Define a PyObject * for the keys and the values lists

    // TODO: Call PyArg_ParseTuple to extract the list from args

    // TODO: Create a loop to loop through the lists

    	/*
    	   TODO:
    	   If number of keys < number of vals, ignore the extra values
    	   If number of keys > number of vals, set those values without keys to None
    	   (use PyList_Size)
    	*/

    	// TODO:  Add the key and value to RetnDict
    	//        (use PyList_GetItem and PyDict_SetItem)
    	//        Return None on error

    return RetnDict;
}
