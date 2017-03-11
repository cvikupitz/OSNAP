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
import psycopg2
from csv import *


"""
FIXME
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
    k = 0
    for transfer in transfers:

        ###################
        # FIXME ###########
        ###################
        pass

    outputfile.close()
    print("-- Exported", k, "transfers to", os.path.join(output, 'transfers.csv'))


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
