"""
directory.py
Author: Cole Vikupitz

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
    directory = argv[1]
    if (os.path.exists(directory)):
        print("That path exists.")

    # If the directory exists, remove all contents inside.
    else:
        print("That path does not exist.")
    
