#!/usr/bin/python3
"""handles errors and post a letter"""


import requests
from sys import argv
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    req = requests.get('https://api.github.com/user',
                       auth=HTTPBasicAuth(argv[1], argv[2]))
    print(req.json().get('id'))
