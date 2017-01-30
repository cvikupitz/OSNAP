"""
import_transport.py
CIS 322 - Assignment 2
Author - Cole Vikupitz
-----------------------------------------------------------------
Imports the downloaded legacy data into the specified database.

Usage:
    >> python3 import_transport.py [database] [port_number]

Files:
    convoy.csv
    transit.csv
"""

import sys, csv, psycopg2

def import_convoy(base, port_num):

    """
    Imports the legacy data from convoy.csv to the database.
    """

    # Opens the csv file
    file = open("convoy.csv")
    reader = csv.reader(file)
    data = list(reader)

    # Opens the database
    conn = psycopg2.connect(dbname = base, host = "localhost", port = port_num)
    curr = conn.cursor()

    # Inserts the data in the appropriate places
    for dt in data[1:]:
        ########## FIXME

    # Closes the database
    conn.close()
    curr.close()


def import_transit(base, port_num):

    """
    Imports the legacy data from transit.csv to the database.
    """

    # Opens the csv file
    file = open("transit.csv")
    reader = csv.reader(file)
    data = list(reader)

    # Opens the database
    conn = psycopg2.connect(dbname = base, host = "localhost", port = port_num)
    curr = conn.cursor()

    # Inserts the data in the appropriate places
    for dt in data[1:]:
        ###### FIXME

    # Closes the database
    conn.close()
    curr.close()


if __name__ == "__main__":

    # Incorrect usage
    if len(sys.argv) != 3:
        print("Usage:")
        print("\t>> python3 import_transport.py [database_name] [port_number]")
        sys.exit()

    # Execute the imports
    import_convoy(sys.argv[1], sys.argv[2])
    import_transit(sys.argv[1], sys.argv[2])
