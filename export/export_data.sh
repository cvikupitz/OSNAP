#!/usr/bin/bash

# export_data.sh
# Author: Cole Vikupitz

# Incorrect usage, display message, exit.
if [ "$#" -ne 2 ]; then
	echo "Usage: ./export_data.sh <dbname> <output_dir>"
	exit;
fi

# Creates the output directory
cd ~
mkdir $2

# Executes the exports
python3 export_users.py $1 $2
python3 export_facilities.py $1 $2
python3 export_assets.py $1 $2
python3 export_transfers.py $1 $2
