#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
from collections import defaultdict
from collections import Counter


def freqQuery(queries):
    """
    more performance
    """
    results = []
    lookup = dict()
    freqs = defaultdict(set)
    for command, value in queries:
        freq = lookup.get(value, 0)
        if command == 1:
            lookup[value] = freq + 1
            freqs[freq].discard(value)
            freqs[freq + 1].add(value)
        elif command == 2:
            lookup[value] = max(0, freq - 1)
            freqs[freq].discard(value)
            freqs[freq - 1].add(value)
        elif command == 3:
            results.append(1 if freqs[value] else 0)
    return results


def freqQuery2(queries):
    """
    bad performance
    """
    ans = []
    d = {}
    for o, v in queries:
        if o == 1:
            d[v] = d.get(v, 0) + 1
        elif o == 2:
            if d.get(v, 0) > 0:
                d[v] = d[v] - 1
        elif o == 3:
            if v in d.values():
                ans.append(1)
            else:
                ans.append(0)

    return ans


def freqQuery3(queries):
    freq = Counter()
    cnt = Counter()
    result = []
    for action, value in queries:
        if action == 1:
            cnt[freq[value]] -= 1
            freq[value] += 1
            cnt[freq[value]] += 1
        elif action == 2:
            if freq[value] > 0:
                cnt[freq[value]] -= 1
                freq[value] -= 1
                cnt[freq[value]] += 1
        else:
            result.append(1 if cnt[value] > 0 else 0)
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
