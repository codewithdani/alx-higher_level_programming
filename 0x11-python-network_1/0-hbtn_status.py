#!/usr/bin/python3
"""
Script that
Fetches https://alx-intranet.hbtn.io/status and displays its body.
"""


if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        body = res.read()
        print("Body response:")
        print("\t- type:", type(body))
        print("\t- content: {}".format(body))
        print("\t- utf8 content:", body.decode('utf-8'))
