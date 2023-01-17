#!/usr/bin/python3
""" Sends a POST request with email and return body """
from urllib import request, parse
from sys import argv


if __name__ == "__main__":
    email = {"email": argv[2]}
    data = parse.urlencode(email)
    with request.urlopen(argv[1], data.encode()) as f:
        body = f.read().decode('utf-8')
        print(body)
