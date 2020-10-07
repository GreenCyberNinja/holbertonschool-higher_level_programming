#!/usr/bin/python3
"""file for task 4"""


def inherits_from(obj, a_class):
    """
    checks if the object is an instance class inherited
    """
    return type(obj) != a_class and issubclass(type(obj), a_class)
