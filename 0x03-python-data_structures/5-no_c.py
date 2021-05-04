#!/usr/bin/python3


def no_c(my_string):
    new_strin = []
    for i in my_string:
        if i == 'c' or i == 'C':
            new_strin.append('')
        else:
            new_strin.append(i)
    return "".join(new_strin)
