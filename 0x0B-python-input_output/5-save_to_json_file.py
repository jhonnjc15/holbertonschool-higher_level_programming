#!/usr/bin/python3

"""Module that saves a json file"""
import json


def save_to_json_file(my_obj, filename):
    """Function to save a json files
    Args:
        my_obj: object to save to file
        filename (str): file to write the my_obj to
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f)
