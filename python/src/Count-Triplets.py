#!/bin/python3

import math
import os
import random
import re
import sys

from itertools import combinations
from collections import Counter
# Complete the countTriplets function below.


def istriplet(arr, r):
    print(arr)
    if arr[1] == arr[0] * r and arr[2] == arr[1] * r:
        return True

    return False


def countTriplets_3(arr, r):
    count = 0
    dict = {}
    dictPairs = {}

    for i in reversed(arr):
        if i * r in dictPairs:
            count += dictPairs[i * r]
        if i * r in dict:
            dictPairs[i] = dictPairs.get(i, 0) + dict[i * r]

        dict[i] = dict.get(i, 0) + 1

    return count


def countTriplets_2(arr, r):
    r2 = Counter()
    r3 = Counter()
    count = 0

    for v in arr:
        if v in r3:
            count += r3[v]
            print("v= {},count ={}".format(v, count))

        if v in r2:
            r3[v * r] += r2[v]

        r2[v * r] += 1

        print(v, r2, r3)

    return count


def countTriplets(arr, r):
    count = 0
    for item in combinations(arr, 3):
        if istriplet(item, r):
            count += 1

    return count


arr = [int(x) for x in '1 3 9 9 27 81'.split()]
r = 3
ret = countTriplets_2(arr, r)
print(ret)

exit(0)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
