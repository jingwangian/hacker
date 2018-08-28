#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.


def makeAnagram(a, b):
    count = 0
    for i in range(97, 123):
        ia = sum(letter == chr(i) for letter in a)
        ib = sum(letter == chr(i) for letter in b)
        print(ia, ib, chr(i))
        count += abs(ia - ib)
    return count


ret = makeAnagram('cdex', 'abcxa')
print('ret = ', ret)
exit(0)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
