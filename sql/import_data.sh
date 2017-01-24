#!usr/bin/bash

# CIS 322 Assignment 2
# Author - Cole Vikupitz

# Use curl to download the legacy data, unpack file
curl -o osnap_legacy.tar.gz https://classes.cs.uoregon.edu//17W/cis322/files/osnap_legacy.tar.gz
tar -xjf osnap_legacy.tar.gz
cd osnap_legacy/
