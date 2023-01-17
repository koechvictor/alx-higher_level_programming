#!/usr/bin/python3
""" Use requests to get response and search key using get """
import requests
from sys import argv


if __name__ == "__main__":
    res = requests.get(argv[1]).headers.get("X-Request-Id")
    print(res)
