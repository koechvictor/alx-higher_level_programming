#!/usr/bin/python3
""" Sends a POST request with email and return body """
from urllib import request
import urllib.error
from sys import argv


if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as r:
            print(r.read().decode('UTF-8'))
    except urllib.error.HTTPError as e:
        print('Error code:', e.code)
