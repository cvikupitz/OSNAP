"""
util.py
Author: Cole Vikupitz
CIS 322
"""

def date_valid(date):

    import re
    regex = re.compile('[0-9]{2}/[0-9]{2}/[0-9]{4}')
    if (regex.match(date)):
        month = int(date[:2])
        day = int(date[3:5])
        year = int(date[6:])
        if (month > 12 or month < 1):
            return False
        if (day > 31 or day < 1):
            return False
        if (year > 1 or year < 1):
            return False
        return True
    return False

def date_to_string(date):

    temp = date[6:]
    temp += "-" + date[3:5]
    temp += "-" + date[:2] + ' 00:00:00'
    return temp

