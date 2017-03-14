"""
activate_user.py
Author: Cole Vikupitz

FIXME

Usage:
    >> python3 activate_user.py [host_url] [username] [password] [role]
"""

import sys


if __name__ == "__main__":

    # Incorrect number of arguments
    if len(sys.argv) != 5:
        print("Usage:")
        print("\t>> python3 activate_user.py [host_url] [username] [password] [role]")
        sys.exit()

    ######
    print("Success")
