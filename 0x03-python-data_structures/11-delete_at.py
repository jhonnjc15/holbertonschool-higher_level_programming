#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    drop_element = my_list[idx]
    my_list.remove(drop_element)
    return my_list
