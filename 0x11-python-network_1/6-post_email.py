#!/usr/bin/python3
"""
Script that takes in a URL and an email address,
sends a POST request to URL with the email as a parameter,
and displays the body of the response
"""
if __name__ == "__main__":
    from requests import post
    from sys import argv

    html = post(argv[1], data={"email": argv[2]})
    print(html.text)
