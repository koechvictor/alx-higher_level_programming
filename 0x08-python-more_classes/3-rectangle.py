#!/usr/bin/python3
"""

Class Rectangle that defines a rectangle based on 2-rectangle.py

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
    def width(self):
        """
        returns width value
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets width value
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

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
        self.__height = value

    def area(self):
        """
        method to get area
        """
        return self.width * self.height

    def perimeter(self):
        """
        method to get perimeter
        """
        if self.width == 0 or self.height == 0:
            return 0
        return self.width * 2 + self.height * 2

    def __str__(self):
        """
        print rectangle using #
        """
        string = ""
        if self.width == 0 or self.height == 0:
            string += "\n"
            return ""
        else:
            for i in range(self.height):
                string += "#" * self.width
                if i < self.height - 1:
                    string += "\n"
            return string
