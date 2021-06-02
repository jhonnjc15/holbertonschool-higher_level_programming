#!/usr/bin/python3

"""8-rectangle.py: MOdule that create a class Rectangle.
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
        Create a Rectange class that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
        Args:
            width:The width of the rectangle.
            height:The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__height = height
        self.__width = width
