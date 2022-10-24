#!/usr/bin/python3
"""
Function that returns True if the object is an instance of, or if the object
is instance of a class that inherited from, the specified class
"""


def is_kind_of_class(obj, a_class):
    """ returns True if the object is an instance of or inst. of inh."""
    return isinstance(obj, a_class)
