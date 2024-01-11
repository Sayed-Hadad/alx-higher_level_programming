#!/usr/bin/python3
"""
This module is a part of alx python tasks.
It contains only one function (to_json_string(my_obj))
"""
import json


def to_json_string(my_obj):
    """
    a function that returns the JSON representation
    of an object (string)
    """
    return json.dumps(my_obj)
