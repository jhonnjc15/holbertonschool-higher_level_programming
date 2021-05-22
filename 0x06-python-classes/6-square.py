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
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        elif (len(position) is not 2 or type(position[0]) is not int or
              type(position[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__size = size
            self.__position = position

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
        if int(value[0]) is not int or int(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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
            for i in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                count = 0
                for j in range(self.__size):
                    if count == 0:
                        for k in range(self.__position[0]):
                            print(" ", end="")
                        count = count + 1
                    print("#", end="")
                print("")
