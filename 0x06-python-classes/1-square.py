#!/usr/bin/python3
class Square:
    """python3 -c 'print(__import__("my_module").my_function.__doc__)"""
    """ python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)"""
    def __init__(self, size):
        self._size = size
