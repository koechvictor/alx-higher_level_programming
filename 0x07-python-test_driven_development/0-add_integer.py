#!/usr/bin/python3
"""

Function that adds 2 integers

"""
def add_integer(a, b=98):
    """
    These comments are stupid
    """
    if not (type(a) is float or type(a) is int):
        raise TypeError("a must be an integer")
    elif not (type(b) is float or type(b) is int):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
