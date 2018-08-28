#!/usr/bin/env python3

import numpy as np

N,M = map(int,input().strip().split())

line_list1 = [list(map(int,input().strip().split())) for x in range(N)]

line_list2 = [list(map(int,input().strip().split())) for x in range(N)]

arr1 = np.array(line_list1)
arr2 = np.array(line_list2)

print(arr1+arr2)
print(arr1-arr2)
print(arr1*arr2)
print(arr1//arr2)
print(arr1%arr2)
print(arr1**arr2)

"""
input:
1 4
1 2 3 4
5 6 7 8
"""