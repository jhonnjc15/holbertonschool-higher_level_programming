#!/usr/bin/python3
"""

"""

from urllib import request
from urllib import parse
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    params = {"email": argv[2]}
    consulta = parse.urlencode(params).encode("ascii")
    request_ = request.Request(url, consulta)
    with request.urlopen(request_) as response:
        print(response.read().decode("utf-8"))
