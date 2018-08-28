#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter
# Complete the makeAnagram function below.

c3 = Counter({'red': 4, 'blue': 2})
c4 = Counter({'red': 4, 'blue': 3, 'ye': 8})
c5 = Counter({'red': 4, 'blue': 3})

t = c4 - c3
print(len(c3))
for k, v in c3.items():
    print(k, v)

# print(t.values)
print(list(t.items()))


def check_valiable_insert(c1, c2):
    x = c2 - c1
    diff_list = list(x.items())
    if len(diff_list) > 1:
        return None
    else:
        return diff_list[0][0] if diff_list[0][1] == 1 else None
        print(diff_list)


ret = check_insert(c3, c5)

print(ret)
