#!/usr/bin/python3
import json

"""Module that returns the JSON representation of an object."""


def to_json_string(my_obj):
    """
        Function that returns the JSON representation of an object.
        Args:
            my_obj: object to serialize
    """
    return json.dumps(my_obj)
