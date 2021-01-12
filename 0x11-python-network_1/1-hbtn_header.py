#!/usr/bin/python3
"""takes input url and displays the x-request-Id"""


import urllib.request
from sys import argv

if __name__ == "__main__":
    req = urllib.request.Request(argv[1])
    with urllib.request.urlopen(req) as stuf:
        print(stuf.getheader('X-Request-id'))
