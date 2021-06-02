#!/usr/bin/python3
import sys

"""Script that adds all arguments to a Python list, and save them to a file"""


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


def main(argv):
    """that adds all arguments to a Python list, and save them to a file
    Args:
        argv (list) : list of the arguments for the command line
    """
    filename = "add_item.json"
    try:
        new_list = load_from_json_file(filename) + argv[1:]
    except Exception:
        new_list = argv[1:]

    save_to_json_file(new_list, filename)

main(sys.argv)
