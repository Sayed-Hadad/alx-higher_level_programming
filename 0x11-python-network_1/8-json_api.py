#!/usr/bin/python3
"""
a Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if (len(argv) == 1):
        q = ""
    else:
        q = argv[1]
    letter = {'q': q}
    r = requests.post(url, data=letter)
    try:
        json_data = r.json()
        if json_data:
            print(f"[{json_data.get('id')}] {json_data.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
