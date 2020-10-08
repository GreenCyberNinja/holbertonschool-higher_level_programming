#!/usr/bin/python3
"""file for task11"""


class Student:
    """
    class student
    atributes: first name, last name, age
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
