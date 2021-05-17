#!/usr/bin/python3


def safe_print_division(a, b):
    try:
        divi = a / b
        return divi
    except ZeroDivisionError:
        divi = None
        return divi
    finally:
        print("Inside result: {}".format(divi))
