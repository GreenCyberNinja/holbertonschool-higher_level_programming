#!/usr/bin/python3
"""file for task0"""


def read_file(filename=""):
    """reads file"""
    with open(filename, 'r') as f:
        for line in f:
            print(line, end="")
