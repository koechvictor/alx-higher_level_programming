#!/usr/bin/python3
""" get data from starwars api """
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/user"
    res = requests.get(url, auth=(argv[1], argv[2]))
    print(res.json().get('id'))
