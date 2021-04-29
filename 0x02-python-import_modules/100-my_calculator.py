#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys


def use_new_calculator():
    parameters = sys.argv
    if len(parameters) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(parameters[1])
        b = int(parameters[3])
        operations = ["add", "sub", "mul", "div"]
        simbols = ["+", "-", "*", "/"]
        try:
            index_parameter = simbols.index(parameters[2])
        except ValueError:
            index_parameter = 4
        if index_parameter != 4:
            i = operations[index_parameter] + "({}, {})".format(a, b)
            print("{:d} {:s} {:d} = {:d}"
                  .format(a, simbols[index_parameter], b, eval(i)))
            exit(0)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
if __name__ == "__main__":
    use_new_calculator()
