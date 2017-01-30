"""
import_securities.py
CIS 322 - Assignment 2
Author - Cole Vikupitz
-----------------------------------------------------------------
Imports the downloaded legacy data into the specified database.

Usage:
    >> python3 import_securities.py [database] [port_number]

Files:
    security_levels.csv
    security_compartments.csv
"""

import sys, csv, psycopg2

def import_levels(base, port_num):

    """
    Imports the legacy data from security_levels.csv to the database.
    """

    # Opens the csv file
    file = open("security_levels.csv")
    reader = csv.reader(file)
    data = list(reader)

    # Opens the database
    conn = psycopg2.connect(dbname = base, host = "localhost", port = port_num)
    curr = conn.cursor()

    # Inserts the data in the appropriate places
    for dt in data[1:]:
        curr.execute("INSERT INTO levels (abbrv, comment) VALUES (%s, %s)", dt[0], dt[1])

    # Closes the database
    conn.close()
    curr.close()


def import_compartments(base, port_num):

    """
    Imports the legacy data from security_compartments.csv to the database.
    """

    # Opens the csv file
    file = open("security_compartments.csv")
    reader = csv.reader(file)
    data = list(reader)

    # Opens the database
    conn = psycopg2.connect(dbname = base, host = "localhost", port = port_num)
    curr = conn.cursor()

    # Inserts the data in the appropriate places
    for dt in data[1:]:
        curr.execute("INSERT INTO compartments (abbrv, comment) VALUES (%s, %s)", dt[0], dt[1])

    # Closes the database
    conn.close()
    curr.close()


if __name__ == "__main__":

    # Incorrect usage
    if len(sys.argv) != 3:
        print("Usage:")
        print("\t>> python3 import_legacy.py [database_name] [port_number]")
        sys.exit()

    # Execute the imports
    import_levels(sys.argv[1], sys.argv[2])
    import_compartments(sys.argv[1], sys.argv[2])
