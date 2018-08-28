#!/bin/python3

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from collections import defaultdict
from datetime import time


def get_total_seconds(duration):
    h, m, s = map(int, duration.split(':'))

    return h * 3600 + m * 60 + s


def get_one_call_fee(total_seconds):
    if total_seconds < 300:
        return total_seconds * 3
    else:
        fee = int(total_seconds / 60 + (1 if total_seconds % 60 else 0)) * 150
        return fee


def get_total_fee(phone_call_dict):

    fee_list = [get_one_call_fee(x) for x in phone_call_dict.values()]
    fee_list.sort(reverse=True)

    return sum(fee_list[1:])


def solution(S):
    # write your code in Python 3.6
    call_list = [x.strip() for x in S.splitlines()]
    phone_call_dict = defaultdict(int)
    for call in call_list:
        duration, phone_number = call.split(',')

        phone_call_dict[phone_number] = phone_call_dict[phone_number] + get_total_seconds(duration)

    fees = get_total_fee(phone_call_dict)

    return fees


# s = """00:01:07,400-234-090
#    00:05:01,701-080-080
#    00:05:00,400-234-090"""
# ret = solution(s)
# print(ret)


s = """00:01:07,400-234-090
   00:05:01,701-080-080
   00:05:00,400-234-090
   00:06:01,400-234-091
   00:01:07,400-234-093
   00:05:00,400-234-093"""
ret = solution(s)
print(ret)
