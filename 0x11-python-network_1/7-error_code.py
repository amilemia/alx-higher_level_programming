#!/usr/bin/python3
"""
script that takes in a URL, sends a request
and displays the body of the response
"""

if __name__ == "__main__":
    from requests import get
    from sys import argv

    response = get(argv[1])
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
