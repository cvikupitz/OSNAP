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
    if (regex.match(date)):
        return True
    return False

if __name__ == "__main__":
    print(date_valid('1999-12-12'))
    print(date_valid('2222-33-23'))
    print(date_valid('33-12-12'))
    print(date_valid('199-12-12'))
    print(date_valid('1999-12w-12'))
