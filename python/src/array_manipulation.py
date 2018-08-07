#!/bin/python3


import math
import os
import random
import re
import sys
from collections import defaultdict
# Complete the arrayManipulation function below.


def arrayManipulation(n, queries):
    array = [0] * n

    for start, stop, num in queries:
        for i in range(start, stop + 1):
            array[i - 1] += num

        # print("{},{},{},   array --> {}, ".format(start, stop, num, array))

    return max(array)


def arrayManipulation2(n, queries):
    array = defaultdict(int)

    max_value = 0
    for start, stop, num in queries:
        for i in range(start, stop + 1):
            array[i] += num

    return max(array.values())


def test_case4():
    queries = []
    file_name = 'array_manipulation_testcase4.txt'
    with open(file_name) as f:
        n, m = map(int, f.readline().strip().split())

        for line in f:
            line = line.strip()
            queries.append(list(map(int, line.split())))

    result = arrayManipulation2(n, queries)

    print(result)


def main():
    input_str = """5 3
    1 2 100
    2 5 100
    3 4 100
    """

    queries = []

    input_array = input_str.splitlines()
    n, m = map(int, input_array[0].strip().split())
    [queries.append(list(map(int, a.strip().split()))) for a in input_array[1:] if len(a.strip())]

    print(queries)

    result = arrayManipulation2(n, queries)

    print(result)


if __name__ == '__main__':

    # main()
    test_case4()

    exit(0)

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
