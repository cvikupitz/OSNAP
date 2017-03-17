"""
activate_user.py
Author: Cole Vikupitz

A web client application that creates a user account for the L.O.S.T.
application. A new user is created and inserted into the database. If
the username exists, it is disabled, otherwise a new account is created.

Usage:
    >> python3 activate_user.py [host_url] [username] [password] [role]
"""

import sys
import json
from urllib.request import Request, urlopen
from urllib.parse import urlencode


if __name__ == "__main__":

    # User must pass in the correct number of arguments.
    if len(sys.argv) != 5:
        print("Usage:")
        print("\t>> python3 activate_user.py [host_url] [username] [password] [role]")
        sys.exit()

    # Usernames and passwords must be 16 characters or less.
    if len(sys.argv[2]) > 16:
        print("Usernames cannot be longer than 16 characters.")
        sys.exit()
    if len(sys.argv[3]) > 16:
        print("Passwords cannot be longer that 16 characters.")
        sys.exit()

    # Role must be logistics or facilities officer.
    if (sys.argv[4] != 'logofc' and sys.argv[4] != 'facofc'):
        print("Role must be 'logofc' or 'facofc'.")
        sys.exit()

    # -------------------
    print("Creating the user", sys.argv[2])
    ####
    print("User", sys.argv[2], "was successfully activated.")





