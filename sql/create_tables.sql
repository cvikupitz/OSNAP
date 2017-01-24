/*
create_tables.sql
CIS 322 Assignment 2
Author - Cole Vikupitz
-----------------------------------------------------------------------
Creates the tables associated with the OSNAP data model.
*/

/* Asset Tables */
CREATE TABLE products (
	product_pk			SERIAL PRIMARY KEY,	-- primary key for a product instance
	vendor				TEXT,				-- who sells this product
	description			TEXT,				-- desc of the asset
	alt_description		TEXT				-- alt desc of the asset
);

CREATE TABLE assets (
	asset_pk			SERIAL PRIMARY KEY, -- primary key for an asset instance
	product_fk	-- id for the product instance the asset was spawned from
	asset_tag			TEXT,				-- stick or engraved id used for inventory tracking
	description			TEXT,				-- desc of the asset
	alt_description		TEXT				-- alt desc of the asset
);

CREATE TABLE vehicles (
	vehicle_pk			SERIAL PRIMARY KEY,	-- primary key for a vehicle instance
	asset_fk	-- id for the associated asset record
);

CREATE TABLE facilities (
	facility_pk			SERIAL PRIMARY KEY,	-- primary key for a facility instance
	fcode				VARCHAR(6),			-- code to id the facility (6> chars)
	common_name			TEXT,				-- common name for facility
	location			TEXT				-- addressing info for facility
);

CREATE TABLE asset_at (
	asset_fk	-- asset at a facility
	facility_fk	-- facility the asset is at
	arrive_dt			TIMESTAMP,	-- when the asset arrived
	depart_dt			TIMESTAMP	-- when the asset left
);

CREATE TABLE convoys (
	convoy pk			SERIAL PRIMARY KEY,	-- primary key for a convoy instance
	request				TEXT,	-- request id for the convoy
	source_fk	-- source facility				
	dest_fk		-- dest facility
	depart_dt			TIMESTAMP,	-- when the asset left
	arrive_dt			TIMESTAMP	-- when the asset arrived
);

CREATE TABLE used_by (
	vehicle_fk	-- vehicle participating in a convoy
	convoy_fk	-- convoy vehicles participate in
);

CREATE TABLE asset_on (
	asset_fk		-- asset at a facility
	convoy_fk		-- convoy the asset is on
	load_dt				TIMESTAMP,	-- when the asset was loaded
	unload_dt			TIMESTAMP	-- when the asset was unloaded
);

/* User Tables */
CREATE TABLE users (
	user_pk				SERIAL PRIMARY KEY,	-- primary key for a user instance
	username			TEXT,		-- login name used by the user
	active				BOOLEAN		-- is the user active?
);

CREATE TABLE roles (
	role_pk				SERIAL PRIMARY KEY,	-- primary key for a role instance
	title				TEXT				-- short textual name for the role
);

CREATE TABLE user_is (
	user_fk		-- id for the user instance
	role_fk		-- id for the role instance
);

CREATE TABLE user_supports (
	user_fk		-- id for the user instance
	facility_fk		-- id for the facility instance
);

/* Security Tables */
CREATE TABLE levels (
	level_pk			SERIAL PRIMARY KEY,	-- primary key for security level lookups
	abbrv				TEXT,				-- abbr for the security levels
	comment				TEXT				-- comment, if any
);

CREATE TABLE compartments (
	compartment_pk		SERIAL PRIMARY KEY,	-- primary key for compartment lookups
	abbrv				TEXT,				-- abbr for the security compartment
	comment				TEXT				-- comment, if any
);

CREATE TABLE security_tags (
	tag_pk				SERIAL PRIMARY KEY,	-- primary key for security tag instance
	level_fk	-- id for the tag level
	compartment_fk	-- id for the tag compartment
	user_fk		-- user the tag is applied to or NULL
	product_fk	-- product the tag is applied to or NULL
	asset_fk	-- asset the tag is applied to or NULL
);
