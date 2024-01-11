#!/usr/bin/python3
"""
This module is a part of alx python inheritance tasks.
it contains only a function called: is_kind_of_class(obj, a_class)
which checks wether object is an instance of a sub class of a_class
"""


def inherits_from(obj, a_class):
    """
    This function returns true iff obj is an instance of
    a sub_class of a_class; otherwise it returns false
    """
    return isinstance(obj, a_class) and type(obj) != a_class
