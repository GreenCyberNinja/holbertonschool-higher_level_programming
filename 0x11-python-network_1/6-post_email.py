#!/usr/bin/python3
"""posts an email"""

from sys import argv
import requests


if __name__ == "__main__":
    e = {'email': argv[2]}
    req = requests.post(argv[1], data=e)
    print(req.text)
