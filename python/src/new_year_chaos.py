#!/bin/python3

import math
import os
import random
import re
import sys

def new_year_chao(q):
    lastIndex = len(q) - 1
    swaps = 0
    swaped = False
    
    # check if the q is too chaotic
    for i, v in enumerate(q):
        if (v - 1) - i > 2:
            return "Too chaotic"

    # bubble sorting to find the answer
    for i in range(0, lastIndex):
        print("i = ",i)
        for j in range(0, lastIndex):
            a,b = q[j],q[j+1]
            if q[j] > q[j+1]:
                q[j],q[j+1] = q[j+1], q[j]
                swaps += 1
                swaped = True

            print(q, "{} --{}, swap = {}".format(a,b, 'True' if a>b else 'False'))
        
        if swaped:
            swaped = False
        else:
            break
    return swaps

def new_year_chao_2(q):
    len_q = len(q)
    total_steps = 0
    for i in map(lambda x,y: x-y, q, range(1,len_q+1)):
        if i >2:
            return "Too chaotic"

    for i in range(0,len_q-1):
        steps = 0
        for j in range(i+1, len_q):
            if q[i] > q[j]:
                steps +=1
        if steps >2:
            return 'Too chaotic'
        else:
            total_steps +=  steps

    return total_steps


# Complete the minimumBribes function below.
def minimumBribes(q):
    print(new_year_chao(q))


def test_minimumBribes():
    qs = [
        [2,1,5,3,4],
        [2,5,1,3,4],
        [1,2,5,3,7,8,6,4],
        [7, 1, 3, 2, 4, 5, 6]
    ]
    for q in qs[3:]:
        minimumBribes(q)

test_minimumBribes()
exit(0)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
