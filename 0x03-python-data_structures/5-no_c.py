#!/usr/bin/python3
def no_c(my_string):
    new_str = my_string[:]
    c = 0
    a = len(my_string)
    for i in range(a):
        b = ord(my_string[i])
        c += 1
        if b == 67 or b == 99:
            c -= 1
            new_str = new_str[:c] + new_str[c + 1:]
    return new_str
