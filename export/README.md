This directory contains files/scripts used for exporting data from the
L.O.S.T. database into a set of csv files. The files generated from exporting 
are: users.csv, facilities.csv, assets.csv, and transfers.csv.

Use the export_data.sh script to execute the export. The python files (.py) are
called by the script so you don't need to execute them on their own.

* export_data.sh  
Usage:  
`$ ./export_data.sh <dbname> <output_directory>`  
<dbname> - The name of the database used by L.O.S.T. to extract the data from.  
<output_directory> - The directory to export the files to. Creates the directory
		     if it does not exist, or overwrites all files in the
		     directory if it does.  
WARNING: It is recommended that you export to a new directory so that you do not
	 risk losing any other files/data on your computer.  

* directory.py - Creates the new directory, or overwrites the files inside the
		 directory if it already exists.
* export_assets.py - Exports the assets from the database to the file 'assets.csv'.
* export_facilities.py - Exports the facilities from the database to the file 'facilities.csv'.
* export_transfers.py - Exports the transfers from the database to the file 'transfers.csv'.
* export_users.py - Exports the users from the database to the file 'users.csv'.

```

...
|
|-- directory.py
|-- export_assets.py
|-- export_data.sh
|-- export_facilities.py
|-- export_transfers.py
|-- export_users.py
|

```