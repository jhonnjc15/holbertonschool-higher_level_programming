#!/usr/bin/python3
import hidden_4


def print_names():
    all_names = dir(hidden_4)
    for name in all_names:
        if name[0] != '_':
            print("{}".format(name))

if __name__ == '__main__':
    print_names()
