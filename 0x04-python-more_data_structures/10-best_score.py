#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    for x, i in reversed(sorted(a_dictionary.items())):
        return (x[0:])
