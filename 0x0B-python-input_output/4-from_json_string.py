#!/usr/bin/python3
"""
This module is a part of alx python tasks.
It contains only one function (from_json_string(my_str))
"""
import json


def from_json_string(my_str):
    """
    a function that returns an object (Python data structure)
    represented by a JSON string
    """
    return json.loads(my_str)
