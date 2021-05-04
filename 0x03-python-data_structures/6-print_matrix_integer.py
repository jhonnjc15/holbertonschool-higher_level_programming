#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        if len(i) > 0:
            for j in i:
                if j == i[-1]:
                    end = "\n"
                else:
                    end = " "
                print("{:d}".format(j), end=end)
        else:
            print("", end="\n")
