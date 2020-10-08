#!/usr/bin/python3
"""file for task1"""


def number_of_lines(filename=""):
    """gets the number of lines in a file"""
    a = 0
    with open(filename, 'r') as f:
        for lines in f:
            a += 1
        return a
