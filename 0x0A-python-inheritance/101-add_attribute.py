#!/usr/bin/python3

"""
101-add_attribute.py: unction that adds a new
                    attribute to an object if it’s possible
"""


def add_attribute(cls, key, value):
    """Adding attributes to a class
    Args:
        key (string): key to add
        value (string): value to add
    """
    if not hasattr(cls, "__dict__") and not hasattr(cls, "__slots__"):
        raise TypeError("can't add new attribute")
    setattr(cls, key, value)
