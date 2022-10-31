#!/usr/bin/python3
""" class square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class for Square that inherits from rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """ initialize """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        returns size value
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        sets size value
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ update square """
        argCount = len(args)
        if argCount == 0:
            if "id" in kwargs.keys():
                self.id = kwargs["id"]
            if "size" in kwargs.keys():
                self.size = kwargs["size"]
            if "x" in kwargs.keys():
                self.x = kwargs["x"]
            if "y" in kwargs.keys():
                self.y = kwargs["y"]
        if argCount > 0:
            self.id = args[0]
        if argCount > 1:
            self.size = args[1]
        if argCount > 2:
            self.x = args[2]
        if argCount > 3:
            self.y = args[3]

    def __str__(self):
        """ string representation of class """
        string = "[{:s}] ({:d})".format(type(self).__name__, self.id)
        string += " {:d}/{:d} ".format(self.x, self.y)
        string += "- {:d}".format(self.size)
        return string

    def to_dictionary(self):
        """ to dictionary """
        dict_rec = {"x": self.x, "y": self.y, "id": self.id}
        dict_rec["size"] = self.size
        return dict_rec
