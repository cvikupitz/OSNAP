"""
import_transfers.py
Author: Cole Vikupitz

Imports information from the file 'transfers.csv' into the requests table in the
specified database from the indicated directory. The data that is imported is
committed to the database.

Usage:
    >> python3 import_transfers.py [dbname] [input_dir]
"""

# Imports
import sys
import os
import csv
import psycopg2


"""
Imports the data from 'transfers.csv' into the database.
"""
def transfer_import(name, directory):

    # Connect to the database.
    with psycopg2.connect(dbname = name, host = '127.0.0.1', port = 5432) as conn:
        cur = conn.cursor()
        inputfile = open(os.path.join(directory, 'transfers.csv'))
        reader = csv.reader(inputfile)
        transfers = list(reader)

        # Iterate through the list of transfers
        for transfer in transfers[1:]:

            # Generete ID stamp
            id_stamp = os.urandom(10).hex()

            # User pk of the requester
            cur.execute("SELECT user_pk FROM users WHERE username=%s", (transfer[1],))
            conn.commit()
            requester = cur.fetchone()[0]

            # User pk of the approver
            cur.execute("SELECT user_pk FROM users WHERE username=%s", (transfer[3],))
            conn.commit()
            approver = cur.fetchone()[0]

            # Facility pk of the source
            cur.execute("SELECT facility_pk FROM facility WHERE fcode=%s", (transfer[5],))
            conn.commit()
            src = cur.fetchone()[0]

            # Facility pk of the destination
            cur.execute("SELECT facility_pk FROM facility WHERE fcode=%s", (transfer[6],))
            conn.commit()
            dest = cur.fetchone()[0]

            # Asset fk of the asset being transferred.
            cur.execute("SELECT asset_pk FROM assets WHERE tag=%s", (transfer[0],))
            conn.commit()
            asset_fk = cur.fetchone()[0]

            # Insert into database
            cur.execute("INSERT INTO requests (id_stamp, requester, approver, submit_date, approve_date,\
                        src_facility, dest_facility, asset_fk, load_time, unload_time) VALUES \
                        (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                        (id_stamp, requester, approver, transfer[2], transfer[4], src, dest, asset_fk, transfer[7], transfer[8],))
            conn.commit()
        print("-- Imported", len(transfers)-1, "transfers from", os.path.join(directory, 'transfers.csv'))
        inputfile.close()


if __name__ == "__main__":

    # Incorrect number of arguments
    if len(sys.argv) != 3:
        print("Usage:")
        print("\t>> python3 import_transfers.py [dbname] [input_dir]")
        sys.exit()

    # Execute the import
    dbname = sys.argv[1]
    directory = sys.argv[2]
    asset_import(dbname, directory)



