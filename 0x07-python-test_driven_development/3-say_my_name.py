#!/usr/bin/python3


"""3-say_my_name: module that prints out somones ones"""


def say_my_name(first_name, last_name=""):
    """Prints: My name is {first_name} {last_name}
    Args:
        first_name (str): first name
        last_name (str): last name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
