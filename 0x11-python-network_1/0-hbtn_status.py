#!/usr/bin/python3
"""
This module fetches a url and print some relvent data
of it
"""
from urllib import request

if __name__ == "__main__":
    with request.urlopen("https://alx-intranet.hbtn.io/status") as resp:
        content = resp.read()
        print(f"Body response:\n\t- type: {type(content)}\n\
\t- content: {content}\n\
\t- utf8 content: {content.decode('utf-8')}")
