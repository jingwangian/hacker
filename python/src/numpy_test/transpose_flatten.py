#!/usr/bin/env python3

import numpy

my_array = numpy.array([[1, 2, 3], [4, 5, 6]])

t = numpy.transpose(my_array)

print(t)

t1 = t.flatten()
print(t1)


array_1 = numpy.array([1, 2, 3])
array_2 = numpy.array([[4, 5, 6], [3, 2]])
array_3 = numpy.array([7, 8, 9, 10])

c1 = numpy.concatenate((array_1, array_2, array_3))

print(c1)


"""
If an array has more than one dimension, it is possible to specify the axis along which multiple arrays are concatenated. By default, it is along the first dimension.

array_1 = numpy.array([[1,2,3],[0,0,0]])
array_2 = numpy.array([[0,0,0],[7,8,9]])

print numpy.concatenate((array_1, array_2), axis = 1)

#Output
[[1 2 3 0 0 0]
 [0 0 0 7 8 9]]
"""

array_1 = numpy.array([[1, 2, 3], [4, 5, 6]])
array_2 = numpy.array([[0, 0, 0], [7, 8, 9]])

print(numpy.concatenate((array_1, array_2)))
print(numpy.concatenate((array_1, array_2), axis=1))
