/*
create_tables.sql
Author: Cole Vikupitz
CIS 322
------------------------------------------------------------
Creates the tables associated with the OSNAP data model.
*/


/* This table will contain user information, which will include their user name, password, and role. */
CREATE TABLE users (

	/* 
	The primary key will be used to create an ordered list of all the users. Not used for the username, as the 
	primary key may come in handy for other functions later. 
	*/
	user_pk			SERIAL PRIMARY KEY,
	
	/*
	The username will not be longer than 16 characters, so a variable length string of 16 will be used for 
	the username.
	*/
	username		varchar(16) NOT NULL,
	
	/*
	The password will also not be longer than 16 characters, so again a variable length string of 16 will 
	also be used for the password.
	*/
	password		varchar(16) NOT NULL,
	
	/*
	The role of the user will be a number corresponding with the role primary key. We will just have a pre-set
	table of roles and each user will point to one of the roles in the table. Should eliminate redundancy and make
	it easy to add new roles if needed.
	*/
	role			integer

);


/* This table holds information on user roles. Contains a key representing a role and a name for that role. */
CREATE TABLE roles (
	
	/* 
	The primary key for the role, used for sorting/accessing different roles from the table. The user will reference
	this key for their role.
	*/
	role_pk			SERIAL PRIMARY KEY,

	/* The name of the role. */
	name			varchar(36)
	
);


/* This table contains information on assets, including their tags and descriptions. */
CREATE TABLE assets (

	/* The primary key used for sorting/accessing assets from the table. */
	asset_pk		SERIAL PRIMARY KEY,

	/* A tag for the asset, up to 16 characters in length. */
	tag			varchar(16),

	/* A small description of the asset, can be up to 80 characters in length. */
	description		varchar(80)

);


/* This table holds information on facilities. Includes data such as the facility common name and its 6-digit code. */
CREATE TABLE facilities (

	/* Primary key used for the facilities, used for accessing facilities from the table. */
	facility_pk		SERIAL PRIMARY KEY,

	/* The name of the facility, up to 32 characters in length. */
	common_name		varchar(32),

	/* A code, up to 6 characters, for the facility. */
	code			varchar(6)
);

INSERT INTO roles (name) VALUES ('Logistics Officer');
INSERT INTO roles (name) VALUES ('Facilities Officer');

