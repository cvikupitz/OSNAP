# config.py
# Author: Cole Vikupitz
# CIS 322 Assignment 6
# File is modified & borrowed from dellswor

# Imports
import json
import os
import pathlib

cpath = pathlib.Path(os.path.realpath(__file__)).parent.joinpath('lost_config.json')

with cpath.open() as conf:

    c = json.load(conf)

    dbname = c['database']['dbname']
    dbhost = c['database']['dbhost']
    dbport = c['database']['dbport']

print(dbname)
print(dbhost)
print(dbport)
