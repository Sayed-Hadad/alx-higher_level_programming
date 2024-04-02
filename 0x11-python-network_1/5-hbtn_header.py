#!/usr/bin/python3
"""
 a Python script that takes in a URL, sends a request to the URL
 and displays the value of the X-Request-Id variable found in the
 header of the response.
"""
import requests
from sys import argv

if __name__ == "__main__":
    r = requests.get(argv[1])
    id_value = r.headers.get('X-Request-Id')
    print(id_value)
