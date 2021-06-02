#!/usr/bin/python3

""" 2-is_same_class.py:
        Module that checks is an object is of a specific class
"""


def is_same_class(obj, a_class):
    """
    Returns:
        True if the object is
    exactly an instance of the specified class ; otherwise False
    """
    if type(obj) == a_class:
        return True
    else:
        return False
