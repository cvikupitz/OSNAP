"""
util.py
Author: Cole Vikupitz

File with helper functions used in the L.O.S.T. web application.
"""


"""
Scans the given date and returns true/false if the date is in the correct format.
The correct format is MM/DD/YYYY, where months/days with single digits are not
allowed (i.e. January usually would be 1, but it must be 01).

Args:
    date - The date string to scan.
Returns:
    True if the date is in the format MM/DD/YYYY, false if not.
"""
def date_valid(date):

    import re
    regex = re.compile('[0-9]{2}/[0-9]{2}/[0-9]{4}')
    if (regex.match(date)):
        month = int(date[:2])
        day = int(date[3:5])
        year = int(date[6:])
        if (month < 1 or month > 12):
            return False
        if (day < 1 or day > 31):
            return False
        if (year < 1 or year > 9999):
            return False
        return True
    return False


"""
Converts the given date string into a different format to be passed into
the SQL server as a Date object. The given date is expected to be in the
format MM/DD/YYYY. The string returned is the date in the format
'YYYY-MM-DD 00:00:00'.

Args:
    date - The date string to convert.
Returns:
    A new date string in the format 'YYYY-MM-DD 00:00:00'.
"""
def date_to_string(date):

    temp = date[6:]
    temp += '-' + date[:2]
    temp += '-' + date[3:5]
    temp += ' 00:00:00'
    return temp


"""
Generates a random 16-character string used for the ID's of transfer requests.

Args:
    None
Returns:
    A random 16-character hex string.
"""
def generate_id():
    import os
    return (os.urandom(10).hex())
