#!/usr/bin/python3
"""
Unittest for base class
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ Test the  Base class """

    def setUp(self):
        """setting up test cases for base class"""
        Base._Base__nb_objects = 0
        # this is to keep each test case separated, and not affect
        # by the other id related tests

    def test_noneId(self):
        """ test when id arg= None"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_givenId(self):
        """ test when id arg != None"""
        b3 = Base(12)
        self.assertEqual(b3.id, 12)

    def test_noneAfterGivenId(self):
        """test both cases together"""
        b1 = Base()
        b2 = Base()
        b3 = Base(12)
        b4 = Base()
        self.assertEqual(b4.id, 3)

    def test_to_json(self):
        """Test to_json method"""
        dictionary = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        json_dictionary = Base.to_json_string([dictionary])
        excepted = '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'
        self.assertEqual(json_dictionary, excepted)
        self.assertEqual(type(json_dictionary), str)
        self.assertEqual(Base.to_json_string([]), '[]')
        self.assertEqual(Base.to_json_string(None), '[]')

    def test_from_json_string(self):
        """Testing from_json_string method"""
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Base.to_json_string(list_input)
        list_output = Base.from_json_string(json_list_input)
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(list_output, list_input)
        self.assertEqual(Base.from_json_string([]), [])

    def test_create(self):
        """Test create method on base class"""
        dic = {'id': 4}
        dic2 = {}
        b1 = Base.create(**dic)
        self.assertEqual(b1.id, 4)
        b2 = Base.create(**dic2)
        self.assertEqual(b2.id, 1)


if __name__ == "__main__":
    unittest.main()
