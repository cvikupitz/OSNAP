"""
import_users.py
Author: Cole Vikupitz

Imports information from the file 'users.csv' into the users table in the specified
database from the indicated directory. The data that is imported is committed to the
new database.

Usage:
    >> python3 import_users.py [dbname] [input_dir]
"""

# Imports
import sys
import os
import csv
import psycopg2


"""
Imports the data from 'users.csv' into the database.
"""
def user_import(name, directory):
    with psycopg2.connect(dbname = name, host = '127.0.0.1', port = 5432) as conn:
        cur = conn.cursor()
        inputfile = open(os.path.join(directory, 'users.csv'))
        reader = csv.reader(inputfile)
        users = list(reader)

        for user in users[1:]:
            if user[2] == 'Logistics Officer':
                role = 1
            else:
                role = 2
            cur.execute("INSERT INTO users (username, password, role, active) VALUES (%s, %s, %s, %s)",
                        (user[0], user[1], role, user[3]))
            conn.commit()
        print("-- Imported", len(users)-1, "users from", os.path.join(directory, 'users.csv'))
        inputfile.close()
        


if __name__ == "__main__":

    # Incorrect number of arguments
    if len(sys.argv) != 3:
        print("Usage:")
        print("\t>> python3 import_users.py [dbname] [input_dir]")
        sys.exit()

    # Execute the import
    dbname = sys.argv[1]
    directory = sys.argv[2]
    user_import(dbname, directory)


    
