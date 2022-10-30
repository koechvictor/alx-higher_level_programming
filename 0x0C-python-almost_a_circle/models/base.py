#!/usr/bin/python3
""" Base class """
import json
import turtle


class Base:
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            type(self).__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

 @staticmethod
    def to_json_string(list_dictionaries):
        """ converts dict to json """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
