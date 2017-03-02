"""
psql.py
Author: Cole Vikupitz

Contains functions that performs SQL commands used in the L.O.S.T web application.
"""

# Imports
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
        cur = conn.cursor()
        temp = (uname, password,)
        cur.execute("SELECT username FROM USERS WHERE username=%s AND password=%s", temp)
        conn.commit()
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
        cur = conn.cursor()
        temp = (uname, password, role,)
        cur.execute("INSERT INTO users (username, password, role) VALUES (%s, %s, %s)", temp)
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
        cur = conn.cursor()
        temp = (uname,)
        cur.execute("SELECT username FROM users WHERE username=%s", temp)
        conn.commit()
        return (cur.fetchone() != None)


"""
Fetches and returns the role title of the account given the username.

Args:
    uname - The username to fetch the role of.
Returns:
    The title of the role of the user.
"""
def fetch_role(uname):
    with psycopg2.connect(dbname = dbname, host = dbhost, port = dbport) as conn:
        cur = conn.cursor()
        temp = (uname,)
        cur.execute("SELECT r.title FROM roles r JOIN users u ON r.role_pk=u.role WHERE u.username=%s", temp)
        conn.commit()
        return (cur.fetchone()[0])


"""
Fetches and returns all the facilities currently in the database in a list.

Args:
    None
Returns:
    A list of all the facilities currently in the database.
"""
def get_facilities():
    with psycopg2.connect(dbname = dbname, host = dbhost, port = dbport) as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM facilities")
        conn.commit()
        return (cur.fetchall())


"""
Checks to see of a facility currently exists within the database with either the
given name or facility code.

Args:
    name - The facility's common name.
    code - The facility's identification code.
Returns:
    True if there exists a facility with the given name or code, or false if both
    are unique.
"""
def facility_exists(name, code):
    with psycopg2.connect(dbname = dbname, host = dbhost, port = dbport) as conn:
        cur = conn.cursor()
        temp = (name, code,)
        cur.execute("SELECT * FROM facilities WHERE common_name=%s OR code=%s", temp)
        conn.commit()
        return (cur.fetchone() != None)


"""
Creates and inserts a new facility instance into the database given the facility
common name and its 6-digit identification code. Changes are committed to the
database.

Args:
    name - The facility's common name.
    code - The facility's identification code.
Returns:
    None
"""
def create_facility(name, code):
    with psycopg2.connect(dbname = dbname, host = dbhost, port = dbport) as conn:
        cur = conn.cursor()
        temp = (name, code,)
        cur.execute("INSERT INTO facilities (common_name, code) VALUES (%s, %s)", temp)
        conn.commit()
        return None


"""
Fetches and returns all the assets currently in the database in a list.

Args:
    None
Returns:
    A list of all the assets currently in the database.
"""
def get_assets():
    with psycopg2.connect(dbname = dbname, host = dbhost, port = dbport) as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM assets")
        conn.commit()
        return (cur.fetchall())


"""
Checks to see of an asset currently exists within the database with the given
asset tag.

Args:
    name - The asset's tag.
Returns:
    True if there exists an asset with the given tag, or false otherwise.
"""
def asset_exists(tag):
    with psycopg2.connect(dbname = dbname, host = dbhost, port = dbport) as conn:
        cur = conn.cursor()
        temp = (tag,)
        cur.execute("SELECT * FROM assets WHERE tag=%s", temp)
        conn.commit()
        return (cur.fetchone() != None)
