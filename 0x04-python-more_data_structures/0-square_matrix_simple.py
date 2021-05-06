#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        elements = []
        for j in i:
            elements.append(j * j)
        new_matrix.append(elements)
    return new_matrix
