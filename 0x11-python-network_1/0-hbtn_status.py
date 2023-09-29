#!/usr/bin/python3
"""
Fetches the status of the ALX intranet website.

Usage:
    python 0-hbtn_status.py

Output:
    Body response:
        - type: <class 'bytes'>
        - content: b'OK'
        - utf8 content: OK
"""

import urllib.request

# Open the URL in a with statement
with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
    # Get the body of the response
    body = response.read()

# Display the body of the response
print("Body response:")

# Print the type of the body
print("- type:", type(body))

# Print the content of the body
print("- content:", body)

# Print the utf-8 content of the body
print("- utf8 content:", body.decode())
