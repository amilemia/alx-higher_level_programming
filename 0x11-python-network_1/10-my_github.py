#!/usr/bin/python3
"""
Takes your GitHub credentials,
and uses the GitHub API to display your id
"""

if __name__ == "__main__":
    from requests import get
    from sys import argv

    r = get("https://api.github.com/user", auth=(argv[1], argv[2]))
    print(r.json().get("id"))
