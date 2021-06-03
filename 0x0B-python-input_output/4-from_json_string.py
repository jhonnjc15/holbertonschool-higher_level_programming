#!/usr/bin/python3

"""Modue that returns an object represented by a JSON string"""
import json


def from_json_string(my_str):
    """
        Function that returns an object represented by a JSON string
        Args:
            my_str: string to convert
    """
    return json.loads(my_str)
