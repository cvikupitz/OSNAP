"""
import_assets.py
CIS 322 - Assignment 2
Author - Cole Vikupitz
-----------------------------------------------------------------
Imports the downloaded legacy data into the specified database.

Usage:
    >> python3 import_assets.py [database] [port_number]

Files:
    acquisitions.csv
    product_list.csv
"""

import sys, csv, psycopg2

def import_acquisitions(base, port_num):

    """
    Imports the legacy data from acquisitions.csv to the database.
    """

    # Opens the csv file
    file = open("acquisitions.csv")
    reader = csv.reader(file)
    data = list(reader)

    # Opens the database
    conn = psycopg2.connect(dbname = base, host = "localhost", port = port_num)
    curr = conn.cursor()

    # Inserts the data in the appropriate places
    for dt in data[1:]:
        curr.execute("INSERT INTO asset_at (arrive_dt, depart_dt) VALUES (%s, %s)", dt[4], dt[3])

    # Closes the database
    conn.close()
    curr.close()


def import_products(base, port_num):

    """
    Imports the legacy data from product_list.csv to the database.
    """

    # Opens the csv file
    file = open("product_list.csv")
    reader = csv.reader(file)
    data = list(reader)

    # Opens the database
    conn = psycopg2.connect(dbname = base, host = "localhost", port = port_num)
    curr = conn.cursor()

    # Inserts the data in the appropriate places
    for dt in data[1:]:
        curr.execute("INSERT INTO products (vendor, description, alt_description) VALUES (%s, %s, %s)",
                     dt[4], dt[2], "Name: " + dt[0] + "\nModel: " + dt[1] + "\nPrice: " + dt[2])

    # Closes the database
    conn.close()
    curr.close()


if __name__ == "__main__":

    # Incorrect usage
    if len(sys.argv) != 3:
        print("Usage:")
        print("\t>> python3 import_assets.py [database_name] [port_number]")
        sys.exit()

    # Execute the imports
    import_acquisitions(sys.argv[1], sys.argv[2])
    import_products(sys.argv[1], sys.argv[2])
