#!/usr/bin/python3

"""0-lookup.py: Looks up the attributes of an object"""


def lookup(obj):

    """ Args:
        obj: Any object being passed
        Return: the list of available attributes and methods
    """

    return dir(obj)
