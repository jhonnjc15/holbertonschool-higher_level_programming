#!/usr/bin/python3


"""4-print_square: module that prints squares"""


def print_square(size):
    """print square prints a square to the stdout the size of the size given
    Args:
        size (int): size of the square you want
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is not float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
