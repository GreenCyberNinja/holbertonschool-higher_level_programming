#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    for i in sorted(a_dictionary.items(), key=lambda x: x[1], reverse=True):
        return (i[0])
