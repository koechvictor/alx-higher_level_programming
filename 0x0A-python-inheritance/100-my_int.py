#!/usr/bin/python3
""" class MyInt that inherits from int """


class MyInt(int):

    def __eq__(self, other):
        """ equals change to not equals """
        return super().__ne__(other)

    def __ne__(self, other):
        """ not equals to equals """
        return super().__eq__(other)
