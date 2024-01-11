#!/usr/bin/python3

"""
This module is part of alx python tasks.
it contains only one function: class_to_json(obj)
"""


def class_to_json(obj):
    """
    a function that returns the dictionary description with
    simple data structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object:
    """
    attrs = vars(obj)
    return attrs
