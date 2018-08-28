#!/usr/bin/env python3

import numpy as np

"""
identity
The identity tool returns an identity array. An identity array is a square
 matrix with all the main diagonal elements as  and the rest as . 
 The default type of elements is float.

eye

The eye tool returns a 2-D array with 's as the diagonal and 's elsewhere.
 The diagonal can be main, upper or lower depending on the optional parameter.
 A positive  is for the upper diagonal, a negative  is for the lower, and a 
 (default) is for the main diagonal.
"""
np.set_printoptions(sign=' ')
print(np.identity(3))

"""
#Output
[[ 1.  0.  0.]
 [ 0.  1.  0.]
 [ 0.  0.  1.]]
"""


arr2 = np.eye(8,7,k=1)

print(arr2.shape, arr2.ndim)
print(arr2)

n,m = map(int,input("please input n and m: ").strip().split())
print(n,m)
print(np.eye(n,m))