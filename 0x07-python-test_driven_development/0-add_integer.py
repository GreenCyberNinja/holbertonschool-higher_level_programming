#!/usr/bin/python3
"""this function takes int(a) and adds it to int(b)
   converts float to int and raise type error if not float or int 
   Example
   >>> add_integer(2, 2)
   4 """
def add_integer(a, b=98):
    """Args:
    a - int or float
    b - 98 unless input(int or float)"""
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    elif not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')

    else:
        return int(a + b)
