#!/usr/bin/python3
"""reads n lines of a text file"""


def read_lines(filename="", nb_lines=0):
    """reads n lines of a text file"""
    count = 0
    with open(filename, encoding="utf-8") as f:
        if nb_lines <= 0:
            print(f.read(), end="")
        for l in f:
            count += 1
            if count > nb_lines:
                break
            print(line, end="")
