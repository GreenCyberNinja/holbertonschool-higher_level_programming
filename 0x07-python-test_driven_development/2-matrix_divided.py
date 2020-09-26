#!/usr/bin/python3
""" this function divides all elements of a matrix
    matrix """


def matrix_divided(matrix, div):
       """Args:
       matrix - matrix to be divided
       div - to dived matrix by"""

    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    ans = [[]]
    a = 0
    b = len(matrix[0])
    for i in matrix:
        if a != 0:
            ans.append([])
        if b != len(matrix[a]):
            raise TypeError("Each row of the matrix must have the same size")
        if type(matrix[a]) != list:
            raise TypeError("matrix must be a matrix (list of lists)
                  of integers/floats")
        for j in matrix[a]:
            if not isinstance(j, int):
                raise TypeError("matrix must be a matrix (list of lists)
                      of integers/floats")
            ans[a].append(round((j / div), 2))
        a += 1
    return ans
