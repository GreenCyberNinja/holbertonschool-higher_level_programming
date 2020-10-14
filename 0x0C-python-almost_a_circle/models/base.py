#!/usr/bin/python3
""" file for base"""
import json


class Base:
    """base for other objects"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initializes"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """converts to json string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return("[]")
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves json to file"""
        d = []
        for i in list_objs:
            d.append(i.to_dictionary())
        with open(cls.__name__ + ".json", 'w') as f:
            f.write(cls.to_json_string(d))

    @staticmethod
    def from_json_string(json_string):
        """creates list from json string"""
        if json_string is none or len(json_string) == 0:
            return ("[]")
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """creates an instance of class"""
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy
