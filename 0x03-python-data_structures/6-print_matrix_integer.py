#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    J = len(matrix[0])
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print("{:d}".format(matrix[i][j]), end='')
            if j < J - 1:
                print(' ', end='')
        print('')
