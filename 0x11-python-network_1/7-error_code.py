#!/usr/bin/python3
""" Use requests to make a post and return body """
import requests
from sys import argv


if __name__ == "__main__":
    res = requests.get(argv[1])
    code = res.status_code
    if code > 400:
        print("Error code:", code)
    else:
        print(res.text)
