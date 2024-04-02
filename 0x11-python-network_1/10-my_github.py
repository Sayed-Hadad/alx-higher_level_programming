#!/usr/bin/python3
"""
a Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/user"
    try:
        r = requests.get(url, auth=(argv[1], argv[2]))
        r.raise_for_status()
        print(r.json().get('id'))
    except Exception:
        print('None')
