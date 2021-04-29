#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def use_calculator():
    a = 10
    b = 5
    operations = ["add", "sub", "mul", "div"]
    simbols = ["+", "-", "*", "/"]
    for i, j in zip(operations, simbols):
        i = i + "({}, {})".format(a, b)
        print("{:d} {:s} {:d} = {:d}".format(a, j, b, eval(i)))
if __name__ == "__main__":
    use_calculator()
