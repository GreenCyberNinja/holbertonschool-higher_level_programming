#!/usr/bin/python3
def max_integer(my_list=[]):
    m = 0
    if len(my_list) == 0:
        return (None)
    for i in range(len(my_list)):
        if m < my_list[i]:
            m = my_list[i]
    return (m)
