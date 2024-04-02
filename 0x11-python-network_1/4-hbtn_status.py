#!/usr/bin/python3
"""
This module fetches a url and print some relvent data
of it
"""
import requests

if __name__ == "__main__":

    resp = requests.get("https://alx-intranet.hbtn.io/status")
    print(f"Body response:\n\t- type: {type(resp.text)}\n\
\t- content: {resp.text}")
