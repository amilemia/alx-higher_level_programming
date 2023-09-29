#!/usr/bin/python3
"""
Python script that takes in a letter
and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parametere.
"""

if __name__ == "__main__":
    from requests import post
    from sys import argv

    q = argv[1] if len(argv) > 1 else ""
    res = post("http://0.0.0.0:5000/search_user", data={"q": q})
    try:
        data = res.json()
        if data == {}:
            print("No result")
        else:
            print("[{}] {}".format(data.get("id"), data.get("name")))
    except ValueError:
        print("Not a valid JSON")
