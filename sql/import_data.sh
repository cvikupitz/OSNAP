#!usr/bin/bash

# CIS 322 Assignment 2
# Author - Cole Vikupitz

# Use curl to download the legacy data, unpack file
curl -o osnap_legacy.tar.gz https://classes.cs.uoregon.edu//17W/cis322/files/osnap_legacy.tar.gz
tar -xjf osnap_legacy.tar.gz

# Create database, use create_tables.sql to generate tables
psql --filename=create_tables.sql $1

# Run the python script to import the legacy data
python3 import_legacy.py $1 $2
