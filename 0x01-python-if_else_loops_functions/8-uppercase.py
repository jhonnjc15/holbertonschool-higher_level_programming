#!/usr/bin/python3
def uppercase(str):
    new_str = list(str)
    for i in range(len(str)):
        if (ord(str[i]) >= 97 and ord(str[i]) <= 122):
            new_str[i] = chr(ord(str[i]) - 32)
    print("{:s}".format("".join(new_str)))
