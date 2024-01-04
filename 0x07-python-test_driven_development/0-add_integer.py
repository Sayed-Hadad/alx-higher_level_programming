#!/usr/bin/python3
'''
Adding integers module.
This module contains 1 function (add_integer)
'''


def add_integer(a, b=98):
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer or float")
    
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer or float")
    
    a = int(a)
    b = int(b)

    result = a + b
    return result
