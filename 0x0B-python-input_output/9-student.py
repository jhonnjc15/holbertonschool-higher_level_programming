#!/usr/bin/python3

"""Module that Writes a class Student that defines a student"""


class Student:
    """
    Student class
    """
    def __init__(self, first_name, last_name, age):
        """
        Constructor
        Args:
            first_name (str): firstname
            last_name (str): lastname
            age (int): age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Method that returns the objetive dictionary
        """
        return self.__dict__
