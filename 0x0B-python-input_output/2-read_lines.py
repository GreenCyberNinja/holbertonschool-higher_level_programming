#!/usr/bin/python3
"""file for task2"""


def read_lines(filename="", nb_lines=0):
    """reads a certain number of lines"""
    a = 0
    with open(filename, 'r') as f:
        if nb_lines <= 0:
            for lines in f:
                print(lines, end="")
        else:
            for lines in f:
                if a < nb_lines:
                    print(lines, end="")
                    a += 1
