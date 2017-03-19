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
    args['password'] = sys.argv[3]
    if sys.argv[4] == 'logofc':
        args['role'] = 1
    else:
        args['role'] = 2
    data = urlencode(args)
    print("-- Activating the user", sys.argv[2])

    # Make the request.
    try:
        path = sys.argv[1] + 'create_user'
        req = Request(path, data.encode('ascii'), method = 'POST')
        res = urlopen(req)
        print("-- Successfully activated the user", args['username'])
    except:
        print("Something went wrong, activation failed.")
