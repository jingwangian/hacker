#!/usr/bin/env python3

import numpy as np

"""
sum

The sum tool returns the sum of array elements over a given axis.

my_array = numpy.array([ [1, 2], [3, 4] ])

print numpy.sum(my_array, axis = 0)         #Output : [4 6]
print numpy.sum(my_array, axis = 1)         #Output : [3 7]
print numpy.sum(my_array, axis = None)      #Output : 10
print numpy.sum(my_array)                   #Output : 10

prod

The prod tool returns the product of array elements over a given axis.

my_array = numpy.array([ [1, 2], [3, 4] ])

print numpy.prod(my_array, axis = 0)            #Output : [3 8]
print numpy.prod(my_array, axis = 1)            #Output : [ 2 12]
print numpy.prod(my_array, axis = None)         #Output : 24
print numpy.prod(my_array)                      #Output : 24
"""

# my_array = np.array([2,3])

# print(np.prod(my_array))
# print(np.prod(my_array, axis=0))
# print(np.prod(my_array, axis=None))

# exit(0)

N, M = map(int, input().strip().split())

line_list1 = [list(map(int, input().strip().split())) for x in range(N)]

arr = np.array(line_list1)

arr1 = np.sum(arr,axis=0)

print(arr1)
arr2 = np.prod(arr1,axis=0)

print(arr2)



