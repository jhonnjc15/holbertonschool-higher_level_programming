#!/usr/bin/python3


def weight_average(my_list=[]):
    if not my_list:
        return 0
    sum_, divi = 0, 0
    for tup in my_list:
        sum_ = sum_ + tup[0] * tup[1]
        divi = divi + tup[1]
    return sum_ / divi
