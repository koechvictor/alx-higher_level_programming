#!/usr/bin/python3
"""
save json to a text file
"""
import json


def load_from_json_file(filename):
    """ prints file contents """
    if filename == "":
        return
    with open(filename, "r") as f:
        return json.load(f)
