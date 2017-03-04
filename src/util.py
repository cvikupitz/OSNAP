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
Generates a random 20-character string used for the ID's of transfer requests.

Args:
    None
Returns:
    A random 20-character hex string.
"""
def generate_id():
    import os
    return (os.urandom(10).hex())



