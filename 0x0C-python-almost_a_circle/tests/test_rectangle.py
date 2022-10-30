#!/usr/bin/python3
""" Tests for class Rectangle """
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import pep8


class TestRectangle(unittest.TestCase):
    """ tests for class Rectangle """

    def test_rec_init(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 5)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 6)
        r3 = Rectangle(10, 2, 0, 0, 15)
        self.assertEqual(r3.id, 15)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 3, 4, 5, 5)

    def test_pep8(self):
        """ tests prp8 formating """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style erros (and warnings).")
