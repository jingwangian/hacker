#!/usr/bin/env python3

import numpy

"""
Zeros and Ones

The zeros tool returns a new array with a given shape and type filled with 's.
"""
print(numpy.zeros((1, 2)))  # Default type is float
# Output : [[ 0.  0.]]

print(numpy.zeros((1, 2), dtype=numpy.int))  # Type changes to int
# Output : [[0 0]]

"""
ones

The ones tool returns a new array with a given shape and type filled with 's.
"""
print(numpy.ones((1, 2)))  # Default type is float
# Output : [[ 1.  1.]]

print(numpy.ones((1, 2), dtype=numpy.int))  # Type changes to int
# Output : [[1 1]]


print(numpy.ones(((1, 2), (3, 4, 5)), dtype=numpy.int))
