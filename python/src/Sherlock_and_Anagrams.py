#!/bin/python3

<<<<<<< HEAD
=======
"""
Sherlock and Anagrams
"""
>>>>>>> 00b76c9e4f3b68f92f6be902664c8887655f0e84
import math
import os
import random
import re
import sys

<<<<<<< HEAD
from collections import Counter
# Complete the sherlockAndAnagrams function below.


def sherlockAndAnagrams(s):
    buckets = {}
    for i in range(len(s)):
        for j in range(1, len(s) - i + 1):
            key = frozenset(Counter(s[i:i + j]).items())  # O(N) time key extract
=======
from itertools import permutations, product, combinations
from collections import Counter


# Complete the sherlockAndAnagrams function below.

def sherlockAndAnagrams(s):
    # def count_anagrams(string):
    buckets = {}
    #search from the first 
    for i in range(len(s)):
        for j in range(1, len(s) - i + 1):
            key = frozenset(Counter(s[i:i + j]).items())  # O(N) time key extract
            # print(key)
>>>>>>> 00b76c9e4f3b68f92f6be902664c8887655f0e84
            buckets[key] = buckets.get(key, 0) + 1
    count = 0
    for key in buckets:
        count += buckets[key] * (buckets[key] - 1) // 2
<<<<<<< HEAD
        print("{} : {}".format(key, buckets[key]))
    return count


print(sherlockAndAnagrams('ifailuhkqq'))
print(sherlockAndAnagrams('kkkk'))


exit(0)
=======
    return count


s = 'ifailuhkqq'

print(sherlockAndAnagrams(s))
print(sherlockAndAnagrams('kkkk'))

exit(0)

>>>>>>> 00b76c9e4f3b68f92f6be902664c8887655f0e84
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
