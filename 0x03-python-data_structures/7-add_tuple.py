#!/usr/bin/python3


def add_zeros(lists):
    for i in range(2):
        if len(lists) != 2:
            lists.append(0)
    return lists[0:2]


def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = []
    list_a = list(tuple_a)
    list_b = list(tuple_b)

    add_zeros(list_a)
    add_zeros(list_b)

    for i, j in zip(list_a, list_b):
        new_tuple.append(i + j)
    return tuple(new_tuple)
