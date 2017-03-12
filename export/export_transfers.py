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
import os
import csv
import psycopg2


"""
Exports all the transfers from the requests table into the file 'assets.csv'.
"""
def transfer_export(name, output):

    # Gets all transfers form database.
    with psycopg2.connect(dbname = name, host = '127.0.0.1', port = 5432) as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM requests")
        conn.commit()
        transfers = cur.fetchall()

    # Opens the file for writing.
    outputfile = open(os.path.join(output, 'transfers.csv'), 'w', newline = '')
    writer = csv.writer(outputfile)
    writer.writerow(['asset_tag', 'request_by', 'request_dt', 'approve_by', 'approve_dt', 'source',
                     'destination', 'load_dt', 'unload_dt'])

    # Add each transfer into row.
    for transfer in transfers:

        # The asset tag.
        cur.execute("SELECT tag FROM assets WHERE asset_pk=%s", (transfer[8],))
        conn.commit()
        tag = cur.fetchone()[0]

        # Username of the requester.
        cur.execute("SELECT username FROM users WHERE user_pk=%s", (transfer[2],))
        conn.commit()
        requester = cur.fetchone()[0]

        # Username of the approver.
        cur.execute("SELECT username FROM users WHERE user_pk=%s", (transfer[3],))
        conn.commit()
        approver = cur.fetchone()[0]

        # Source facility.
        cur.execute("SELECT fcode FROM facilities WHERE facility_pk=%s", (transfers[6],))
        conn.commit()
        src = cur.fetchone()[0]

        # Destination facility.
        cur.execute("SELECT fcode FROM facilities WHERE facility_pk=%s", (transfers[7],))
        conn.commit()
        dest = cur.fetchone()[0]

        writer.writerow([tag, requester, transfer[4], approver, transfer[5], src, dest, transfer[9], transfer[10]])
    outputfile.close()
    print("-- Exported", len(transfers), "transfers to", os.path.join(output, 'transfers.csv'))


if __name__ == "__main__":

    # Incorrect number of arguments
    if len(sys.argv) != 3:
        print("Usage:")
        print("\t>> python3 export_transfers.py [dbname] [output_dir]")
        sys.exit()

    # Execute the export
    dbname = sys.argv[1]
    output = sys.argv[2]
    transfer_export(dbname, output)
