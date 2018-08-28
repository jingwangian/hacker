#!/bin/python3

from collections import Counter

IMPOSSIBLE = 'IMPOSSIBLE'
SWAP = 'SWAP {} {}'
INSERT = 'INSERT {}'
DELETE = 'DELETE {}'
NOTHING = 'NOTHING'


#!/usr/bin/env python3

INSERT = 'INSERT {}'
DELETE = 'DELETE {}'
SWAP = 'SWAP {} {}'
IMPOSSIBLE = 'IMPOSSIBLE'
NOTHING = 'NOTHING'


def find_swap(l1, l2):
    """
    len(l1) == len(l2)
    """

    diff_list = [(l1[i], l2[i]) for i in range(len(l1)) if l1[i] != l2[i]]

    if len(diff_list) != 2:
        return IMPOSSIBLE
    else:
        if set(diff_list[0]) == set(diff_list[1]):
            return SWAP.format(diff_list[0][0], diff_list[0][1])


def find_less_one(l1, l2):
    """
    len(l1) <len(l2)
    """
    x = Counter(l2) - Counter(l1)
    diff_list = list(x.items())
    if len(diff_list) > 1:
        return None
    else:
        return diff_list[0][0] if diff_list[0][1] == 1 else None


def solution(S, T):
    set1 = set(S)
    set2 = set(T)

    len_T = len(T)
    len_S = len(S)
    if abs(len_T - len_S) >= 2:
        return IMPOSSIBLE

    if len(set1 ^ set2) >= 2:
        return IMPOSSIBLE

    if S == T:
        return NOTHING

    if len_T == len_S:
        return find_swap(S, T)
    elif len_T - len_S == 1:
        ret = find_less_one(S, T)
        return INSERT.format(ret) if ret else IMPOSSIBLE

    elif len_S - len_T == 1:
        ret = find_less_one(T, S)
        return DELETE.format(ret) if ret else IMPOSSIBLE

    return IMPOSSIBLE


# ret = solution('A', 'AB')
# print(ret)

# ret = solution('ABD', 'AB')
# print(ret)

# ret = solution('ADC', 'ABDC')
# print(ret)

# ret = solution('ADC', 'DC')
# print(ret)

# ret = solution('AB', 'ABC')
# print(ret)

# ret = solution('AB', 'ADB')
# print(ret)

# ret = solution('nice', 'niece')
# print(ret)

# ret = solution('form', 'from')
# print(ret)

# ret = solution('form', 'fmro')
# print(ret)

# ret = solution('mrof', 'from')
# print(ret)

# ret = solution('romf', 'from')
# print(ret)
