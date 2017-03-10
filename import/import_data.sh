#!/usr/bin/bash

# import_data.sh
# Author: Cole Vikupitz

# Incorrect usage, display message, exit.
if [ "$#" -ne 1 ]; then
	echo "Usage: ./import_data.sh <dbname> <input_dir>"
	exit;
fi
