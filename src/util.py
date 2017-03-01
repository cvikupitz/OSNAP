"""
util.py
Author: Cole Vikupitz
CIS 322
"""

def date_valid(date):

    """

    """
    import re
    regex = re.compile('[0-9]{4}-[0-9]{2}-[0-9]{2}')
    return regex.match(date)


