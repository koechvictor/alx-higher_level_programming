#!/usr/bin/python3
"""Module for add_atribute method"""


def add_attribute(obj, att, val):
    """Module for add_atribute method"""
    if hasattr(obj, '__dict__') is True:
        setattr(obj, att, val)
    else:
        raise TypeError("can't add new attribute")
