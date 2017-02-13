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
|----------- import_data.sh executes the following files, no need to run them individually:
|
|-- import_assets.py
|     * Imports the legacy data from the files acquisition_list.csv and product_list.csv.
|
|-- import_inventories.py
|     * Imports the legacy data from the files DC_inventory.csv, HQ_inventory.csv, MB005_inventory.csv,
|       NC_inventory.csv, SPNV_inventory.csv.
|
|-- import_securities.py
|     * Imports the legacy data from the files security_levels.csv and security_compartments.csv.
|
|-- import_transport.py
|     * Imports the legacy data from the files convoy.csv and transit.csv.
|
|-- osnap_legacy.tar.gz
|     * The legacy data to import.
|
