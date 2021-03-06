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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Set the height
        Args:
            value :  value to set
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Set x
        Args:
            value :  value to set
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Set y
        Args:
            value :  value to set
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Return the area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        Print a rectangle with '#'s
        """
        for i in range(self.__y):
            print("")

        for i in range(self.__height):
            print(self.__x * " " + self.__width * "#", end="")
            print("")

    def __str__(self):
        """
        Return string of rectangle instance's stats
        """
        return "[Rectangle] ({})"\
               " {}/{} - {}/{}".format(self.id, self.__x, self.__y,
                                       self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
        Update the instances with new arguments
        Args:
            args: tuple with the new arguments
            kwargs: a dictionary with new arguments
        """
        if args:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.__width = args[i]
                if i == 2:
                    self.__height = args[i]
                if i == 3:
                    self.__x = args[i]
                if i == 4:
                    self.__y = args[i]

        elif kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.__width = value
                if key == "height":
                    self.__height = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value

    def to_dictionary(self):
        """
        Return a dictionary with all the arguments
        """
        return {"id": self.id, "width": self.__width,
                "height": self.__height, "x": self.__x, "y": self.__y}
