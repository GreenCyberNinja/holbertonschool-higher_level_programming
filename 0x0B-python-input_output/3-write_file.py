#!/usr/bin/python3
"""file for task3"""


def write_file(filename="", text=""):
    """writes to a file"""
    with open(filename, 'w') as f:
        f.write(text)
    return(len(text))
