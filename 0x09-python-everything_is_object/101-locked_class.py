#!/usr/bin/python3
"""class LockedClass"""


class LockedClass:
    """a locked class that prevents the user from creating
    attributes unless its first_name
    """

    __slots__ = "first_name"

    def __init__(self):
        """ initiates instance"""
        self.first_name = any
