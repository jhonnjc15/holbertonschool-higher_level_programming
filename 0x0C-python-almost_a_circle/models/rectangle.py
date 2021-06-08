#!/usr/bin/python3

"""Rectangle module"""

from models.base import Base


class Rectangle(Base):
    """Rectangle class, that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor
        Args:
            width : width of the rectangle
            height : heifth of the rectangle
            x : the x position
            y : the y position
            id : id
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Return the width of rectangle instance"""
        return self.__width

    @property
    def height(self):
        """Return the height of the instance"""
        return self.__height

    @property
    def x(self):
        """Return the x-position property"""
        return self.__x

    @property
    def y(self):
        """Returns the y-pisition property"""
        return self.__y

    @width.setter
    def width(self, value):
        """Set the width
        Args:
            value :  value to set
        """
        self.__width = value

    @height.setter
    def height(self, value):
        """Set the height
        Args:
            value :  value to set
        """
        self.__height = value

    @x.setter
    def x(self, value):
        """Set x
        Args:
            value :  value to set
        """
        self.__x = value

    @y.setter
    def y(self, value):
        """Set y
        Args:
            value :  value to set
        """
        self.__y = value
