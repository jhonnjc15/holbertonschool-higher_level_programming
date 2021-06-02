#!/usr/bin/python3

"""1-my_list.py: Write a class MyList that inherits from list"""


class MyList(list):
    """
    MyList
    Args:
        list (list): inherits from the class list.
    """
    def print_sorted(self):
        """
        Prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
