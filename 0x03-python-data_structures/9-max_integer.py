#!/usr/bin/python3


def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        max_num = my_list[0]
        for i in my_list:
            for j in my_list:
                if max_num < j:
                    max_num = j
                    break
        return max_num
