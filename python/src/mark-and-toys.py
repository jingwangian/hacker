#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.


def maximumToys(prices, k):
    prices = sorted(prices)
    print(prices)
    count = cost = 0
    for price in prices:
        if cost + price <= k:
            count += 1
            cost += price
        else:
            break
    return count


prices = [int(x) for x in '1 12 5 111 200 1000 10'.split()]
k = 50
ret = maximumToys(prices, k)
print(ret)
exit(0)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
