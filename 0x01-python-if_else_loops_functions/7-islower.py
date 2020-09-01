#!/usr/bin/python3
def islower(c):
    ac = ord(c)
    for i in range(97, 123):
        if ac == i:
            return(True)
    return(False)
