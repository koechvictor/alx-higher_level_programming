#!/usr/bin/python3
def best_score(a_dictionary={}):
    if a_dictionary is None:
        return
    for key, value in a_dictionary.items():
        if value == max(a_dictionary.values()):
            return key
