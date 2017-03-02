"""
psql.py
Author: Cole Vikupitz
"""

from config import dbname, dbhost, dbport
import psycopg2


"""
Checks to see if the given username and password belongs to an account.

Args:
    uname - The username of the account.
    password - The password of the account.
Returns:
    True if the account exists, false if not.
"""
def authenticate(uname, password):
    with psycopg2.connect(dbname = dbname, host = dbhost, port = dbport) as conn:
        cur.execute("SELECT username FROM USERS WHERE username=%s AND password=%s",
                    (uname, password))
        return (cur.fetchone() != None)


"""
Creates an account and inserts the data into the database given the username,
password, and the user role. The inserted ccount is commited to the database.

Args:
    uname - The account's username.
    password - The account password.
    role - The role of the account.
Returns:
    None
"""
def create_account(uname, password, role):
    with psycopg2.connect(dbname = dbname, host = dbhost, port = dbport) as conn:
        cur.execute("INSERT INTO users (username, password, role) VALUES (%s, %s, %s)",
                    (uname, password, role))
        conn.commit()
        return None


"""
Checks to see if the given username currently belongs to an account.

Args:
    uname - The username to search for.
Returns:
    True if the username already exists, false if not.
"""
def user_exists(uname):
    with psycopg2.connect(dbname = dbname, host = dbhost, port = dbport) as conn:
        cur.execute("SELECT username FROM users WHERE username=%s",
                    (uname))
        return (cur.fetchone() != None)


"""
Fetches and returns the role title of the account given the username.

Args:
    uname - The username to fetch the role of.
Returns:
    The title of the role of the user.
"""
def fetch_role(uname):
    """"""
    with psycopg2.connect(dbname = dbname, host = dbhost, port = dbport) as conn:
        cur.execute("SELECT r.title FROM roles r JOIN users u ON r.role_pk=u.role WHERE u.username=%s",
                    (uname))
        return (cur.fetchone()[0])
