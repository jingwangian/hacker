#!/bin/python3

import sys


def alternatingCharacters(s):
    # Complete this function
    deleted_num = 0
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            deleted_num += 1

    return deleted_num


q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = alternatingCharacters(s)
    print(result)
