#!/usr/bin/python3
"""
a function that reads a text file  and prints it to stdout
"""


def read_file(filename=""):
    """prints file contents"""
    if filename == "":
        return
    with open(filename, "r") as f:
        print(f.read(), end="")
