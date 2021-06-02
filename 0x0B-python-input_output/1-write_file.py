#!/usr/bin/python3

"""Module that write a string to a text file"""


def write_file(filename="", text=""):
    """
        Function that write a string
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        num_charac = f.write(text)
    return num_charac
