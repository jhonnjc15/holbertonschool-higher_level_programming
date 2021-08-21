#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

from requests import post
from sys import argv

if __name__ == '__main__':
    if len(argv) == 2:
        params = {'q': argv[1]}
        req = post('http://0.0.0.0:5000/search_user', params)
        try:
            resp = req.json()
            if resp:
                print("[{}] {}".format(resp.get('id'), resp.get('name')))
            else:
                print("No result")
        except Exception:
            print("Not a valid JSON")
    else:
        print("No result")
