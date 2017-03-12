"""
export_facilities.py
Author: Cole Vikupitz

Exports information from the facilities table in the database to the indicated
directory. The data that is exported is saved into a file named 'facilities.csv'.

Usage:
    >> python3 export_facilities.py [dbname] [output_dir]
"""

# Imports
import sys
import os
import csv
import psycopg2


"""
Exports all the facilities from the facilities table into the file 'facilities.csv'.
"""
def facility_export(name, output):
    with psycopg2.connect(dbname = name, host = '127.0.0.1', port = 5432) as conn:

        # Gets all facilities form database.
        cur = conn.cursor()
        cur.execute("SELECT * FROM facilities")
        conn.commit()
        facilities = cur.fetchall()

        # Opens the file for writing.
        outputfile = open(os.path.join(output, 'facilities.csv'), 'w', newline = '')
        writer = csv.writer(outputfile)
        writer.writerow(['fcode', 'common_name'])

        # Add each user into row.
        for facility in facilities:
            writer.writerow([facility[1], facility[2]])
        outputfile.close()
        print("-- Exported", len(facilities), "facilities to", os.path.join(output, 'facilities.csv'))


if __name__ == "__main__":

    # Incorrect number of arguments
    if len(sys.argv) != 3:
        print("Usage:")
        print("\t>> python3 export_facilities.py [dbname] [output_dir]")
        sys.exit()

    # Execute the export
    dbname = sys.argv[1]
    output = sys.argv[2]
    facility_export(dbname, output)
