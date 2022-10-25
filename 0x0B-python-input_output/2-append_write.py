#!/usr/bin/python3
"""
Program that counts lines in a file
"""


def read_lines(filename="", nb_lines=0):
    """ count lines in file """
    if filename == "":
        return
    if nb_lines <= 0:
        with open(filename, "r") as f:
            print(f.read(), end="")
    else:
        with open(filename, "r") as f:
            head = [next(f) for x in range(nb_lines)]
        print("".join(head), end="")
