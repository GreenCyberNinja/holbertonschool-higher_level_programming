#!/usr/bin/python3
for x in range(0, 10):
    for y in range(x, 9):
        print('{:d}{:d}'.format(x, y + 1), end='')
        if x != 8 and y != 9:
            print(', ', end='')
print('')
