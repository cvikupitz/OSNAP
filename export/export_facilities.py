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
Exports all the facilities from the users table into the file 'facilities.csv'.
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
        k = 0
        for facl in facilities:
            writer.writerow([facl[1], facl[2]])
            k += 1
        outputfile.close()
        print("-- Exported", k, "facilities to", os.path.join(output, 'facilities.csv'))


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
