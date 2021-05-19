#!/usr/bin/python3


"""Class Square"""


class Square:
    """Class Square: initializes with the size attribute"""
    def __init__(self, size=0):
        """
        initialize the square class with size
        Args:
        size (int): size of length or width of square
        Returns:
        None
        """
        if type(size) is int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
