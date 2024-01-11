#!/usr/bin/python3
"""
0-lookup module: it's a part of python alx tasks, it contains
only 1 function which is lookup(obj) funcition
"""


def lookup(obj):
    """
    a function that returns the list of available attributes
    and methods of an object
    """
    return dir(obj)
