#!/usr/bin/python3

"""MOdule that loads and returns an object from a file"""
import json


def load_from_json_file(filename):
    """Function that loads an object from a file and returns that object
    in an object format
    Args:
        filename (str): the file to load
    """
    with open(filename, encoding='utf-8') as f:
        return json.load(f)
