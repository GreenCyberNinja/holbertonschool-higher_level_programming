#!/usr/bin/python3
"""file for task4"""


def append_write(filename="", text=""):
    """appends file"""
    with open(filename, 'a+') as f:
        f.write(text)
    return len(text)
