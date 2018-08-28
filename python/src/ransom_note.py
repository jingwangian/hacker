#!/bin/python3

"""
Ransom Note
"""

import math
import os
import random
import re
import sys

from collections import Counter
from collections import defaultdict

# Complete the checkMagazine function below.


def ransom_note(magazine, rasom):
    return not (Counter(rasom) - Counter(magazine))


def ransom_note_2(magazine, ransom):
    dicty = defaultdict(int)
    for word in magazine:
        dicty[word] += 1
    for word in ransom:
        if dicty[word] == 0:
            return False
        dicty[word] -= 1
    return True


def checkMagazine(magazine, note):
    if ransom_note(magazine, note):
        print('Yes')
    else:
        print('No')


m = "ive got a lovely bunch coconuts of coconuts"
n = "ive got some coconuts"

# m = "apgo clm w lxkvg mwz elo bg elo lxkvg elo apgo apgo w elo bg"
# n = "elo lxkvg bg mwz clm w"

m = m.split()
n = n.split()


c1 = Counter(m)
c2 = Counter(n)
print(c1)
print(c2)
print(c1 - c2)
print(c2 - c1)
cx1 = c2.subtract(c1)
cx = c2 - c1
print(cx1)
print(cx == {})

checkMagazine(m, n)

exit(0)


def ransom_note(magazine, rasom):
    return (Counter(rasom) - Counter(magazine)) == {}


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
