#!/usr/bin/python3
""" file for square"""
from models.rectangle import Rectangle
import json
class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        return("[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x, self.y, self.height))

    def to_dictionary(self):
        return self.__dict__
   
    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
         self.width = size
         self.height = size

    def update(self, *args, **kwargs):
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
           if 'id' in kwargs:
                self.id = kwargs['id']
           if 'size' in kwargs:
                self.size = kwargs['size']
           if 'x' in kwargs:
                self.x = kwargs['x']
           if 'y' in kwargs:
                self.y = kwargs['y']
