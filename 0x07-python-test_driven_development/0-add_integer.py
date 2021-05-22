#!/usr/bin/python3


"""0-add_integer.py:  module that return the sum of two numbers"""


def add_integer(a, b=98):
    """Add integer adds two integers together that are int types
    Args:
        a (int): first integer
        b (int): second integer
    Returns:
        int: a + b
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
