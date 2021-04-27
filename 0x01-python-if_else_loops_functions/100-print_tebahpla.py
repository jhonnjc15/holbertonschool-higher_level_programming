#!/usr/bin/python3
for i in range(122, 96, -1):
    if (i % 2 == 0):
        n = 0
    else:
        n = 32
    print("{:s}".format(chr(i - n)), end='')
