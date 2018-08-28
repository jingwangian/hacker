#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter


def ransom_note(magazine, rasom):
    return not (Counter(rasom) - Counter(magazine))


def checkMagazine(magazine, note):
    if ransom_note(magazine, note):
        print('Yes')
    else:
        print('No')


checkMagazine('give me one grand today night',
              'give one grand today')

exit(0)

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
