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
	role_pk				SERIAL PRIMARY KEY,
	title				varchar(36)
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
	facility_pk			SERIAL PRIMARY KEY,
	fcode				varchar(6),
	common_name			varchar(32)
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
	user_pk				SERIAL PRIMARY KEY,
	username			varchar(16) NOT NULL,
	password			varchar(16) NOT NULL,
	role				integer REFERENCES roles (role_pk)
);


/* This table holds data on an individual asset. All assets have a tag for identification
 * that can be up to 16 characters in length. Assets can also have an option description
 * for them, can be up to 80 characters in length. This table does not include pointers to
 * facilities that these assets are tracked at.
 *
 * asset_pk (PRIMARY KEY) - Primary key for the asset instance.
 * tag (varchar(16)) - The asset's identification tag, can be up to 16 characters in length.
 * description (varchar(80)) - A brief description of the asset, can be up to 80 characters.
 */
CREATE TABLE assets (
	asset_pk			SERIAL PRIMARY KEY,
	tag				varchar(16) NOT NULL,
	description			varchar(80)
);


/* This table holds data on assets stored at particular facilities. Each asset created must
 * be stored at a facility on a given date. These two variables are required when we create
 * an asset into the system. The departure date will be the date the asset is disposed of,
 * or when it leaves that facility.
 *
 * asset_at_pk (PRIMARY KEY) - Primary key for the instance.
 * asset_fk (integer) - Pointer to the asset being stored, from the assets table.
 * facility_fk (integer) - Pointer to the facility the asset is stored at, from the facilities table.
 * arrive_date (date) - The date the asset arrived at the facility.
 * depart_date (date) - The date the asset was disposed from the facility.
 */
CREATE TABLE asset_at (
	asset_at_pk			SERIAL PRIMARY KEY,
	asset_fk			integer REFERENCES assets (asset_pk),
	facility_fk			integer REFERENCES facilities (facility_pk),
	arrive_date			date,
	depart_date			date
);


/*
 * FIXME
 */
CREATE TABLE requests (
	request_pk			SERIAL PRIMARY KEY,
	requester			integer REFERENCES users (user_pk),
	approver			integer REFERENCES users (user_pk),
	submit_date			timestamp,
	approve_date			timestamp,
	src_facility			integer REFERENCES facilities (facility_pk),
	dest_facility			integer REFERENCES facilities (facility_pk),
	asset_pk			integer REFERENCES assets (asset_pk)
);


/*
 * FIXME
 */
CREATE TABLE in_transit (
	in_transit_pk			SERIAL PRIMARY KEY,
	asset_fk			integer REFERENCES assets (asset_pk),
	src_facility			integer REFERENCES facilities (facility_pk),
	dest_facility			integer REFERENCES facilities (facility_pk),
	load_time			timestamp,
	unload_time			timestamp
);

/* Inserts the 2 roles into the table. */
INSERT INTO roles (title) VALUES ('Logistics Officer');
INSERT INTO roles (title) VALUES ('Facilities Officer');
