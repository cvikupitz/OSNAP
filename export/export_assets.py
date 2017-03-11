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
import psycopg2
from csv import *


"""
FIXME
"""
def asset_export(name, output):
    with psycopg2.connect(dbname = name, host = '127.0.0.1', port = 5432) as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM assets")
        conn.commit()
        users = cur.fetchall()
        #######


if __name__ == "__main__":

    # Incorrect number of arguments
    if len(sys.argv) != 3:
        print("Usage:")
        print("\t>> python3 export_assets.py [dbname] [output_dir]")
        sys.exit()

    # Execute the export
    dbname = sys.argv[1]
    output = sys.argv[2]
    asset_export(dbname, output)
