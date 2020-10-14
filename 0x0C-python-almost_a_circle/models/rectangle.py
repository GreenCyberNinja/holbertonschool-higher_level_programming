#!/usr/bin/python3
""" class rectangle inherits from Base"""
from models.base import Base


class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        return self.width * self.height

    def display(self):
        for h in range((self.y + self.height)):
            for w in range((self.x + self.width)):
                if h < self.y:
                    pass
                elif w < self.x:
                    print(" ", end="")
                else:
                    print("#", end="")
            print()

    def update(self, *args, **kwargs):
        if len(args) > 0 :
            for arg in range(args):
                if arg == 0:
                    self.id = args[arg]
                if arg == 1:
                    self.width = args[arg]
                if arg == 2:
                    self.height = args[arg]
                if arg == 3:
                    self.x = args[arg]
                if arg == 4:
                    self.y = args[arg]
        else:
            for karg in kwargs:
                if karg == 'id':
                    self.id = kwargs['id']
                if karg == 'width':
                    self.width = kwargs['width']
                if karg =='height':
                    self.height = kwargs['height']
                if karg == 'x':
                    self.x = kwargs['x']
                if karg == 'y':
                    self.y = kwargs['y']


    def __str__(self):
        return("[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format

               (self.id, self.x, self.y, self.width, self.height))
    def to_dictionary(self):
        return self.__dict__

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y
