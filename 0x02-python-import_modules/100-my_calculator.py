#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def use_new_calculator():
    parameters = sys.argv
    if len(parameters) != 4:
        print("Usage: {} <a> <operator> <b>".format(parameters[0]))
        sys.exit(1)
    else:
        a = int(parameters[1])
        b = int(parameters[3])

        operations = ["add", "sub", "mul", "div"]
        simbols = ["+", "-", "*", "/"]

        for k, j in zip(simbols, range(len(simbols))):
            if k == parameters[2]:
                i = operations[j] + "({}, {})".format(a, b)
                print("{:d} {:s} {:d} = {:d}"
                      .format(a, simbols[j], b, eval(i)))
                exit(0)
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

if __name__ == "__main__":
    import sys
    use_new_calculator()
