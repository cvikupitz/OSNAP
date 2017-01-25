Contains script files that create/manage the DERP databases.

...
|
|-- create_tables.sql
|     * SQL script that creates the data tables that is associated with the data model decribed in 
|       the lost requirements document found in lost_req.pdf.
|
|-- import_data.sh
|     * Bash script that imports the OSNAP legacy data into the newly created database. Uses curl to
|       download the archive, unzips it, then moves all the data into the appropriate locations.
|       Usage:
|         >> ./ import_data [database_name] [port_number]
|
|-- import_legacy.py
|     * Python program that will install the legacy data into the database into the best fit areas
|       decided.
|
