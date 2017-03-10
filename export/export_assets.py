"""
export_assets.py
Author: Cole Vikupitz

Exports information from the assets table in the database to the indicated
directory. The data that is exported is saved into a file named 'assets.csv'.

Usage:
    >> python3 export_assets.py [dbname] [output_dir]
"""

# Imports
import sys
from csv import *


"""
FIXME
"""
def asset_export(dbname, output):
    ### FIXME


if __name__ == "__main__":

    # Incorrect number of arguments
    if len(sys.argv) != 3:
        print("Usage:")
        print("\t>> python3 export_assets.py [dbname] [output_dir]")
        sys.exit()

    # Execute the export
    print("Hello")
