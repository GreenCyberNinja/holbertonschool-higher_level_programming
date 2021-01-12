#!/usr/bin/python3
"""posts an email"""

from sys import argv
import urllib.parse
import urllib.request


if __name__ == "__main__":
    em = urllib.parse.urlencode({'email': argv[2]})
    em = em.encode('ascii')
    req = urllib.request.Request(argv[1], em)
    with urllib.request.urlopen(req) as stuf:
        print(stuf.read().decode('utf'))
