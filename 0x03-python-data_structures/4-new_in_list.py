#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cpy = my_list[:]
    if idx < 0:
        return (my_list)
    for i in range(len(cpy)):
        if i == idx:
            cpy[i] = element
            return (cpy)
    return (my_list)
