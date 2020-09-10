#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = list(set(my_list))
    b = 0
    for i in new:
        b += i
    return (b)
