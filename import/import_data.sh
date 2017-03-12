#!/usr/bin/bash

# import_data.sh
# Author: Cole Vikupitz

# Incorrect usage, display message, exit.
if [ "$#" -ne 2 ]; then
	echo "Usage: ./import_data.sh <dbname> <input_dir>"
	exit;
fi

# Executes the imports
python3 import_users.py $1 $2
python3 import_facilities.py $1 $2
python3 import_assets.py $1 $2
#python3 import_transfers.py $1 $2

