#!/usr/bin/python3
"""this function prints first and last name"""


def say_my_name(first_name, last_name=""):
    """Args:
       first_name: should be type str
       last_name: should be type str
       prints both or first name"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {:s} {:s}".format(first_name, last_name))
