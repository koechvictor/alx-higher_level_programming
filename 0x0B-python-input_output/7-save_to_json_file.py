#!/usr/bin/python3
"""
save json to a text file
"""
import json


def save_to_json_file(my_obj, filename):
    """ prints file contents """
    if filename == "":
        return
    with open(filename, "w") as f:
        json.dump(my_obj, f)
