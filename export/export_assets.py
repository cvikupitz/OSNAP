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
import os
import psycopg2
from csv import *


"""
Exports all the assets from the users table into the file 'assets.csv'.
"""
def asset_export(name, output):

    # Gets all assets form database.
    with psycopg2.connect(dbname = name, host = '127.0.0.1', port = 5432) as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM assets")
        conn.commit()
        assets = cur.fetchall()

    # Opens the file for writing.
    outputfile = open(os.path.join(output, 'assets.csv'), 'w', newline = '')
    writer = csv.writer(outputfile)
    writer.writerow(['asset_tag', 'description', 'facility', 'acquired', 'disposed'])

    # Add each asset into row.
    k = 0
    for asset in assets:

        cur.execute("SELECT * FROM asset_at WHERE asset_fk=%s", (asset[0],))
        conn.commit()
        asset_at = cur.fetchone()
        cur.execute("SELECT fcode FROM facilities WHERE facility_pk=%s", (asset_at[2],))
        conn.commit()
        fcode = cur.fetchone()
        writer.writerow([asset[1], asset[2], fcode, asset_at[3], asset_at[4]])
        k += 1

    outputfile.close()
    print("-- Exported", k, "assets to", os.path.join(output, 'assets.csv'))


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
