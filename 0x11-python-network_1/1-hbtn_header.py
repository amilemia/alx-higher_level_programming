#!/usr/bin/python3
"""
    Sends a request to given URL & returns value of the X-Request-Id header.

    Args:
        url: The URL to send the request to.

    Returns:
        The value of the X-Request-Id header.
    """

import urllib.request
import sys


def get_request_id(url):

    # Open the URL in a with statement
    with urllib.request.urlopen(url) as response:
        # Get the headers of the response
        headers = response.headers

        # Get the value of the X-Request-Id header
        request_id = headers.get("X-Request-Id")

    return request_id


# Get the URL from the command line arguments
url = sys.argv[1]

# Get the request ID
request_id = get_request_id(url)

# Display the request ID
print(request_id)
