#include <Python.h>
/**
 * print_python_list_info - prints python list info
 * @p: pyobject
 */
void print_python_list_info(PyObject *p)
{
	int size, alloc, i;
	PyObject *r;

	size = Py_SIZE(p);
	/*cast PyObject to PyList Object*/
	alloc = ((PyListObject *)p)->allocated;
	/*Print header info for list object*/
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);
	/*Print each object for list*/
	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);
		r = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(r)->tp_name);
	}
}
