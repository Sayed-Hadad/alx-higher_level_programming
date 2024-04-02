#!/usr/bin/python3
"""
a Python script that takes in a URL and an email, sends a POST request
to the passed URLwith the email as a parameter, and displays the body
of the response (decoded in utf-8)
"""
from urllib import request, parse
from sys import argv

if __name__ == "__main__":
    email_dict = {"email": argv[2]}
    data = parse.urlencode(email_dict).encode('utf-8')
    with request.urlopen(argv[1], data=data) as resp:
        print(resp.read().decode('utf-8'))
