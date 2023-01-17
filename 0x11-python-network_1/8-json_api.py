#!/usr/bin/python3
""" Use requests to make a post and return body """
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) < 2:
        data = {"q": ""}
    else:
        data = {"q": argv[1]}
    url = "http://0.0.0.0:5000/search_user"
    res = requests.post(url, data)
    try:
        _json = res.json()
    except ValueError:
        print("Not a valid JSON")
    if len(_json) < 1 or ("id" and "name") not in _json:
        print("No result")
    else:
        print("[{}] {}".format(_json["id"], _json["name"]))
