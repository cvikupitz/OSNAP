"""
export_users.py
Author: Cole Vikupitz

Exports information from the users table in the database to the indicated
directory. The data that is exported is saved into a file named 'users.csv'.

Usage:
    >> python3 export_users.py [dbname] [output_dir]

Output:
    [output_dir]/users.csv
"""

# Imports
import sys
import os
import csv
import psycopg2


"""
Exports all the users from the users table into the file 'users.csv'.
"""
def user_export(name, output):
    with psycopg2.connect(dbname = name, host = '127.0.0.1', port = 5432) as conn:
        
        # Gets all users form database.
        cur = conn.cursor()
        cur.execute("SELECT * FROM users")
        conn.commit()
        users = cur.fetchall()

        # Opens the file for writing.
        outputfile = open(os.path.join(output, 'users.csv'), 'w', newline = '')
        writer = csv.writer(outputfile)
        writer.writerow(['username', 'password', 'role', 'active'])

        # Add each user into row.
        for user in users:
            cur.execute("SELECT title FROM roles WHERE role_pk=%s", (user[3],))
            conn.commit()
            role = cur.fetchone()[0]
            writer.writerow([user[1], user[2], role, user[4]])
        outputfile.close()


if __name__ == "__main__":

    # Incorrect number of arguments
    if len(sys.argv) != 3:
        print("Usage:")
        print("\t>> python3 export_users.py [dbname] [output_dir]")
        sys.exit()

    # Execute the export
    dbname = sys.argv[1]
    output = sys.argv[2]
    user_export(dbname, output)


