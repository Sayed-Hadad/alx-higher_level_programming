#!/usr/bin/python3
"""
This module is a part of alx python inheritance tasks.
it contains only a function called: is_same_class(obj, a_class)
which returns true iff obj is the same type as a_class
"""


def is_same_class(obj, a_class):
    """
    This function returns true iff obj is the same type as a_class;
    otherwise it returns false
    """
    return type(obj) == a_class
