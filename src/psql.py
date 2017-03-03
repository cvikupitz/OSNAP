"""
psql.py
Author: Cole Vikupitz

Contains functions that performs SQL commands used in the L.O.S.T. web application.
"""


# Imports
from util import *
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
        cur.execute("SELECT username FROM USERS WHERE username=%s AND password=%s", (uname, password,))
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
        cur.execute("INSERT INTO users (username, password, role) VALUES (%s, %s, %s)", (uname, password, role,))
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
        cur.execute("SELECT username FROM users WHERE username=%s", (uname,))
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
        cur.execute("SELECT r.title FROM roles r JOIN users u ON r.role_pk=u.role WHERE u.username=%s", (uname,))
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
        cur.execute("SELECT * FROM facilities WHERE common_name=%s OR fcode=%s", (name, code,))
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
        cur.execute("INSERT INTO facilities (common_name, fcode) VALUES (%s, %s)", (name, code,))
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
        cur.execute("SELECT * FROM assets WHERE tag=%s", (tag,))
        conn.commit()
        return (cur.fetchone() != None)


"""
Creates and inserts an asset into the database given the asset tag, description,
facility of storage, and its intake date. The asset is inserted into the assets
table as well as the asset_at table to keep track of the asset location and
intake date. Changes are made then committed to the database.

Args:
    tag - The asset's tag.
    desc - The asset's description.
    facility - The name of the facility the asset is stored at.
    date - The date the asset was stored at the facility.
Returns:
    None
"""
def create_asset(tag, desc, facility, date):
    with psycopg2.connect(dbname = dbname, host = dbhost, port = dbport) as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO assets (tag, description) VALUES (%s, %s)", (tag, desc,))
        conn.commit()
        cur.execute("SELECT facility_pk FROM facilities WHERE common_name=%s", (facility,))
        conn.commit()
        ffk = cur.fetchone()[0] #### TypeError: 'NoneType' object is not subscriptable
        cur.execute("SELECT asset_pk FROM assets WHERE tag=%s", (tag,))
        conn.commit()
        afk = cur.fetchone()[0]
        new_date = date_to_string(date)
        cur.execute("INSERT INTO asset_at (asset_fk, facility_fk, arrive_date) VALUES (%s, %s, %s)",
                (afk, ffk, new_date,))
        conn.commit()
        return None


"""
Checks the database to see if an asset was disposed given its tag. An asset is considered
disposed if it contains a departure date.

Args:
    tag - The tag of the asset to check.
Returns:
    True if the asset was disposed already, false if not.
"""
def asset_disposed(tag):
    with psycopg2.connect(dbname = dbname, host = dbhost, port = dbport) as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM assets WHERE tag=%s", (tag,))
        conn.commit()
        ident = cur.fetchone()[0]
        cur.execute("SELECT * FROM asset_at WHERE asset_fk=%s", (ident,))
        conn.commit()
        return (cur.fetchone()[4] != None)


"""
Disposes the asset from the system given the tag and the date the asset was disposed. The
changes are made and committed to the database.

Args:
    tag - The tag of the asset to dispose of.
    date - The date the asset will be disposed.
Returns:
    None
"""
def dispose(tag, date):
    with psycopg2.connect(dbname = dbname, host = dbhost, port = dbport) as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM assets WHERE tag=%s", (tag,))
        conn.commit()
        ident = cur.fetchone()[0]
        new_date = date_to_string(date)
        cur.execute("UPDATE asset_at SET depart_date=%s WHERE asset_fk=%s", (new_date, ident,))
        conn.commit()
        return None


"""
Generates and returns an asset report in the form of a list. The list generated
takes the form [(a1,b1,c1,d1,e1), (a2,b2,c2,d2,e2), ...] where a is the asset
tag, b is the asset description, c is the facility, d is the arrival date, and
e is the departure date. The list is generated filtered by the given facility
name and the arrival date.

Args:
    facility - The name of the facility to filter by.
    date - The date to filter by.
Returns:
    A list of tuplesthat represent the asset report.
"""
def generate_report(facility, date):
    with psycopg2.connect(dbname = dbname, host = dbhost, port = dbport) as conn:
        cur = conn.cursor()
        arrive_date = date_to_string(date)
        if (facility == "ALL"):
            cur.execute("SELECT * FROM asset_at WHERE arrive_date=%s", (arrive_date,))
            conn.commit()
        else:
            cur.execute("SELECT * FROM facilities WHERE facility_name=%s", (facility,))
            conn.commit()
            ffk = cur.fetchone()[0]
            cur.execute("SELECT * FROM asset_at WHERE facility_fk=%s AND arrive_date=%s", (ffk, arrive_date,))
            conn.commit()
        res = cur.fetchall()
        #report = [('A','B','C','D','E')]
        for asset in res:
            cur.execute("SELECT * FROM assets WHERE asset_pk=%s", (asset[1],))
            conn.commit()
            a_temp = cur.fetchone()
            cur.execute("SELECT * FROM facilities WHERE facility_pk=%s", (asset[2],))
            conn.commit()
            b_temp = cur.fetchone()[2]
            report.append((a_temp[1], a_temp[2], b_temp, asset[3], asset[4],))
        return report
