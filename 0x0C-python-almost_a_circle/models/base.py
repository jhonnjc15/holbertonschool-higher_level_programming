#!/usr/bin/python3


"""Base module"""
import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor
        Args:
            id (int) : id of each instance object.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns JSON string representation of list_dictionaries
        Args:
            list_dictionaries : list of dictionaries
        """
        if list_dictionaries is None or []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Create objects from object instances, then save to json file
        Args:
            cls (class): the class of the object instances
            list_objs (list): list of class objects
        """
        filename = cls.__name__ + ".json"
        with open(filename, mode="w", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                objs = [cls.to_dictionary(obj) for obj in list_objs]
                f.write(cls.to_json_string(objs))

    @staticmethod
    def from_json_string(json_string):
        """
        Args:
            json_string : string representating a list of dicts.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)
