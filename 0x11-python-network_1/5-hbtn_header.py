#!/usr/bin/python3
"""takes input url and displays the x-request-Id"""


import requests
from sys import argv

if __name__ == "__main__":
    req = requests.get(argv[1])
    print(req.headers.get('X-Request-Id'))
