#!/usr/bin/python3

"""MyInt class"""


class MyInt(int):
    """MyInt Class, inherits from the int class"""
    def __init__(self, number):
        """Initializes value to int
        """
        self.__number = number

    def __eq__(self, other):
        """ Checks for non equality !=
        """
        return self.__number != other

    def __ne__(self, other):
        """Checks for equality ==
        """
        return self.__number == other

    def __str__(self):
        """Prints out the string format of the value"""
        return "{}".format(self.__number)
