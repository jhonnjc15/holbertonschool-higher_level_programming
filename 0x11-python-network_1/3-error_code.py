#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request
to the URL and displays the body of the response (decoded in utf-8).
"""
from urllib import request
from urllib import error
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    request_ = request.Request(url)
    try:
        with request.urlopen(request_) as response:
            print(response.read().decode("ascii"))
    except error.HTTPError as err:
        print("Error code: {}".format(err.code))
