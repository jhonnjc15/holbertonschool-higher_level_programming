#!/usr/bin/python3

"""10-square.py: MOdule that create a class Square.
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
        Create a Square class that inherits from Rectangle
    """
    def __init__(self, size):
        """
        Args:
            width:The width of the rectangle.
            height:The height of the rectangle.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """" Returns the area of the Square """
        return self.__size ** 2

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
