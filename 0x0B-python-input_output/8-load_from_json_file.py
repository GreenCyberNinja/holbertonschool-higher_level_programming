#!/usr/bin/python3
"""file for task8"""
import json


def load_from_json_file(filename):
    """creates object from json"""
    with open(filename, 'r') as f:
        return json.load(f)
