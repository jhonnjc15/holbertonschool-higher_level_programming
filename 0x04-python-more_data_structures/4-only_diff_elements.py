#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    new_eq_set = []
    new_dif_set = []
    list_1 = list(set_1)
    list_2 = list(set_2)
    for i in list_1:
        for j in list_2:
            if j == i:
                new_eq_set.append(j)
    for i in new_eq_set:
        if i in list_1:
            list_1.remove(i)
    for i in new_eq_set:
        if i in list_2:
            list_2.remove(i)

    return set(list_1 + list_2)
