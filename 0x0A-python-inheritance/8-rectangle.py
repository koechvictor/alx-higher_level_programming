#!/usr/bin/python3
"""
class Rectangle that inherits BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ class Rectangle"""
    def __init__(self, width, height):
        """ initialize """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
