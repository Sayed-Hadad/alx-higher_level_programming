#!/usr/bin/python3
"""
This module is a part of Alx python inheritance tasks.
It contains a class "MyList" that inherits the list class,
and a public method called print_sorted()
"""


class MyList(list):
    """
    This class inherits the list class in python.
    It contains a public method called print_sorted.
    creating an object of it:
    my_list = MyList()
    """
    def print_sorted(self):
        """
        This method prints the list in an ascending order,
        without affecting the original list.
        """
        print(sorted(self))
