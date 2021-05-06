#!/usr/bin/python3


def common_elements(set_1, set_2):
    new_eq_set = []
    list_1 = list(set_1)
    list_2 = list(set_2)
    for i in list_1:
        for j in list_2:
            if j == i:
                new_eq_set.append(j)
    return set(new_eq_set)
