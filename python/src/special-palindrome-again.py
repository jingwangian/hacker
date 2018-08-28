#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.


def triangular_number(*args):
    pass


def substrCount(n, s):
    """
    Really simple 3 pass solution:
    1. Build a list of tuples such that the string "aaabbc" can be squashed down to [("a", 3), ("b", 2), ("c", 1)].
    2. add to answer all combinations of substrings from these tuples which would represent palindromes which have all same letters.
    3. traverse this list to specifically find the second case mentioned in probelm

    """
    l = []
    count = 0
    cur = None

# 1st pass
    for i in range(n):
        if s[i] == cur:
            count += 1
        else:
            if cur is not None:
                l.append((cur, count))
            cur = s[i]
            count = 1
    l.append((cur, count))

    ans = 0

    print(l)
# 2nd pass
    for i in l:
        print(i[1])
        ans += (i[1] * (i[1] + 1)) // 2

# 3rd pass
    for i in range(1, len(l) - 1):
        if l[i - 1][0] == l[i + 1][0] and l[i][1] == 1:
            ans += min(l[i - 1][1], l[i + 1][1])

    return ans


def substrCount_1(n, s):
    count = len(s)

    exp1 = r'(([a-z])\2*)(?!\1)(?=[a-z]\1)'
    m = re.finditer(exp1, s)
    count += sum([len(x.group(0)) for x in m])

    exp2 = r'([a-z])\1+'
    m = re.finditer(exp2, s)
    count += sum([triangular_number(len(x.group(0)) - 1) for x in m])

    return count


ret = substrCount(5, 'asasd')
print(ret)
exit(0)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
