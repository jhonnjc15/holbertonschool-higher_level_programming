#!/usr/bin/python3


"""Base module"""
import json
import csv


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

    @classmethod
    def create(cls, **dictionary):
        """
        Return a new instance with all arguments
        Args:
            **dictionary : dictionary with all the arguments
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances
        Args:
            cls (class): a class
        """
        filename = cls.__name__ + '.json'
        instances_list = []
        try:
            with open(filename, mode='r', encoding='utf-8') as f:
                json_string = f.read()
                new_lists = cls.from_json_string(json_string)
                for dictionary in new_lists:
                    instances_list.append(cls.create(**dictionary))
            return instances_list
        except BaseException:
            return instances_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serialize a list from a class instance in csv"""
        filename = cls.__name__ + '.csv'
        objs = [cls.to_dictionary(obj) for obj in list_objs]
        try:
            with open(filename, mode='w', encoding='utf-8') as f:
                if cls.__name__ == "Rectangle":
                    fieldnames = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == "Square":
                    fieldnames = ['id', 'size', 'x', 'y']
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                for obj in objs:
                    writer.writerow(obj)
        except BaseException:
            return "[]"

    @classmethod
    def load_from_file_csv(cls):
        """deserialize a list from a class instance in csv """
        filename = cls.__name__ + '.csv'
        da_list = []
        try:
            with open(filename, mode='r') as f:
                reader = csv.DictReader(f)
                for obj in reader:
                    for key, value in obj.items():
                        obj[key] = int(value)
                    da_list.append(obj)
            return [cls.create(**num_objs) for num_objs in da_list]
        except BaseException:
            return da_list
