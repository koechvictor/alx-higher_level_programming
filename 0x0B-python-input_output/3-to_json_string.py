#!/usr/bin/python3
"""
Program that writes text to a file
"""


def write_file(filename="", text=""):
    """ write to a file and return # of characters written """
    if filename == "":
        return
    with open(filename, "w") as f:
        f.write(text)
    return len(text)
