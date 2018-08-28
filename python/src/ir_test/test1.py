#!/bin/python3


def solution(M, A):
    N = len(A)
    count = [0] * (M + 1)
    maxOccurence = 0
    index = 0
    for i in range(N):
        print("A[{}] = {}".format(i, A[i]))
        if count[A[i]] > 0:
            tmp = count[A[i]] + 1
            if tmp > maxOccurence:
                maxOccurence = tmp
                # print(maxOccurence, tmp, i)
                index = i
            count[A[i]] = tmp
        else:
            count[A[i]] = 1

    return A[index]


a = [3, 1, 1, 3, 4, 3, 1, 1]
ret = solution(5, a)
print(ret)
