#!/usr/bin/python3
"""
This module is a part of alx python inheritance tasks.
it contains only a function called: is_kind_of_class(obj, a_class)
which checks wether object is an instance of a_class
"""


def is_kind_of_class(obj, a_class):
    """
    This function returns true if obj is an instance of  a_class,
    or its parent subclasses; otherwise it returns false
    """
    return isinstance(obj, a_class)
