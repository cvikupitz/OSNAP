"""
import_transfers.py
Author: Cole Vikupitz

FIXME

Usage:
    >> python3 import_transfers.py [dbname] [input_dir]
"""

# Imports
import sys
from csv import *


"""
FIXME
"""
def transfer_inport(dbname, input):
    ### FIXME


if __name__ == "__main__":

    # Incorrect number of arguments
    if len(sys.argv) != 3:
        print("Usage:")
        print("\t>> python3 import_transfers.py [dbname] [input_dir]")
        sys.exit()

    # Execute the import
    print("Hello")
