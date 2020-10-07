#!/usr/bin/python3
"""file for task 1"""


class MyList(list):
    """
    prints inherited list
    """
    def print_sorted(self):
        srtlst = self[:]
        print(sorted(srtlst))
