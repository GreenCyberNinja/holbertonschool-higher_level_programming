#!/usr/bin/python3
"""file for task7"""
import json


def save_to_json_file(my_obj, filename):
    """writes json file"""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
