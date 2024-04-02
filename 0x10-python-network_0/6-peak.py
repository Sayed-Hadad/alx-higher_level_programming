#!/usr/bin/python3
""" This module contains the peak function """


def find_peak(arr):
    """ find a peak in the list in o(log(n))"""
    if (arr is None or len(arr) == 0):
        return None
    start = 0
    end = len(arr) - 1
    while (start < end):
        mid = (start + end) // 2
        if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]:
            return arr[mid]
        if arr[mid + 1] > arr[mid - 1]:
            start = mid + 1
        else:
            end = mid - 1
    return arr[start]
