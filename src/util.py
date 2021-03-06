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
    limit = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (regex.match(date)):
        month = int(date[:2])
        day = int(date[3:5])
        year = int(date[6:])
        if (month < 1 or month > 12):
            return False
        if (day < 1 or day > limit[month]):
            return False
        if (year < 1 or year > 9999):
            return False
        return True
    return False


"""
Scans the given time and returns true/false if the time is in the correct format.
The correct format is HH:MM:SS.

Args:
    date - The time string to scan.
Returns:
    True if the time is in the format HH:MM:SS, false if not.
"""
def time_valid(time):
    import re
    regex = re.compile('[0-9]{2}:[0-9]{2}:[0-9]{2}')
    if (regex.match(time)):
        hour = int(time[:2])
        minute = int(time[3:5])
        sec = int(time[6:])
        if (hour < 0 or hour > 23):
            return False
        if (minute < 0 or minute > 59):
            return False
        if (sec < 0 or sec > 59):
            return False
        return True
    return False


"""
Scans a datetime object and returns a string representation of the given time
in the format MM/DD/YYYY  HH:MM A.M./P.M.
Used for displaying the date/time in the web application.

Args:
    time - The datetime object to convert.
Returns:
    A string representation of the given datetime object.
"""
def time_to_string(time):
    return time.strftime('%m/%d/%Y  %I:%M %p')


"""
Scans the datetime object and returns a string representation of the given date
in the format MM/DD/YYYY. Used for displaying the date in the reports.

Args:
    date - The datetime object to convert.
Returns:
    A string representation of the given date object.
"""
def date_to_string(date):
    try:
        return date.strftime('%m/%d/%Y')
    except:
        return 'None'


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

