#!/usr/bin/python3

"""Module that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """
        Function that appends a string at the end of a text file
    """
    with open(filename, mode='a', encoding='utf-8') as f:
        num_cha_added = f.write(text)
    return num_cha_added
