#!/usr/bin/python3


"""5-square.py: class Square that defines a square """


class Square:
    """Class Square"""
    def __init__(self, size=0, position=(0, 0)):
        """initializes the square with a size and position
        Args:
            size (int): size of length
            position (int): 2 coordinate position
        """
        if (type(position) is tuple) and (len(position) == 2):
            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

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
        """sets the size of the square
        Args:
            value (int): the value to set the square lenght to
        """
        if type(value) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """returns the area of the square"""
        return self.__size * self.__size

    @property
    def position(self):
        """returns the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets the position values
        Args:
            value (int): the tuple value to set the position
        """
        if (type(value) is tuple) and (len(value) == 2):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """Prints the a square in # the size of the square
        Args:
            None
        Returns:
            None
        """
        for i in range(self.__position[1]):
            print("")

        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                count = 0
                for j in range(self.__size):
                    if count == 0:
                        for k in range(self.__position[0]):
                            print(" ", end="")
                        count = count + 1
                    print("#", end="")
                print("")
