This directory contains source files used for starting/running the application.
Files invoked in this directory are done so during the program's launch and
during execution.

* static/ - This sub-directory contains static files used for the application.
* templates/ - This sub-directory contains template files (HTML) used by the 
	       web application.
* app.py - The Flask source file that runs the web application. Can be run by itself,
	   but is run by the preflight script in the home directory.
* config.py - File used to read the L.O.S.T. configuration file from a JSON file into
	      a wsgi directory.
* psql.py - File that holds a library of PSQL functions used for adding, accessing, and
	    modifying data in the L.O.S.T. database.
* util.py - File that contains a collection of other useful functions used by the web
	    application.

...
|
|-- static/
|-- templates/
|-- app.py
|-- config.py
|-- psql.py
|-- util.py
|
