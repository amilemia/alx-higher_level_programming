#!/usr/bin/python3
"""
Sends a request to given URL & returns value of the X-Request-Id header.
"""

if __name__ == "__main__":
    from urllib.request import urlopen
    from sys import argv

    with urlopen(argv[1]) as response:
        head = response.headers.get("X-Request-Id")
        print(head)
