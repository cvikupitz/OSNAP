"""
revoke_user.py
Author: Cole Vikupitz

FIXME

Usage:
    >> python3 revoke_user.py [host_url] [username]
"""

import sys


if __name__ == "__main__":

    # Incorrect number of arguments
    if len(sys.argv) != 3:
        print("Usage:")
        print("\t>> python3 revoke_user.py [host_url] [username]")
        sys.exit()

    ######
    print("Success")
