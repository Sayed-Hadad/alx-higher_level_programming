#!/usr/bin/python3
"""
Unittest for Sqaure class
"""
import unittest
from unittest import mock
from models.square import Square
import json
import os


class TestSquare(unittest.TestCase):
    """Testing the Square class"""

    def setUp(self):
        """setup to do before the start of each test"""
        Square._Base__nb_objects = 0
        # this is to keep each test case separated, and not affect
        # by the other id related tests

    def test_ids(self):
        """Testing ids for square objects"""
        s1 = Square(5)
        s2 = Square(7)
        s3 = Square(5, 0, 0, 12)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s2.id, 2)
        self.assertEqual(s3.id, 12)

    def test_initialize(self):
        """Test valid size, x, y, id"""
        s1 = Square(5, 3, 2)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 2)

    def test_invalid_size(self):
        """Test invalid size exceptions"""
        with self.assertRaises(ValueError):
            Square(-2)
            Square(0)
        with self.assertRaises(TypeError):
            Square('1', 2, 3)
            Square(True, 2, 3)
            Square(3.14, 2, 3)
            Square([2], 3, 4)

    def test_invalid_x(self):
        """Test invalid x exceptions"""
        with self.assertRaises(ValueError):
            Square(1, -2, 3)
        with self.assertRaises(TypeError):
            Square(2, 'x', 3)
            Square(2, True, 3)
            Square(2, 3.14, 3)
            Square(2, [3], 4)

    def test_invalid_y(self):
        """Test invalid y exceptions"""
        with self.assertRaises(ValueError):
            Square(1, 2, -3)
        with self.assertRaises(TypeError):
            Square(2, 3, True)
            Square(2, 3, 'y')
            Square(2, 3, 3.14)
            Square(3, 4, [5])

    def test_set_size(self):
        """Test setting size with valid values"""
        s1 = Square(5)
        s1.size = 10
        self.assertEqual(s1.size, 10)

    def test_set_x_y(self):
        """Test setting x and y with valid values"""
        s1 = Square(5)
        s1.x = 2
        s1.y = 3
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 3)

    def test_str(self):
        """Test __str__method"""
        s1 = Square(6, 2, 1, 12)
        expected = '[Square] (12) 2/1 - 6'
        self.assertEqual(str(s1), expected)
        s2 = Square(5, 1)
        expected = '[Square] (1) 1/0 - 5'
        self.assertEqual(str(s2), expected)

    def test_update(self):
        """Test the update method in Square class"""
        s1 = Square(5)
        s1.update(10)
        expected = '[Square] (10) 0/0 - 5'
        self.assertEqual(str(s1), expected)
        s1.update(1, 2)
        expected = '[Square] (1) 0/0 - 2'
        self.assertEqual(str(s1), expected)
        s1.update(1, 2, 3)
        expected = '[Square] (1) 3/0 - 2'
        self.assertEqual(str(s1), expected)
        s1.update(1, 2, 3, 4)
        expected = '[Square] (1) 3/4 - 2'
        self.assertEqual(str(s1), expected)
        s1.update(x=12)
        expected = '[Square] (1) 12/4 - 2'
        self.assertEqual(str(s1), expected)
        s1.update(size=7, y=1)
        expected = '[Square] (1) 12/1 - 7'
        self.assertEqual(str(s1), expected)
        s1.update(89, size=7, y=1)
        expected = '[Square] (89) 12/1 - 7'
        self.assertEqual(str(s1), expected)

    def test_to_dic(self):
        """Test the to_dictionary method"""
        s1 = Square(10, 2, 1)
        expected = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertEqual(s1.to_dictionary(), expected)
        s2 = Square(1, 1)
        s2.update(**expected)
        expected = '[Square] (1) 2/1 - 10'
        self.assertEqual(str(s2), expected)

    def test_save_to_file(self):
        """Testing save_to_file method for Square class"""
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            out = json.load(f)
        self.assertEqual(out, [])
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            out = json.load(f)
        self.assertEqual(out, [])
        s1 = Square(10, 2, 8)
        s2 = Square(2)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as f:
            out = json.load(f)
        expected = [s1.to_dictionary(), s2.to_dictionary()]
        self.assertEqual(out, expected)

    def test_create(self):
        """Testing create method on Square class"""
        s1 = Square(3, 5)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        expected = '[Square] (1) 5/0 - 3'
        self.assertEqual(str(s2), expected)

    def test_load_from_file(self):
        """Testing load_from_file method from Square objects"""
        s1 = Square(10, 2, 8)
        s2 = Square(2)
        if os.path.exists('Square.json'):
            os.remove('Square.json')
        self.assertEqual(Square.load_from_file(), [])
        list_Squares_input = [s1, s2]
        Square.save_to_file(list_Squares_input)
        list_Squares_output = Square.load_from_file()
        expected = '[Square] (1) 2/8 - 10'
        self.assertEqual(str(list_Squares_output[0]), expected)
        expected = '[Square] (2) 0/0 - 2'
        self.assertEqual(str(list_Squares_output[1]), expected)
