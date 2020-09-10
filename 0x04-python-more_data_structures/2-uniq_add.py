#!/bin/usr/python3
def uniq_add(my_list=[]):
    new = my_list[:]
    b = 0
    for i in new:
        a = new[i]
        if new.count(a) > 1:
            new.remove(new[i])
    return (sum(new))
