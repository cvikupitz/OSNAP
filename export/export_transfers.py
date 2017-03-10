"""
export_transfers.py
Author: Cole Vikupitz

Exports information from the requests table in the database to the indicated
directory. The data that is exported is saved into a file named 'transfers.csv'.

Usage:
    >> python3 export_transfers.py [dbname] [output_dir]
"""

# Imports
import sys
from csv import *


"""
FIXME
"""
def transfer_export(dbname, output):
    ### FIXME


if __name__ == "__main__":

    # Incorrect number of arguments
    if len(sys.argv) != 3:
        print("Usage:")
        print("\t>> python3 export_transfers.py [dbname] [output_dir]")
        sys.exit()

    # Execute the export
    print("Hello")