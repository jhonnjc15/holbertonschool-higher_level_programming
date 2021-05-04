#!/usr/bin/python3


def max_integer(my_list=[]):
    max_num = my_list[0]
    if len(my_list) == 0:
        return None
    else:
        for i in my_list:
            for j in my_list:
                if max_num < j:
                    max_num = j
                    break
        return max_num
