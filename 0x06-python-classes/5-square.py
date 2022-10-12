#!/usr/bin/python3
"""a class Square that defines a square """


class Square:
    """based on 4-square.py"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        printSize = self.__size
        if printSize == 0:
            print()
        for i in range(printSize):
            for j in range(printSize):
                print("#", end="")
            print()
