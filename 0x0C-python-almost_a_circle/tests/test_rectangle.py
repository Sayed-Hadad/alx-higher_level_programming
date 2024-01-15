#!/usr/bin/python3
"""
Unittest for Rectangle class
"""
import unittest
from unittest import mock
from models.rectangle import Rectangle
import json
import os


class TestRectangle(unittest.TestCase):
    """Testing Rectangle Class"""

    def setUp(self):
        """setup to do before the start of each test"""
        Rectangle._Base__nb_objects = 0
        # this is to keep each test case separated, and not affect
        # by the other id related tests

    def test_ids(self):
        """Testing rectangle objects ids"""
        r1 = Rectangle(5, 3)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)

    def test_normal(self):
        """Test valid widht, height, x, y"""
        r1 = Rectangle(5, 3, 2, 1)
        self.assertEqual(r1.width, 5)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 1)

    def test_invalid_width(self):
        """Test invalid width exceptions"""
        with self.assertRaises(ValueError):
            Rectangle(-2, 1)
            Rectangle(0, 1)
        with self.assertRaises(TypeError):
            Rectangle('width', 1, 2, 3)
            Rectangle(True, 1, 2, 3)
            Rectangle(3.14, 1, 2, 3)
            Rectangle([1], 2, 3, 4)

    def test_invalid_height(self):
        """Test invalid height exceptions"""
        with self.assertRaises(ValueError):
            Rectangle(2, -1)
            Rectangle(2, 0)
        with self.assertRaises(TypeError):
            Rectangle(1, 'height', 2, 3)
            Rectangle(1, True, 2, 3)
            Rectangle(1, 3.14, 2, 3)
            Rectangle(1, [2], 3, 4)

    def test_invalid_x(self):
        """Test invalid x exceptions"""
        with self.assertRaises(ValueError):
            Rectangle(2, 1, -2, 3)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 'x', 3)
            Rectangle(1, 2, True, 3)
            Rectangle(1, 2, 3.14, 3)
            Rectangle(1, 2, [3], 4)

    def test_invalid_y(self):
        """Test invalid y exceptions"""
        with self.assertRaises(ValueError):
            Rectangle(2, 1, 2, -3)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, True)
            Rectangle(1, 2, 3, 'y')
            Rectangle(1, 2, 3, 3.14)
            Rectangle(2, 3, 4, [5])

    def test_set_width_height(self):
        """Test setting size with valid values"""
        r1 = Rectangle(4, 6)
        r1.width = 10
        r1.height = 2
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)

    def test_set_valid_x_y(self):
        """Test setting x and y with valid values"""
        r1 = Rectangle(5, 7)
        r1.x = 2
        r1.y = 3
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 3)

    def test_set_invalid_width_height(self):
        """Testing setting invalid values for width and height"""
        r1 = Rectangle(4, 6)
        with self.assertRaises(ValueError):
            r1.width = -2
            r1.width = 0
            r1.height = -2
            r1.height = 0
        with self.assertRaises(TypeError):
            r1.width = True
            r1.widht = 3.14
            r1.width = 's'
            r1.height = True
            r1.height = 3.14
            r1.height = 's'

    def test_set_invalid_x_y(self):
        """Testing setting x and y with invalid values"""
        r1 = Rectangle(4, 6)
        with self.assertRaises(ValueError):
            r1.x = -2
            r1.y = -2
        with self.assertRaises(TypeError):
            r1.x = True
            r1.x = 3.14
            r1.x = 's'
            r1.y = True
            r1.y = 3.14
            r1.y = 's'

    def test_display(self):
        """Test the display method"""
        with mock.patch('builtins.print') as mock_print:
            r1 = Rectangle(4, 6)
            expected = '####\n####\n####\n####\n####\n####\n'
            r1.display()
            output = mock_print.call_args_list
            output_str = ''.join([call[0][0] + '\n' for call in output])
            self.assertEqual(output_str, expected)

        with mock.patch('builtins.print') as mock_print:
            r2 = Rectangle(2, 3, 2, 2)
            r2.display()
            output = mock_print.call_args_list
            output_str = ''.join([call[0][0] + '\n' for call in output])
            expected = '\n\n  ##\n  ##\n  ##\n'
            self.assertEqual(output_str, expected)

    def test_str(self):
        """Test __str__method"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        expected = '[Rectangle] (12) 2/1 - 4/6'
        self.assertEqual(str(r1), expected)
        r2 = Rectangle(5, 5, 1)
        expected = '[Rectangle] (1) 1/0 - 5/5'
        self.assertEqual(str(r2), expected)

    def test_update(self):
        """Test update method"""
        r1 = Rectangle(10, 10, 10, 10)
        # test args first
        r1.update(89)
        str_rect = '[Rectangle] (89) 10/10 - 10/10'
        self.assertEqual(str(r1), str_rect)
        r1.update(90, 2)
        str_rect = '[Rectangle] (90) 10/10 - 2/10'
        self.assertEqual(str(r1), str_rect)
        r1.update(89, 2, 3, 4, 5)
        str_rect = '[Rectangle] (89) 4/5 - 2/3'
        self.assertEqual(str(r1), str_rect)
        # test kwargs
        r1.update(height=1)
        str_rect = '[Rectangle] (89) 4/5 - 2/1'
        self.assertEqual(str(r1), str_rect)
        r1.update(id=1, x=1, height=2, y=3, width=4)
        str_rect = '[Rectangle] (1) 1/3 - 4/2'
        self.assertEqual(str(r1), str_rect)
        # test both together, (ignore kwargs)
        r1.update(2, height=2)
        str_rect = '[Rectangle] (2) 1/3 - 4/2'
        self.assertEqual(str(r1), str_rect)
        r1.update(1, 2, width=5)
        str_rect = '[Rectangle] (1) 1/3 - 2/2'
        self.assertEqual(str(r1), str_rect)

    def test_to_dic(self):
        """Test the to_dictionary method"""
        r1 = Rectangle(10, 2, 1, 9)
        expected = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertEqual(r1.to_dictionary(), expected)
        r2 = Rectangle(1, 1)
        r2.update(**expected)
        expected = '[Rectangle] (1) 1/9 - 10/2'
        self.assertEqual(str(r2), expected)

    def test_save_to_file(self):
        """Testing save_to_file method for rectangle class"""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            out = json.load(f)
        self.assertEqual(out, [])
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            out = json.load(f)
        self.assertEqual(out, [])
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            out = json.load(f)
        expected = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertEqual(out, expected)

    def test_create(self):
        """Testing create method on rectangle class"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        expected = '[Rectangle] (1) 1/0 - 3/5'
        self.assertEqual(str(r2), expected)

    def test_load_from_file(self):
        """Testing load_from_file method from rectangle objects"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        if os.path.exists('Rectangle.json'):
            os.remove('Rectangle.json')
        self.assertEqual(Rectangle.load_from_file(), [])
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        expected = '[Rectangle] (1) 2/8 - 10/7'
        self.assertEqual(str(list_rectangles_output[0]), expected)
        expected = '[Rectangle] (2) 0/0 - 2/4'
        self.assertEqual(str(list_rectangles_output[1]), expected)


if __name__ == "__main__":
    unittest.main()
