"""
import_facilities.py
Author: Cole Vikupitz

Imports information from the file 'facilities.csv' into the facilities table in the
specified database from the indicated directory. The data that is imported is
committed to the database.

Usage:
    >> python3 import_facilities.py [dbname] [input_dir]
"""

# Imports
import sys
import os
import csv
import psycopg2


"""
Imports the data from 'facilities.csv' into the database.
"""
def facility_import(name, directory):

    # Connect to the database.
    with psycopg2.connect(dbname = name, host = '127.0.0.1', port = 5432) as conn:
        cur = conn.cursor()
        inputfile = open(os.path.join(directory, 'facilities.csv'))
        reader = csv.reader(inputfile)
        facilities = list(reader)

        # Iterate through the list of facilities
        for facility in facilities[1:]:
            cur.execute("INSERT INTO facilities (fcode, common_name) VALUES (%s, %s)", (facility[0], facility[1],))
        print("-- Imported", len(facilities)-1, "facilities from", os.path.join(directory, 'facilities.csv'))
        inputfile.close()


if __name__ == "__main__":

    # Incorrect number of arguments
    if len(sys.argv) != 3:
        print("Usage:")
        print("\t>> python3 import_facilities.py [dbname] [input_dir]")
        sys.exit()

    # Execute the import
    dbname = sys.argv[1]
    directory = sys.argv[2]
    facility_import(dbname, directory)


