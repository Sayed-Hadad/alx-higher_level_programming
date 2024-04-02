#!/usr/bin/python3
"""
 a Python script that takes in a URL, sends a request to the URL and displays
 the body of the response (decoded in utf-8).
"""
import requests
from sys import argv

if __name__ == "__main__":
    try:
        r = requests.get(argv[1])
        r.raise_for_status()
        print(r.text)
    except requests.exceptions.HTTPError as err:
        print(f'Error code: {r.status_code}')
