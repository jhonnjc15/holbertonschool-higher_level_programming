#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = list(str)
    if not(n > len(str) or n < 0):
        new_str.pop(n)
    return "".join(new_str)
