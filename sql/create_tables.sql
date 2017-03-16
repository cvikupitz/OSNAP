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
 * active - True if the user can sign in, false if not.
 */
CREATE TABLE users (
	user_pk				SERIAL PRIMARY KEY,
	username			varchar(16) NOT NULL,
	password			varchar(16) NOT NULL,
	role				integer REFERENCES roles (role_pk),
	active				boolean
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
	tag					varchar(16) NOT NULL,
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
 * arrive_date (varchar(10)) - The date the asset arrived at the facility.
 * depart_date (varchar(10)) - The date the asset was disposed from the facility.
 */
CREATE TABLE asset_at (
	asset_at_pk			SERIAL PRIMARY KEY,
	asset_fk			integer REFERENCES assets (asset_pk),
	facility_fk			integer REFERENCES facilities (facility_pk),
	arrive_date			varchar(10),
	depart_date			varchar(10)
);


/*
 * This table holds information on transfer requests made by logistics officers. A request has
 * a pointer to the asset being transferred, a source, and a destination facility. This information
 * is set manually by the officer when making the request. A stamp is randomly generated to
 * identify each transfer, which will be a link on any facilities officer's dashboard to go and
 * approve/decline that request. Also contains a column for the user who made the request and a
 * timestamp of when it was made. When a facilities officer approves the request, they are
 * inserted into the table as the approver, and the time the request was approved is added as well.
 * If the request is declined, then it will be dropped from the database. Once the request is
 * approved, the stamp id will then appear in the logistics officer's dashboard as a link to go
 * and manually set the date and time of when the asset is loaded and unloaded.
 *
 * request_pk (PRIMARY KEY) - Primary key for the request instance.
 * id_stamp (varchar(20)) - A 20-character identification string for the request.
 * requester (integer) - Pointer to the user who submitted the request.
 * approver (integer) - Pointer to the user who approved the request.
 * submit_date (timestamp) - Date & time the request was submitted.
 * approve_date (timestamp) - Date & time the request was approved.
 * src_facility (integer) - Pointer to the facility where the asset is transferred from.
 * dest_facility (integer) - Pointer to the facility where the asset is transferred to.
 * asset_fk (integer) - Pointer to the asset being transferred.
 * load_time (timestamp) - Date & time the asset was loaded.
 * unload_time (timestamp) - Date & time the asset was unloaded.
 */
CREATE TABLE requests (
	request_pk			SERIAL PRIMARY KEY,
	id_stamp			varchar(20),
	requester			integer REFERENCES users (user_pk),
	approver			integer REFERENCES users (user_pk),
	submit_date			timestamp,
	approve_date		timestamp,
	src_facility		integer REFERENCES facilities (facility_pk),
	dest_facility		integer REFERENCES facilities (facility_pk),
	asset_fk			integer REFERENCES assets (asset_pk),
	load_time			timestamp,
	unload_time			timestamp
);


/* Inserts the 2 roles into the table. */
INSERT INTO roles (title) VALUES ('Logistics Officer');
INSERT INTO roles (title) VALUES ('Facilities Officer');


-------------------------------------------------
/* TESTING - COMMENT OUT WHEN COMPLETE */
/*
INSERT INTO users (username, password, role, active) VALUES ('user1', 'p1', '1', 'TRUE');
INSERT INTO users (username, password, role, active) VALUES ('user2', 'p2', '2', 'TRUE');
INSERT INTO users (username, password, role, active) VALUES ('user3', 'p3', '1', 'FALSE');
INSERT INTO facilities (fcode, common_name) VALUES ('WLGRNS', 'Wallgreens');
INSERT INTO facilities (fcode, common_name) VALUES ('TARGET', 'Target');
INSERT INTO facilities (fcode, common_name) VALUES ('NRDSTM', 'Nordstrom');
INSERT INTO facilities (fcode, common_name) VALUES ('MRCDES', 'Mercedes');
INSERT INTO assets (tag, description) VALUES ('AA1', 'Prescription pills.');
INSERT INTO assets (tag, description) VALUES ('AA2', 'Greeting cards.');
INSERT INTO assets (tag, description) VALUES ('AA3', 'Medicine.');
INSERT INTO assets (tag, description) VALUES ('AA4', 'Bell Peppers.');
INSERT INTO assets (tag, description) VALUES ('BB1', 'HDTV.');
INSERT INTO assets (tag, description) VALUES ('BB2', 'Samsung Galaxy.');
INSERT INTO assets (tag, description) VALUES ('BB3', 'DVD Player.');
INSERT INTO assets (tag, description) VALUES ('BB4', 'Macbook Pro.');
INSERT INTO assets (tag, description) VALUES ('CC1', 'Dress socks.');
INSERT INTO assets (tag, description) VALUES ('CC2', 'Collared shirts.');
INSERT INTO assets (tag, description) VALUES ('CC3', 'Dress shoes.');
INSERT INTO assets (tag, description) VALUES ('CC4', 'Under armour.');
INSERT INTO assets (tag, description) VALUES ('DD1', 'Car C230.');
INSERT INTO assets (tag, description) VALUES ('DD2', 'Engine V3.');
INSERT INTO assets (tag, description) VALUES ('DD3', 'Car seats.');
INSERT INTO assets (tag, description) VALUES ('DD4', 'Fluffy dice.');
INSERT INTO asset_at (asset_fk, facility_fk, arrive_date) VALUES ('1','1','01/01/2000');
INSERT INTO asset_at (asset_fk, facility_fk, arrive_date) VALUES ('2','1','01/01/2000');
INSERT INTO asset_at (asset_fk, facility_fk, arrive_date) VALUES ('3','1','01/02/2000');
INSERT INTO asset_at (asset_fk, facility_fk, arrive_date) VALUES ('4','1','01/02/2000');
INSERT INTO asset_at (asset_fk, facility_fk, arrive_date) VALUES ('5','2','02/01/2000');
INSERT INTO asset_at (asset_fk, facility_fk, arrive_date) VALUES ('6','2','02/01/2000');
INSERT INTO asset_at (asset_fk, facility_fk, arrive_date) VALUES ('7','2','02/02/2000');
INSERT INTO asset_at (asset_fk, facility_fk, arrive_date) VALUES ('8','2','02/02/2000');
INSERT INTO asset_at (asset_fk, facility_fk, arrive_date) VALUES ('9','3','01/02/2000');
INSERT INTO asset_at (asset_fk, facility_fk, arrive_date) VALUES ('10','3','01/02/2000');
INSERT INTO asset_at (asset_fk, facility_fk, arrive_date) VALUES ('11','3','01/03/2000');
INSERT INTO asset_at (asset_fk, facility_fk, arrive_date) VALUES ('12','3','01/03/2000');
INSERT INTO asset_at (asset_fk, facility_fk, arrive_date) VALUES ('13','4','01/01/2000');
INSERT INTO asset_at (asset_fk, facility_fk, arrive_date) VALUES ('14','4','01/02/2000');
INSERT INTO asset_at (asset_fk, facility_fk, arrive_date) VALUES ('15','4','01/03/2000');
INSERT INTO asset_at (asset_fk, facility_fk, arrive_date) VALUES ('16','4','01/04/2000');
INSERT INTO requests (id_stamp, requester, approver, submit_date, approve_date, src_facility, dest_facility, asset_fk, load_time, unload_time) VALUES ('1cdcc65d73aa2902947a','1','2','03/12/2014','03/12/2014','1','2','1','01/01/2002 12:00:00','01/20/2002 13:00:00');
INSERT INTO requests (id_stamp, requester, approver, submit_date, approve_date, src_facility, dest_facility, asset_fk, load_time, unload_time) VALUES ('9030bdac88f7b1203412','1','2','03/13/2014','03/14/2014','1','3','3','01/06/2002 10:45:00','01/31/2002 13:10:00');
INSERT INTO requests (id_stamp, requester, approver, submit_date, approve_date, src_facility, dest_facility, asset_fk, load_time, unload_time) VALUES ('550da86eb0e684eb00d3','1','2','03/13/2014','03/14/2014','3','2','7','01/10/2002 09:30:00','02/01/2002 07:45:00');
INSERT INTO requests (id_stamp, requester, approver, submit_date, approve_date, src_facility, dest_facility, asset_fk, load_time, unload_time) VALUES ('95aec9bd166d78216134','1','2','03/14/2014','03/14/2014','2','3','10','02/08/2002 15:00:00','02/19/2002 11:35:00');
INSERT INTO requests (id_stamp, requester, approver, submit_date, approve_date, src_facility, dest_facility, asset_fk, load_time, unload_time) VALUES ('6944e3d472f7e3564a65','1','2','03/15/2014','03/16/2014','4','3','12','02/12/2002 17:00:00','03/03/2002 12:30:00');
INSERT INTO requests (id_stamp, requester, approver, submit_date, approve_date, src_facility, dest_facility, asset_fk, load_time, unload_time) VALUES ('0435a71d628677fd4dca','1','2','03/15/2014','03/17/2014','4','1','15','03/01/2002 10:20:00','04/01/2002	016:45:00');
*/

