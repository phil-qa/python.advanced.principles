/* Solution */
#include <string.h>
#include <Python.h>

static PyObject * MkDict(PyObject *self, PyObject *args, PyObject *kwdict);

/* ------------------------------------------------------------------ */

// Globals
static PyMethodDef MkDictMethods[] = {
    // {"MkDict",  MkDict, METH_VARARGS, "Create a dictionary from two lists."},
    {"MkDict",  (PyCFunction)MkDict, METH_VARARGS|METH_KEYWORDS, "Create a dictionary from two lists."},
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

static PyObject * MkDict(PyObject *self, PyObject *args, PyObject *kwdict)
{
	int num_keys;
	int num_vals;
	Py_ssize_t i;

    static char *keywords[] = {"keys", "values", NULL};

	PyObject * keys;
	PyObject * vals;
	PyObject * RetnDict = PyDict_New();

    /*
	if (! PyArg_ParseTuple(args, "O!O!",
	                       &PyList_Type, &keys, &PyList_Type, &vals))
	    Py_RETURN_NONE;
    */

	if (! PyArg_ParseTupleAndKeywords(args, kwdict, "O!O!", keywords,
	                       &PyList_Type, &keys, &PyList_Type, &vals))
	    Py_RETURN_NONE;


	num_keys = PyList_Size(keys);
	num_vals = PyList_Size(vals);

	/*
	   If num_keys < num_vals, ignore the extra values
	   If num_keys > num_vals, set those values without keys to None
	*/

    for (i = 0; i < num_keys; i++)
    {
		PyObject * value;
		PyObject * key;
		int iRetn;

		key = PyList_GetItem(keys, i);

        if (i > num_vals - 1)
			value = Py_None;
	    else
	        value = PyList_GetItem(vals, i);

	    iRetn = PyDict_SetItem(RetnDict, key, value);

	    if (iRetn == -1)
	        Py_RETURN_NONE;

	}

    return RetnDict;
}
