// -*- C++ -*-
// 
// michael a.g. aïvázis
// california institute of technology
// (c) 1998-2012 all rights reserved
// 


#include <portinfo>
#include <Python.h>

// turn on GSL inlining
#define HAVE_INLINE
#include <gsl/gsl_matrix.h>
#include "matrix.h"

#include <iostream>

// local
static void free(PyObject *);
static const char * capsule_t = "gsl.matrix";


// construction
const char * const gsl::matrix::allocate__name__ = "matrix_allocate";
const char * const gsl::matrix::allocate__doc__ = "allocate a matrix";

PyObject * 
gsl::matrix::allocate(PyObject *, PyObject * args) {
    // place holders for the python arguments
    size_t s0, s1;
    // unpack the argument tuple
    int status = PyArg_ParseTuple(args, "(kk):matrix_allocate", &s0, &s1);
    // if something went wrong
    if (!status) return 0;

    // allocate a matrix
    gsl_matrix * v = gsl_matrix_alloc(s0, s1);
    // std::cout << " gsl.matrix_allocate: matrix@" << v << ", size=" << length << std::endl;

    // wrap it in a capsule and return it
    return PyCapsule_New(v, capsule_t, free);
}


// initialization
const char * const gsl::matrix::zero__name__ = "matrix_zero";
const char * const gsl::matrix::zero__doc__ = "zero out the elements of a matrix";

PyObject * 
gsl::matrix::zero(PyObject *, PyObject * args) {
    // the arguments
    PyObject * capsule;
    // unpack the argument tuple
    int status = PyArg_ParseTuple(args, "O!", &PyCapsule_Type, &capsule);
    // if something went wrong
    if (!status) return 0;
    // bail out if the capsule is not valid
    if (!PyCapsule_IsValid(capsule, capsule_t)) {
        PyErr_SetString(PyExc_TypeError, "invalid matrix capsule");
        return 0;
    }

    // get the matrix
    gsl_matrix * v = static_cast<gsl_matrix *>(PyCapsule_GetPointer(capsule, capsule_t));
    // std::cout << " gsl.matrix_zero: matrix@" << v << std::endl;
    // zero it out
    gsl_matrix_set_zero(v);

    // return None
    Py_INCREF(Py_None);
    return Py_None;
}


const char * const gsl::matrix::fill__name__ = "matrix_fill";
const char * const gsl::matrix::fill__doc__ = "set all elements of a matrix to a value";

PyObject * 
gsl::matrix::fill(PyObject *, PyObject * args) {
    // the arguments
    double value;
    PyObject * capsule;
    // unpack the argument tuple
    int status = PyArg_ParseTuple(args, "O!d", &PyCapsule_Type, &capsule, &value);
    // if something went wrong
    if (!status) return 0;
    // bail out if the capsule is not valid
    if (!PyCapsule_IsValid(capsule, capsule_t)) {
        PyErr_SetString(PyExc_TypeError, "invalid matrix capsule");
        return 0;
    }

    // get the matrix
    gsl_matrix * v = static_cast<gsl_matrix *>(PyCapsule_GetPointer(capsule, capsule_t));
    // std::cout << " gsl.matrix_fill: matrix@" << v << ", value=" << value << std::endl;
    // fill it out
    gsl_matrix_set_all(v, value);

    // return None
    Py_INCREF(Py_None);
    return Py_None;
}


const char * const gsl::matrix::identity__name__ = "matrix_identity";
const char * const gsl::matrix::identity__doc__ = "build an identity matrix";

PyObject * 
gsl::matrix::identity(PyObject *, PyObject * args) {
    // the arguments
    size_t index;
    PyObject * capsule;
    // unpack the argument tuple
    int status = PyArg_ParseTuple(args, "O!k", &PyCapsule_Type, &capsule, &index);
    // if something went wrong
    if (!status) return 0;
    // bail out if the capsule is not valid
    if (!PyCapsule_IsValid(capsule, capsule_t)) {
        PyErr_SetString(PyExc_TypeError, "invalid matrix capsule");
        return 0;
    }

    // get the matrix
    gsl_matrix * v = static_cast<gsl_matrix *>(PyCapsule_GetPointer(capsule, capsule_t));
    // std::cout << " gsl.matrix_identity: matrix@" << v << ", index=" << index << std::endl;
    // fill it out
    gsl_matrix_set_identity(v);

    // return None
    Py_INCREF(Py_None);
    return Py_None;
}


// access
const char * const gsl::matrix::get__name__ = "matrix_get";
const char * const gsl::matrix::get__doc__ = "get the value of a matrix element";

PyObject * 
gsl::matrix::get(PyObject *, PyObject * args) {
    // the arguments
    PyObject * capsule;
    size_t index0, index1;
    // unpack the argument tuple
    int status = PyArg_ParseTuple(args, "O!kk", &PyCapsule_Type, &capsule, &index0, &index1);
    // if something went wrong
    if (!status) return 0;
    // bail out if the capsule is not valid
    if (!PyCapsule_IsValid(capsule, capsule_t)) {
        PyErr_SetString(PyExc_TypeError, "invalid matrix capsule");
        return 0;
    }

    // get the matrix
    gsl_matrix * v = static_cast<gsl_matrix *>(PyCapsule_GetPointer(capsule, capsule_t));
    // get the value
    double value = gsl_matrix_get(v, index0, index1);
    // std::cout
        // << " gsl.matrix_get: matrix@" << v << ", index=" << index << ", value=" << value 
        // << std::endl;

    // return the value
    return PyFloat_FromDouble(value);
}


const char * const gsl::matrix::set__name__ = "matrix_set";
const char * const gsl::matrix::set__doc__ = "set the value of a matrix element";

PyObject * 
gsl::matrix::set(PyObject *, PyObject * args) {
    // the arguments
    double value;
    PyObject * capsule;
    size_t index0, index1;
    // unpack the argument tuple
    int status = PyArg_ParseTuple(
                                  args, "O!kkd",
                                  &PyCapsule_Type, &capsule, &index0, &index1, &value);
    // if something went wrong
    if (!status) return 0;
    // bail out if the capsule is not valid
    if (!PyCapsule_IsValid(capsule, capsule_t)) {
        PyErr_SetString(PyExc_TypeError, "invalid matrix capsule");
        return 0;
    }

    // get the matrix
    gsl_matrix * v = static_cast<gsl_matrix *>(PyCapsule_GetPointer(capsule, capsule_t));
    // std::cout
        // << " gsl.matrix_set: matrix@" << v << ", index=" << index << ", value=" << value 
        // << std::endl;
    // set the value
    gsl_matrix_set(v, index0, index1, value);

    // return None
    Py_INCREF(Py_None);
    return Py_None;
}


const char * const gsl::matrix::contains__name__ = "matrix_contains";
const char * const gsl::matrix::contains__doc__ = "check whether a given value appears in matrix";

PyObject * 
gsl::matrix::contains(PyObject *, PyObject * args) {
    // the arguments
    double value;
    PyObject * capsule;
    // unpack the argument tuple
    int status = PyArg_ParseTuple(args, "O!d", &PyCapsule_Type, &capsule, &value);
    // if something went wrong
    if (!status) return 0;
    // bail out if the capsule is not valid
    if (!PyCapsule_IsValid(capsule, capsule_t)) {
        PyErr_SetString(PyExc_TypeError, "invalid matrix capsule");
        return 0;
    }

    // get the matrix
    gsl_matrix * v = static_cast<gsl_matrix *>(PyCapsule_GetPointer(capsule, capsule_t));
    // std::cout
        // << " gsl.matrix_contains: matrix@" << v << ", index=" << index << ", value=" << value 
        // << std::endl;

    // the answer
    PyObject * result = Py_False;

    // loop over the elements
    for (size_t index0=0; index0 < v->size1; index0++) {
        for (size_t index1=0; index1 < v->size2; index1++) {
            // if i have a match
            if (value == gsl_matrix_get(v, index0, index1)) {
                // update the answer
                result = Py_True;
                // and bail
                break;
            }
        }
    }

    // return the answer
    Py_INCREF(result);
    return result;
}


// minima and maxima
const char * const gsl::matrix::max__name__ = "matrix_max";
const char * const gsl::matrix::max__doc__ = "find the largest value contained";

PyObject * 
gsl::matrix::max(PyObject *, PyObject * args) {
    // the arguments
    PyObject * capsule;
    // unpack the argument tuple
    int status = PyArg_ParseTuple(args, "O!", &PyCapsule_Type, &capsule);
    // if something went wrong
    if (!status) return 0;
    // bail out if the capsule is not valid
    if (!PyCapsule_IsValid(capsule, capsule_t)) {
        PyErr_SetString(PyExc_TypeError, "invalid matrix capsule");
        return 0;
    }

    // get the matrix
    gsl_matrix * v = static_cast<gsl_matrix *>(PyCapsule_GetPointer(capsule, capsule_t));
    double value = gsl_matrix_max(v);
    // std::cout << " gsl.matrix_max: matrix@" << v << ", value=" << value << std::endl;

    // return the value
    return PyFloat_FromDouble(value);
}


const char * const gsl::matrix::min__name__ = "matrix_min";
const char * const gsl::matrix::min__doc__ = "find the smallest value contained";

PyObject * 
gsl::matrix::min(PyObject *, PyObject * args) {
    // the arguments
    PyObject * capsule;
    // unpack the argument tuple
    int status = PyArg_ParseTuple(args, "O!", &PyCapsule_Type, &capsule);
    // if something went wrong
    if (!status) return 0;
    // bail out if the capsule is not valid
    if (!PyCapsule_IsValid(capsule, capsule_t)) {
        PyErr_SetString(PyExc_TypeError, "invalid matrix capsule");
        return 0;
    }

    // get the matrix
    gsl_matrix * v = static_cast<gsl_matrix *>(PyCapsule_GetPointer(capsule, capsule_t));
    double value = gsl_matrix_min(v);
    // std::cout << " gsl.matrix_max: matrix@" << v << ", value=" << value << std::endl;

    // return the value
    return PyFloat_FromDouble(value);
}


const char * const gsl::matrix::minmax__name__ = "matrix_minmax";
const char * const gsl::matrix::minmax__doc__ = 
    "find both the smallest and the largest value contained";

PyObject * 
gsl::matrix::minmax(PyObject *, PyObject * args) {
    // the arguments
    PyObject * capsule;
    // unpack the argument tuple
    int status = PyArg_ParseTuple(args, "O!", &PyCapsule_Type, &capsule);
    // if something went wrong
    if (!status) return 0;
    // bail out if the capsule is not valid
    if (!PyCapsule_IsValid(capsule, capsule_t)) {
        PyErr_SetString(PyExc_TypeError, "invalid matrix capsule");
        return 0;
    }

    // get the matrix
    gsl_matrix * v = static_cast<gsl_matrix *>(PyCapsule_GetPointer(capsule, capsule_t));
    double small, large;
    gsl_matrix_minmax(v, &small, &large);
    // std::cout 
        // << " gsl.matrix_max: matrix@" << v << ", min=" << small << ", max=" << large 
        // << std::endl;

    // build the answer
    PyObject * answer = PyTuple_New(2);
    PyTuple_SET_ITEM(answer, 0, PyFloat_FromDouble(small));
    PyTuple_SET_ITEM(answer, 1, PyFloat_FromDouble(large));
    // and return
    return answer;
}


// in-place operations
const char * const gsl::matrix::add__name__ = "matrix_add";
const char * const gsl::matrix::add__doc__ = "in-place addition of two matrices";

PyObject * 
gsl::matrix::add(PyObject *, PyObject * args) {
    // the arguments
    PyObject * self;
    PyObject * other;
    // unpack the argument tuple
    int status = PyArg_ParseTuple(args, "O!O!", &PyCapsule_Type, &self, &PyCapsule_Type, &other);
    // if something went wrong
    if (!status) return 0;
    // bail out if the two capsules are not valid
    if (!PyCapsule_IsValid(self, capsule_t) || !PyCapsule_IsValid(other, capsule_t)) {
        PyErr_SetString(PyExc_TypeError, "invalid matrix capsule");
        return 0;
    }

    // get the two matrices
    gsl_matrix * v1 = static_cast<gsl_matrix *>(PyCapsule_GetPointer(self, capsule_t));
    gsl_matrix * v2 = static_cast<gsl_matrix *>(PyCapsule_GetPointer(other, capsule_t));
    // std::cout << " gsl.matrix_add: matrix@" << v1 << ", matrix@" << v2 << std::endl;
    // perform the addition
    gsl_matrix_add(v1, v2);

    // return None
    Py_INCREF(Py_None);
    return Py_None;
}


const char * const gsl::matrix::sub__name__ = "matrix_sub";
const char * const gsl::matrix::sub__doc__ = "in-place subtraction of two matrices";

PyObject * 
gsl::matrix::sub(PyObject *, PyObject * args) {
    // the arguments
    PyObject * self;
    PyObject * other;
    // unpack the argument tuple
    int status = PyArg_ParseTuple(args, "O!O!", &PyCapsule_Type, &self, &PyCapsule_Type, &other);
    // if something went wrong
    if (!status) return 0;
    // bail out if the two capsules are not valid
    if (!PyCapsule_IsValid(self, capsule_t) || !PyCapsule_IsValid(other, capsule_t)) {
        PyErr_SetString(PyExc_TypeError, "invalid matrix capsule");
        return 0;
    }

    // get the two matrices
    gsl_matrix * v1 = static_cast<gsl_matrix *>(PyCapsule_GetPointer(self, capsule_t));
    gsl_matrix * v2 = static_cast<gsl_matrix *>(PyCapsule_GetPointer(other, capsule_t));
    // std::cout << " gsl.matrix_sub: matrix@" << v1 << ", matrix@" << v2 << std::endl;
    // perform the subtraction
    gsl_matrix_sub(v1, v2);

    // return None
    Py_INCREF(Py_None);
    return Py_None;
}


const char * const gsl::matrix::mul__name__ = "matrix_mul";
const char * const gsl::matrix::mul__doc__ = "in-place multiplication of two matrices";

PyObject * 
gsl::matrix::mul(PyObject *, PyObject * args) {
    // the arguments
    PyObject * self;
    PyObject * other;
    // unpack the argument tuple
    int status = PyArg_ParseTuple(args, "O!O!", &PyCapsule_Type, &self, &PyCapsule_Type, &other);
    // if something went wrong
    if (!status) return 0;
    // bail out if the two capsules are not valid
    if (!PyCapsule_IsValid(self, capsule_t) || !PyCapsule_IsValid(other, capsule_t)) {
        PyErr_SetString(PyExc_TypeError, "invalid matrix capsule");
        return 0;
    }

    // get the two matrices
    gsl_matrix * v1 = static_cast<gsl_matrix *>(PyCapsule_GetPointer(self, capsule_t));
    gsl_matrix * v2 = static_cast<gsl_matrix *>(PyCapsule_GetPointer(other, capsule_t));
    // std::cout << " gsl.matrix_mul: matrix@" << v1 << ", matrix@" << v2 << std::endl;
    // perform the multiplication
    gsl_matrix_mul_elements(v1, v2);

    // return None
    Py_INCREF(Py_None);
    return Py_None;
}


const char * const gsl::matrix::div__name__ = "matrix_div";
const char * const gsl::matrix::div__doc__ = "in-place division of two matrices";

PyObject * 
gsl::matrix::div(PyObject *, PyObject * args) {
    // the arguments
    PyObject * self;
    PyObject * other;
    // unpack the argument tuple
    int status = PyArg_ParseTuple(args, "O!O!", &PyCapsule_Type, &self, &PyCapsule_Type, &other);
    // if something went wrong
    if (!status) return 0;
    // bail out if the two capsules are not valid
    if (!PyCapsule_IsValid(self, capsule_t) || !PyCapsule_IsValid(other, capsule_t)) {
        PyErr_SetString(PyExc_TypeError, "invalid matrix capsule");
        return 0;
    }

    // get the two matrices
    gsl_matrix * v1 = static_cast<gsl_matrix *>(PyCapsule_GetPointer(self, capsule_t));
    gsl_matrix * v2 = static_cast<gsl_matrix *>(PyCapsule_GetPointer(other, capsule_t));
    // std::cout << " gsl.matrix_div: matrix@" << v1 << ", matrix@" << v2 << std::endl;
    // perform the division
    gsl_matrix_div_elements(v1, v2);

    // return None
    Py_INCREF(Py_None);
    return Py_None;
}


const char * const gsl::matrix::shift__name__ = "matrix_shift";
const char * const gsl::matrix::shift__doc__ = "in-place addition of a constant to a matrix";

PyObject * 
gsl::matrix::shift(PyObject *, PyObject * args) {
    // the arguments
    double value;
    PyObject * self;
    // unpack the argument tuple
    int status = PyArg_ParseTuple(args, "O!d", &PyCapsule_Type, &self, &value);
    // if something went wrong
    if (!status) return 0;
    // bail out if the two capsules are not valid
    if (!PyCapsule_IsValid(self, capsule_t)) {
        PyErr_SetString(PyExc_TypeError, "invalid matrix capsule");
        return 0;
    }

    // get the two matrices
    gsl_matrix * v = static_cast<gsl_matrix *>(PyCapsule_GetPointer(self, capsule_t));
    // std::cout << " gsl.matrix_shift: matrix@" << v << ", value=" << value << std::endl;
    // perform the shift
    gsl_matrix_add_constant(v, value);

    // return None
    Py_INCREF(Py_None);
    return Py_None;
}


const char * const gsl::matrix::scale__name__ = "matrix_scale";
const char * const gsl::matrix::scale__doc__ = "in-place scaling of a matrix by a constant";

PyObject * 
gsl::matrix::scale(PyObject *, PyObject * args) {
    // the arguments
    double value;
    PyObject * self;
    // unpack the argument tuple
    int status = PyArg_ParseTuple(args, "O!d", &PyCapsule_Type, &self, &value);
    // if something went wrong
    if (!status) return 0;
    // bail out if the two capsules are not valid
    if (!PyCapsule_IsValid(self, capsule_t)) {
        PyErr_SetString(PyExc_TypeError, "invalid matrix capsule");
        return 0;
    }

    // get the two matrices
    gsl_matrix * v = static_cast<gsl_matrix *>(PyCapsule_GetPointer(self, capsule_t));
    // std::cout << " gsl.matrix_scale: matrix@" << v << ", value=" << value << std::endl;
    // perform the scale
    gsl_matrix_scale(v, value);

    // return None
    Py_INCREF(Py_None);
    return Py_None;
}


// destructor
void free(PyObject * capsule)
{
    // bail out if the capsule is not valid
    if (!PyCapsule_IsValid(capsule, capsule_t)) return;
    // get the matrix
    gsl_matrix * v = static_cast<gsl_matrix *>(PyCapsule_GetPointer(capsule, capsule_t));
    // std::cout << " gsl.matrix_free: matrix@" << v << std::endl;
    // deallocate
    gsl_matrix_free(v);
    // and return
    return;
}


// end of file
