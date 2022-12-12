/* Solution */
#include <string.h>
#include <stdio.h>
#include <Python.h>

static PyObject * MkList(PyObject *self, PyObject *args);

/* ------------------------------------------------------------------ */

// Globals
static PyMethodDef MkListMethods[] = {
    {"MkList",  MkList, METH_VARARGS, "Create a list from a dictionary."},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

static struct PyModuleDef MkList_module = {
   PyModuleDef_HEAD_INIT,
   "MkList",  /* name of module */
   NULL,      /* module documentation, may be NULL */
   -1,        /* size of per-interpreter state of the module,
                or -1 if the module keeps state in global variables. */
   MkListMethods
};

/* Module entry point */

PyMODINIT_FUNC
PyInit_MkList(void)
{
    return PyModule_Create(&MkList_module);
}

/* ----------------------------------------------------------------------------------------------- */

static PyObject * MkList(PyObject *self, PyObject *args)
{
	PyObject * pDict;
	PyObject * RetnList = PyList_New(0);
	PyObject * pKey;
	PyObject * pValue;
	Py_ssize_t pos = 0;

	if (! PyArg_ParseTuple(args, "O!", &PyDict_Type, &pDict))
	    Py_RETURN_NONE;

    while (PyDict_Next(pDict, &pos, &pKey, &pValue))
    {
		int iRetn;
		iRetn = PyList_Append(RetnList, pKey);
		if (iRetn == -1) Py_RETURN_NONE;

		iRetn = PyList_Append(RetnList, pValue);
		if (iRetn == -1) Py_RETURN_NONE;
	}

    return RetnList;
}