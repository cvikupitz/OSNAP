This directory contains files/scripts used for importing data from a
set of files from a specified directory into a database. The files that
are expected in the directory are: users.csv, facilities.csv, assets.csv, 
and transfers.csv.

Use the import_data.sh script to execute the import. The python files (.py) are
called by the script so you don't need to execute them on their own.

* import_data.sh  
Usage:  
`$ ./import_data.sh <dbname> <input_directory>`  
<dbname> - The name of the database used by L.O.S.T. to import the data into.  
WARNING: It is recommended that you import to a new database so that you do not
	 risk importing any duplicated data.  
<input_directory> - The directory to import the files from.  

* import_assets.py - Exports the assets from the file 'assets.csv' to the database.
* import_facilities.py - Exports the assets from the file 'facilities.csv' to the database.
* import_transfers.py - Exports the assets from the file 'transfers.csv' to the database.
* import_users.py - Exports the assets from the file 'users.csv' to the database.

```

...
|
|-- import_assets.py
|-- import_data.sh
|-- import_facilities.py
|-- import_transfers.py
|-- import_users.py
|

```