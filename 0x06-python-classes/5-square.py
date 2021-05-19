#!/usr/bin/python3


"""5-square.py: class Square that defines a square """


class Square:
    """Class Square"""
    def __init__(self, size=0):
        """initialize instance with size
        Note:
            has to be greater than 0 and of an int class
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

    @property
    def size(self):
        """returns the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size of a length of the square"""
        if type(value) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Returns the area of the square instance
        Args:
            None
        Returns:
            Area of the square instance
        """
        return self.__size * self.__size

    def my_print(self):
        """Prints the a square in # the size of the square
        Args:
            None
        Returns:
            None
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")
