#!/usr/bin/python3
""" Use urllib to fetch website and display X-Request-Id """
import urllib.request
from sys import argv


if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as response:
        print(response.headers.get("X-Request-Id"))
