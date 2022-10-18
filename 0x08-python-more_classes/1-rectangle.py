#!/usr/bin/python3
"""
Class Rectangle that defines a rectangle
"""


class Rectangle:
    """
    Create Rectangle class
    """
    def __init__(self, width=0, height=0):
        """
        Initialize variables
        """
        self.width = width
        self.height = height

    @property
    """
    returns width value
    """
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets width value
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

    @property
    def height(self):
        """
        returns height value
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets width value
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
