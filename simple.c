#include <Python.h>

PyObject * Hello(PyObject *, PyObject *); # prototype

static PyMethodDef SimpleMethods[] = {
    {"Hello", Hello, METH_NOARGS, "Says Hello World!"},
    {NULL, NULL, 0, NULL}
}; # Method registration table

static struct PyModuleDef Simple_module = {
   PyModuleDef_HEAD_INIT,
   "Simple",
   "Test Module",
   -1,
   SimpleMethods
};

PyMODINIT_FUNC PyInit_Simple(void)
{
    return PyModule_Create(&Simple_module);
}

static PyObject * Hello(PyObject *self, PyObject *args)
{
    printf("Hello, World!\n");
    return Py_None;
}
