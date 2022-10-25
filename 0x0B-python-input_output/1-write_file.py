#!/usr/bin/python3
"""
a function that writes a string to a text file
and returns the number of characters written
"""


def write_file(filename="", text=""):
    """count lines in a file"""
    count = 0
    if filename == "":
        return count
    with open(filename, "r") as f:
        for line in f:
            count += 1
    return count
