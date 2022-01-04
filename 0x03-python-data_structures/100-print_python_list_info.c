#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	int Py_ssize_t = PyList_Size(*p);
	int i;
	PyListObject *obj = (PyListObject*)p;

	printf("[*] Size of the Python List = %li\n", Py_ssize_t);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (i = 0; i < size; i++)
		printf("Element %i: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
}