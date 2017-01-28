"""
import_inventories.py
CIS 322 - Assignment 2
Author - Cole Vikupitz
-----------------------------------------------------------------
Imports the downloaded legacy data into the specified database.

Usage:
    >> python3 import_legacy.py [database] [port_number]

Files:
    DC_inventory.csv
    HQ_inventory.csv
    MB005_inventory.csv
    NC_inventory.csv
    SPNV_inventory.csv
"""

import sys, csv, psycopg2

def import_inventory(name, base):
    """
    Imports the legacy data from all the inventory files to the database.
    """
    file = open(name)
    reader = csv.reader(file)
    data = list(reader)
	conn = psycopg2.connect(dbname = base, host = "localhost")
    curr = conn.cursor()
	for dt in data[1:]:
        curr.execute("INSERT INTO assets (product_pk, asset_tag, description) VALUES (NULL, %s, %s)", dt[0], dt[1])
    conn.close()
    curr.close()
    

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage:")
        print("\t>> python3 import_legacy.py [database_name] [port_number]")
        sys.exit()

    import_inventory("DC_inventory.csv", sys.argv[1])
    import_inventory("HQ_inventory.csv", sys.argv[1])
    import_inventory("MB005_inventory.csv", sys.argv[1])
    import_inventory("NC_inventory.csv", sys.argv[1])
    import_inventory("SPNV_inventory.csv", sys.argv[1])