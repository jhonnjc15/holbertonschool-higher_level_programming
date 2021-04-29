#!/usr/bin/python3
import sys


def prints_num_arg(): 
    arguments = sys.argv
    num_arg = len(arguments) - 1
    str_argumen = "argument"
    if num_arg != 1:
        str_argumen = str_argumen + "s"
    if num_arg != 0:
        last_character = ":"
    else:
        last_character = "."
    print("{:d} {:s}{:s}".format(num_arg, str_argumen, last_character))
    for i in range(1, num_arg + 1):
        print("{:d}: {:s}".format(i, arguments[i]))
if __name__ == "__main__":
    prints_num_arg()
