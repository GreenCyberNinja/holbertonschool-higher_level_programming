#!/usr/bin/python3
"""program to create object Square"""


class Square:
    """establish object Square"""
    def __init__(self, size=0):
        """initiates size as private attribute only if positive int"""
        self.size = size

    @property
    def size(self):
        """getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the area"""
        return self.size * self.size
