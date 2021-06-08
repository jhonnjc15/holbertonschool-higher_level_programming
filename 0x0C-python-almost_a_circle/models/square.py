#!/usr/bin/python3

"""Square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor
        Args:
            size : size of the square
            x : x-position
            y : y-position
            id : id
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Return string representation of itself
        """
        return "[Square] ({}) "\
               "{}/{} - {}".format(self.id, self.x, self.y, self.height)

    @property
    def size(self):
        """Return the size if the square instance"""
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the size of the square
        Args:
            value: value to set
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
