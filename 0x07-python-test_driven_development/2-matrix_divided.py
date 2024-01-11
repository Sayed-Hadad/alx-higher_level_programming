#!/usr/bin/python3
'''
matrix_divided module.
It contains only one function which isinstance
matrix_divided
'''


def matrix_divided(matrix, div):
    '''
    it divides all the values of the matrix by the variable div
    it ensures that (matrix) is a valid list of list of numbers
    and that div is a numbere that is not zero, and return the
    values of the matrix divided by the div variable rounded to
    2 decimal places
    '''

    str_msg = 'matrix must be a matrix (list of lists) of integers/floats'
    if not isinstance(matrix, list) or \
        not all(isinstance(row, list) for row in matrix) or not \
            all(isinstance(value, (float, int)) for row in matrix
                for value in row):
        raise TypeError(str_msg)

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')
    if not isinstance(div, (float, int)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    return [[round(value/div, 2) for value in row] for row in matrix]
