/*
 * create_tables.sql
 * Author: Cole Vikupitz
 * CIS 322
 *
 * Creates the data tables associated with the OSNAP data model.
 */


/* This table will hold all the possible roles a user can have. As of right now,
 * only 2 roles are possible which are 'logistics officer' and 'facilities officer',
 * each with different access levels to different components. This allows us to add
 * more roles into the application easily if we wanted to in the future.
 * 
 * role_pk (PRIMARY KEY) - The primary key for the role instance.
 * title (varchar(36)) - The title of the role (up to 36 characters in length), can
 *						 be 'Logistics Officer' or 'Facilities Officer'.
 */
CREATE TABLE roles (
	role_pk			SERIAL PRIMARY KEY,
	title			varchar(36)
);


/* This table will hold information on facilities. Each facility in our database will 
 * have a name and code for identification. The facilities will be used to keep track 
 * of where our assets are located via their primary key.
 *
 * facility_pk (PRIMARY KEY) - Primary key for the facility instance.
 * fcode (varchar(6)) - The code to identify the facility, can be up to 6 characters 
 *					    in length.
 * common_name (varchar(36)) - The name of the facility, can be up to 36 characters in
 *							   length.
 */
CREATE TABLE facilities (
	facility_pk		SERIAL PRIMARY KEY,
	fcode			varchar(6),
	common_name		varchar(32)
);


/* This table holds information on users that are in the system. All users have a username 
 * and password stored in their account, used for signing into the web application. In
 * addition, a role is also stored into each user, via by pointing to the key of one of
 * the roles inside the roles table by using a primary key.
 *
 * user_pk (PRIMARY KEY) - Primary key for the user instance.
 * username (varchar(16)) - The account username, up to 16 characters in length. 
 * password (varchar(16)) - The password of the account, up to 16 characters in length.
 * role (integer) - The role of the user. This points to the primary key of the role in
 *					the roles table that this user has.
 */
CREATE TABLE users (
	user_pk			SERIAL PRIMARY KEY,
	username		varchar(16) NOT NULL,
	password		varchar(16) NOT NULL,
	role			integer REFERENCES roles (role_pk)
);








CREATE TABLE assets (
	asset_pk		SERIAL PRIMARY KEY,
	tag				varchar(16),
	description		varchar(80)
);

CREATE TABLE asset_status (
	asset_status_pk		SERIAL PRIMARY KEY,
	asset_fk		integer REFERENCES assets (asset_pk),
	facility_fk		integer REFERENCES facilities (facility_pk),
	arrive_date		date,
	depart_date		date
);


/* Inserts the 2 roles into the table. */
INSERT INTO roles (title) VALUES ('Logistics Officer');
INSERT INTO roles (title) VALUES ('Facilities Officer');
