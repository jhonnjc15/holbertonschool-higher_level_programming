#!/usr/bin/python3

"""7-base_geometry.py: MOdule that create a class BaseGeometry"""


class BaseGeometry:
    """
        Create a BaseGeometry class
    """
    def area(self):
        """
            Area method
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            Checks if value is a integer
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
