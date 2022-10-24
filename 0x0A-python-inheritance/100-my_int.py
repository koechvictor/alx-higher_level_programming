#!/usr/bin/python3
"""MyInt class"""


class MyInt(int):
    """MyInt class"""

    def __eq__(self, value):
        return self.real != value

    def __ne__(self, value):
        return self.real == value
