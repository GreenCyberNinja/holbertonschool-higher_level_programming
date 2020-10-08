#!/usr/bin/python3
"""file for task9"""
import sys
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file


filename = "add_item.json"
try:
    ans = load_from_json_file(filename)
    ans.extend(sys.argv[1:])
    save_to_json_file(ans, filename)
except FileNotFoundError:
    ans = sys.argv[1:]
    save_to_json_file(ans, filename)
