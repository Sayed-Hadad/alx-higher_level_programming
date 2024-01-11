#!/usr/bin/python3
"""
This module is part of Alx python tasks.
It contains one function, append_write(),
which write a text to a file
"""


def append_write(filename="", text=""):
    """
    function that appends a string to a text file (UTF8),
    and returns the number of characters added,
    It creates the file if doesn’t exist.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
