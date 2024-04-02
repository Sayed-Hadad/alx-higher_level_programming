#!/bin/bash
# a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response, when code = 200
curl -sX GET "$1" -L
