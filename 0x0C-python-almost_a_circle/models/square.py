#!/usr/bin/python3
""" file for square"""
from models.rectangle import Rectangle

class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        Rectangle.__init__(self, size, size, x, y, id)

    def __str__(self)
