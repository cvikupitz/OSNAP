/*
create_tables.sql
Author: Cole Vikupitz
CIS 322 Assignment 6
------------------------------------------------------------
Creates the tables associated with the OSNAP data model.
*/


/* This table will contain user information, which will include their user name and password. */
CREATE TABLE users (

	/* 
	The primary key will be used to create an ordered list of all the users. Not used for the username, as the 
	primary key may come in handy for other functions later. 
	*/
	user_pk		SERIAL PRIMARY KEY,
	
	/*
	The username will not be longer than 16 characters, so a variable length string of 16 will be used for 
	the username.
	*/
	username	varchar(16) NOT NULL,
	
	/*
	The password will also not be longer than 16 characters, so again a variable length string of 16 will 
	also be used for the password.
	*/
	password	varchar(16) NOT NULL

);


CREATE TABLE roles ();

CREATE TABLE assets ();

CREATE TABLE facilities ();

