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
        cur.execute("SELECT username FROM USERS WHERE username=%s AND password=%s",
                    (uname, password,))
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
        cur.execute("INSERT INTO users (username, password, role) VALUES (%s, %s, %s)",
                    (uname, password, role,))
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
Returns the primary key associated with the user from the database given the username.

Args:
    uname - The user's username.
Returns:
    The primary key of the account, or None if the account does not exist.
"""
def get_user_pk(uname):
    with psycopg2.connect(dbname = dbname, host = dbhost, port = dbport) as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username=%s", (uname,))
        conn.commit()
        return (cur.fetchone()[0])


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
        cur.execute("SELECT r.title FROM roles r JOIN users u ON r.role_pk=u.role WHERE u.username=%s",
                    (uname,))
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
Returns the primary key of the facility from the database given the common name.

Args:
    name - The common name of the facility.
Returns:
    The facility's primary key, or None if the facility does not exist.
"""
def get_facility_pk(name):
    with psycopg2.connect(dbname = dbname, host = dbhost, port = dbport) as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM facilities WHERE common_name=%s", (name,))
        conn.commit()
        return (cur.fetchone()[0])


"""
Creates and inserts a new facility instance into the database given the facility
common name and its 6-digit identification code. Changes are committed to the
database.

Args:
    code - The facility's identification code.
    name - The facility's common name.
Returns:
    None
"""
def create_facility(code, name):
    with psycopg2.connect(dbname = dbname, host = dbhost, port = dbport) as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO facilities (fcode, common_name) VALUES (%s, %s)",
                    (code, name,))
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
Returns the primary key associated with the given asset tag.

Args:
    tag - The asset tag.
Returns:
    The primary key of the asset, or None if the asset does not exist.
"""
def get_asset_pk(tag):
    with psycopg2.connect(dbname = dbname, host = dbhost, port = dbport) as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM assets WHERE tag=%s", (tag,))
        conn.commit()
        return (cur.fetchone()[0])


"""
Creates and inserts an asset into the database given the asset tag, description,
facility of storage, and its intake date. The asset is inserted into the assets
table as well as the asset_at table to keep track of the asset location and
intake date. Changes are made then committed to the database.

Args:
    tag - The asset's tag.
    desc - The asset's description.
    facility - The common name of the facility the asset is stored at.
    date - The date the asset was stored at the facility.
Returns:
    None
"""
def create_asset(tag, desc, facility, date):
    with psycopg2.connect(dbname = dbname, host = dbhost, port = dbport) as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO assets (tag, description) VALUES (%s, %s)", (tag, desc,))
        conn.commit()
        ffk = get_facility_pk(facility) # NoneType Error Here.......
        afk = get_asset_pk(tag)
        cur.execute("INSERT INTO asset_at (asset_fk, facility_fk, arrive_date) VALUES (%s, %s, %s)",
                (afk, ffk, date,))
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
        cur.execute("UPDATE asset_at SET depart_date=%s WHERE asset_fk=%s", (date, ident,))
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
        if (facility == "ALL"):
            cur.execute("SELECT * FROM asset_at WHERE arrive_date=%s", (date,))
            conn.commit()
        else:
            cur.execute("SELECT * FROM facilities WHERE common_name=%s", (facility,))
            conn.commit()
            ffk = cur.fetchone()[0]     # NoneType Error
            cur.execute("SELECT * FROM asset_at WHERE facility_fk=%s AND arrive_date=%s", (ffk, date,))
            conn.commit()
        res = cur.fetchall()
        report = list() #### STILL NEEDS FIXING...
        for asset in res:
            cur.execute("SELECT * FROM assets WHERE asset_pk=%s", (asset[1],))
            conn.commit()
            a_temp = cur.fetchone()
            cur.execute("SELECT * FROM facilities WHERE facility_pk=%s", (asset[2],))
            conn.commit()
            b_temp = cur.fetchone()[2]
            report.append((a_temp[1], a_temp[2], b_temp, asset[3], asset[4],))
        return report


"""
Inserts a request into the database. A request submission contains the asset
tag, a source and destination facility, and the user submitting the request.
The request is then sent and committed into the database for facility officers
to approve/decline.

Args:
    user - The user submitting the request.
    src - The source facility.
    dest - The destination facility.
    tag - The asset tag.
Returns:
    None
"""
def add_request(user, src, dest, tag):
    with psycopg2.connect(dbname = dbname, host = dbhost, port = dbport) as conn:
        cur = conn.cursor()
        stamp = generate_id()
        user_fk = get_user_pk(user)
        src_fk = get_facility_pk(src)
        dest_fk = get_facility_pk(dest)
        asset_fk = get_asset_pk(tag)
        cur.execute("INSERT INTO requests (id_stamp, requester, submit_date, src_facility, dest_facility, asset_fk)\
                        VALUES (%s, %s, NOW(), %s, %s, %s)", (stamp, user_fk, src_fk, dest_fk, asset_fk,))
        conn.commit()
        return None


"""
Returns a list of all the pending transfer requests currently in the database. A pending request
is a request that has been made by a logistics officer, but has not yet been approved by a
facility officer.

Args:
    None
Returns:
    A list of all the pending transfer requests from the requests table that need approval from
    a facility officer.
"""
def get_pending_requests():
    with psycopg2.connect(dbname = dbname, host = dbhost, port = dbport) as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM requests WHERE approver IS NULL")
        conn.commit()
        return (cur.fetchall())


"""
Returns a list of all the approved requests from the database that need loading and unloading
timestamps set by a logistics officer.

Args:
    None
Returns:
    A list of all the transfer requests approved, but not yet completed.
"""
def get_approved_requests():
    with psycopg2.connect(dbname = dbname, host = dbhost, port = dbport) as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM requests WHERE approver IS NOT NULL") ### FIXME - NOT INCLUDE COMPLETED
        conn.commit()
        return (cur.fetchall())



##############
if __name__ == "__main__":
    li = generate_report('ALL', '01/02/2000') ## TESTING
    print("----")
    print(li)
