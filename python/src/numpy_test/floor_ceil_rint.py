#!/usr/bin/env python3

import numpy as np

np.set_printoptions(sign=' ')
input_list = list(map(float, input().strip().split()))
arr = np.array(input_list)

print(np.floor(arr))
print(np.ceil(arr))
print(np.rint(arr))