#!/usr/bin/python3


"""3-square.py: Create a Square Class"""


class Square:
    """Class Square: initializes an instance with the size attributes"""
    def __init__(self, size=0):
        """
        initialize the square class with size.
        Has to be greater than 0 and of an int class
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

    def area(self):
        """
        Args:
            None
        Return:
            Int - Area of the square
        """
        return self.__size * self.__size
