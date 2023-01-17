#!/usr/bin/python3
""" Use requests to make a post and return body """
import requests
from sys import argv


if __name__ == "__main__":
    data = {"email": argv[2]}
    res = requests.post(argv[1], data)
    print(res.text)
