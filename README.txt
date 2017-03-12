Welcome to my repository for L.O.S.T.

=============== What is OSNAP? ===============

OSNAP is a project designed and implemented for a group of customers with specific requirements
on how they want to manage the assets in their business. This implementation is referred to as
L.O.S.T., whick keeps track of assets, facilities of storage, where assets are located, transfer
requests of assets between two facilities, and generating asset and transfer reports. All of these
features have been implemented based on these clients' requests and have helped made business
organization much easier for their company. The web application was designed and built over a ten
week course for CIS 322 at the University of Oregon.

=============== Installation ===============

To run the application, you will need to install postgres 9.5., and Apache httpd-2.4.25 or a later
version.

To install postgres, run the commands:

>> git clone https://github.com/postgres/postgres.git
>> cd postgres/
>> ./configure --prefix=$1
>> make
>> make install

where $1 is the install prefix.

To install Apache, run the commands:

>> curl -o httpd-2.4.25.tar.bz2 http://apache.mirrors.tds.net//httpd/httpd-2.4.25.tar.bz2
>> tar -xjf httpd-2.4.25.tar.bz2
>> cd httpd-2.4.25/
>> ./configure --prefix=$1
>> make
>> make install

where $1 is the install prefix.

To clone this repository, run the command:

>> git clone http://github.com/cvikupitz/OSNAP.git

=============== Running the Application ===============

First, create and start a database cluster on your machine with the following commands:

>> initdb -D $1
>> pg_ctl -D $1 -l logfile start

where $1 is the specified directory on your system to store the database.

Next, create the database by running:

>> createdb -p $1 $2

where $1 is the port number and $2 is the name of the database.

Finally, change into the OSNAP directory and run the preflight script by running:

>> ./preflight.sh $1

where $1 is the name of the database you created.

Open your browser and go to http://127.0.0.1:8080 to use the web application.


=============== Repository Directories/Contents ===============

* doc/ - This sub-directory contains documentation on the design/implementation L.O.S.T.
* export/ - This sub-directory contains a script to run for exporting data from your database.
* import/ - This sub-directory contains a script to run for importing data into your database.
* lectures/ - This sub-directory contains files/notes from the CIS 322 class page.
* sql/ - This sub-directory contains SQL scripts used to generate tables in the database.
* src/ - This sub-directory contains source files for the L.O.S.T. application.
* preflight.sh
Usage: ./preflight.sh <dbname>
<dbname> - The name of the database for L.O.S.T. to use.

...
|
|-- doc/
|    |
|    |-- assignment1.pdf
|    |-- assignment2.pdf
|    |-- assignment3.pdf
|    |-- assignment4.pdf
|    |-- assignment5.pdf
|    |-- assignment6.pdf
|    |-- assignment7.pdf
|    |-- assignment8.pdf
|    |-- assignment9.pdf
|    |-- assignment10.pdf
|    |-- derp_req.pdf
|    |-- lost_req.pdf
|    |-- rubric.pdf
|    |-- who_req.pdf
|
|-- export/
|    |
|    |-- directory.py
|    |-- export_assets.py
|    |-- export_data.sh
|    |-- export_facilities.py
|    |-- export_transfers.py
|    |-- export_users.py
|
|-- import/
|    |
|    |-- import_assets.py
|    |-- import_data.sh
|    |-- import_facilities.py
|    |-- import_transfers.py
|    |-- import_users.py
|
|-- lectures/
|    |
|    |-- < Lecture slides & notes are here. >
|
|-- sql/
|    |
|    |-- create_tables.sql
|
|-- src/
|    |
|    |-- static/
|    |    |
|    |    |-- add_asset_icon.png
|    |    |-- add_facility_icon.png
|    |    |-- alien_icon.png
|    |    |-- asset_report_icon.png
|    |    |-- checkmark.png
|    |    |-- dashboard_icon.png
|    |    |-- dispose_asset_icon.png
|    |    |-- password_icon.png
|    |    |-- stop.png
|    |    |-- transfer_report_icon.png
|    |    |-- transfer_request_icon.png
|    |    |-- user_icon.png
|    |
|    |-- templates/
|    |    |
|    |    |-- add_asset.html
|    |    |-- add_facility.html
|    |    |-- approve_req.html
|    |    |-- asset_report.html
|    |    |-- create_user.html
|    |    |-- dashboard.html
|    |    |-- dispose_asset.html
|    |    |-- error.html
|    |    |-- login.html
|    |    |-- logout.html
|    |    |-- message.html
|    |    |-- transfer_report.html
|    |    |-- transfer_req.html
|    |    |-- update_transit.html
|    |
|    |-- app.py
|    |-- config.py
|    |-- lost_config.json
|    |-- psql.py
|    |-- util.py
|
|-- preflight.sh
|
