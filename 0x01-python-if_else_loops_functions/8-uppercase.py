#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        b = ord(str[i])
        if b >= 97 and b <= 122:
            b -= 32
        print('{:s}'.format(chr(b)), end='')
    print('')
