#!/usr/bin/bash

# preflight.sh
# Author: Cole Vikupitz
# CIS 322 Assignment 6
# File borrowed from dellswor

# Incorrect usage, display message, exit.
if [ "$#" -ne 1 ]; then
	echo "Usage: ./preflight.sh <dbname>"
	exit;
fi

# Create the database
cd sql/
psql $1 -f create_tables.sql
cd ..

# Install the wsgi files
cp -R src/* $HOME/wsgi

