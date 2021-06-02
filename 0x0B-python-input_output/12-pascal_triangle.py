#!/usr/bin/python3

"""Module that list of lists of integers
    representing the Pascal’s triangle
"""


def pascal_triangle(n):
    pascal_list = [[1]]
    if n <= 0:
        return pascal_triangle
    else:
        for i in range(1, n):
            row_list = []
            for j in range(i + 1):
                try:
                    if j - 1 >= 0:
                        row_list.append(pascal_list[i - 1][j] +
                                        pascal_list[i - 1][j - 1])
                    else:
                        raise IndexError()
                except IndexError:
                    if j == 0:
                        row_list.append(pascal_list[i-1][j] + 0)
                    else:
                        row_list.append(0 + pascal_list[i-1][j-1])
            pascal_list.append(row_list)
    return pascal_list
