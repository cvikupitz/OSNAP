"""
revoke_user.py
Author: Cole Vikupitz

A web client application that revokes a user account for the L.O.S.T.
application. An existing username is given and the account's active
flag is set to false. This prevents the account from being able to login.

Usage:
    >> python3 revoke_user.py [host_url] [username]
"""

# Imports
import sys
from urllib.request import Request, urlopen
from urllib.parse import urlencode


if __name__ == "__main__":

    # Incorrect number of arguments
    if len(sys.argv) != 3:
        print("Usage:")
        print("\t>> python3 revoke_user.py [host_url] [username]")
        sys.exit()

    # Put the username into dictionary & encode.
    args = dict()
    args['username'] = sys.argv[2]
    data = urlencode(args)

    # Make the request.
    path = sys.argv[1] + 'revoke_user'
    req = Request(path, data.encode('ascii'), method = 'POST')
    res = urlopen(req)
    print(res.read().decode('ascii'))

