#!/usr/bin/python3
"""
This module is an implementation for the
Pascal's triangle coeffs
"""


def compute_row(row, last_row):
    """
    This function computes the values of each row
    for Pascal's triangle
    """
    if last_row == []:
        return [1]
    this_row = []
    for i in range(row):
        if (i == 0) or (i == (row-1)):
            this_row.append(1)
        else:
            this_row.append(last_row[i] + last_row[i-1])
    return this_row


def pascal_triangle(n):
    """
    This function implements the Pascal's triangle
    coeff
    """
    last_row = []
    pascal_list = []
    this_row = []
    for i in range(1, n+1):
        this_row = compute_row(i, last_row)
        pascal_list.append(this_row)
        last_row = this_row
    return pascal_list
