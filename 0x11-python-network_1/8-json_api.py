#!/usr/bin/python3
"""handles errors and post a letter"""


import requests
from sys import argv


if __name__ == "__main__":
    r = ""
    if len(argv) >=2:
        r = argv[1]
    req = requests.post('http://0.0.0.0:5000/search_user', data={'q': r})
    try:
        d = req.json()
	if d:
            print("[{}] {}".format(d.get('id'),d.get('name')))
        else:
            print("No result")
    except ValueError as err:
            print("Not a valid JSON")
