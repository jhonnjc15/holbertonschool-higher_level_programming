#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = []
    list_a = list(tuple_a)
    list_b = list(tuple_b)

    for i in range(2):
        if len(list_a) != 2:
            list_a.append(0)
        if len(list_b) != 2:
            list_b.append(0)

    for i, j in zip(list_a[:2], list_b[:2]):
        new_tuple.append(i + j)
    return tuple(new_tuple)
