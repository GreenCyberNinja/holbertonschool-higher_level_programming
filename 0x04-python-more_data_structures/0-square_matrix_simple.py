#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = [[]]
    a = 0
    for i in matrix:
        if a != 0:
            new.append([])
        for j in matrix[a]:
            new[a].append(j * j)
        a += 1
    return new
