"""
import_assets.py
Author: Cole Vikupitz

Imports information from the file 'assets.csv' into the assets table in the
specified database from the indicated directory. The data that is imported is
committed to the database.

Usage:
    >> python3 import_assets.py [dbname] [input_dir]
"""

# Imports
import sys
import os
import csv
import psycopg2


"""
Imports the data from 'assets.csv' into the database.
"""
def asset_import(name, directory):

    # Connect to the database.
    with psycopg2.connect(dbname = name, host = '127.0.0.1', port = 5432) as conn:
        cur = conn.cursor()
        inputfile = open(os.path.join(directory, 'assets.csv'))
        reader = csv.reader(inputfile)
        assets = list(reader)

        # Iterate through the list of assets
        for asset in assets[1:]:

            # Insert asset into assets table.
            cur.execute("INSERT INTO assets (tag, description) VALUES (%s, %s)", (asset[0], asset[1],))
            conn.commit()

            # Get the asset fk
            cur.execute("SELECT asset_pk FROM assets WHERE tag=%s", (asset[0],))
            conn.commit()
            asset_fk = cur.fetchone()[0]

            # Get the facility fk.
            cur.execute("SELECT facility_pk FROM facilities WHERE fcode=%s", (asset[2],))
            conn.commit()
            facility = cur.fetchone()[0]

            # Insert into the asset_at table.
            cur.execute("INSERT INTO asset_at (asset_fk, facility_fk, arrive_date, depart_date) VALUES (%s, %s, %s, %s)",
                        (asset_fk, facility, asset[3], asset[4]))
            conn.commit()
        print("-- Imported", len(assets)-1, "assets from", os.path.join(directory, 'assets.csv'))
        inputfile.close()


if __name__ == "__main__":

    # Incorrect number of arguments
    if len(sys.argv) != 3:
        print("Usage:")
        print("\t>> python3 import_assets.py [dbname] [input_dir]")
        sys.exit()

    # Execute the import
    dbname = sys.argv[1]
    directory = sys.argv[2]
    asset_import(dbname, directory)


