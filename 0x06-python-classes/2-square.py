#!/usr/bin/python3
"""This program is to establish square and its size is only a positive int"""


class Square:
    """establish object Square"""
    def __init__(self, size=0):
        """initiat size as private attribute only if positive int"""
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
