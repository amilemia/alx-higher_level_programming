#!/usr/bin/python3
"""
Sends a request to the URL and displays the value of
the variable X-Request-Id in the response header
"""
if __name__ == "__main__":
    from requests import get
    from sys import argv

    html = get(argv[1])
    print(html.headers.get("X-Request-Id"))
