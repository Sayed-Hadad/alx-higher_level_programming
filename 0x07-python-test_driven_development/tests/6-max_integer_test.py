#!/usr/bin/python3
import unittest
"""Unittest for max_integer([..])
"""
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Test the max_integer function """
    def test_sorted_case(self):
        ls = [1, 2, 3, 4]
        test = max_integer(ls)
        self.assertEqual(test, 4)

    def test_reverse_sorted(self):
        ls = [4, 3, 2, 1]
        test = max_integer(ls)
        self.assertEqual(test, 4)

    def test_random_order(self):
        ls = [1, 3, 4, 2]
        test = max_integer(ls)
        self.assertEqual(test, 4)

    def test_all_negative(self):
        ls = [-5, -6, -7, -10]
        test = max_integer(ls)
        self.assertEqual(test, -5)

    def test_empty_list(self):
        test = max_integer([])
        self.assertEqual(test, None)

    def test_one_element(self):
        test = max_integer([7])
        self.assertEqual(test, 7)

    def test_duplicates(self):
        ls = [0, 0, 1, 5, 10, 10]
        test = max_integer(ls)
        self.assertEqual(test, 10)


if __name__ == "__main__":
    unittest.main()
