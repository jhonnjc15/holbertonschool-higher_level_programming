#!/usr/bin/python3

"""2-matrix_divid: module that divides all elements in a matrix by the div"""


def matrix_divided(matrix, div):
    """2-matrix_divid: module that divides all elements in a matrix
    by the div parameter, returns a new list matrix
    Args:
        matrix (list): 2d array of ints or floats
        div (int): divider to divide number
    Returns:
        list: matrix of a new list
    """
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    if all(isinstance(n, (int, float)) for r in matrix for n in r) is False:
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    if len(set([len(row) for row in matrix])) is not 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[float("{:.2f}".format(num/div)) for num in row] for row in matrix]
