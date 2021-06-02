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

    def to_json(self, attrs=None):
        """
        Method that returns the objetive dictionary
        Args:
            attrs (str): list of strings
        """
        if attrs is None:
            return self.__dict__

        new_dict = {}
        for attr in attrs:
            if attr in self.__dict__:
                new_dict[attr] = self.__dict__[attr]
        return new_dict
