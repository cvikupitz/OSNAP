"""
directory.py
Author: Cole Vikupitz

User passes in a directory to be created. If the directory does not exist, it
gets created, or its contents are cleared if it does exist.

Usage:
    >> python3 directory.py [dir]
"""

# Imports
import sys
import os


if __name__ == "__main__":

    # Incorrect number of arguments.
    if len(sys.argv) != 2:
        print("Usage:")
        print("\t>> python3 directory.py [dir]")

    # Checks to see if the directory exists, if not, create it.
    directory = sys.argv[1]
    if not (os.path.exists(directory)):
        os.makedirs(directory)

    # If the directory exists, remove all contents inside.
    else:
        files = os.listdir(directory)
        for f in files:
            temp = os.path.join(directory, f)
            if os.path.isfile(temp):
                os.remove(temp)
    
