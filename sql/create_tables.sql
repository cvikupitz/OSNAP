/*
create_tables.sql
CIS 322 Assignment 2
Author - Cole Vikupitz
-----------------------------------------------------------------------
Creates the tables associated with the OSNAP data model.
*/

CREATE TABLE products (
	product_pk
	vendor				TEXT,
	description			TEXT,
	alt_description		TEXT
);

CREATE TABLE assets (
	asset_pk
	product_fk
	asset_tag			TEXT,
	description			TEXT,
	alt_description		TEXT
);

CREATE TABLE vehicles(
	vehicle_pk
	asset_fk
);

CREATE TABLE facilities (
	facility_pk
	fcode				TEXT,
	common_name			TEXT,
	location			TEXT
);

CREATE TABLE asset_at (
	asset_fk
	facility_fk
	arrive_dt			TIMESTAMP,		
	depart_dt			TIMESTAMP
);

CREATE TABLE convoys (
	convoy pk
	request				TEXT,
	source_fk
	dest_fk
	depart_dt			TIMESTAMP,
	arrive_dt			TIMESTAMP
);

CREATE TABLE used_by (
	vehicle_fk
	convoy_fk
);

CREATE TABLE asset_on (
	asset_fk
	convoy_fk
	load_dt				TIMESTAMP,
	unload_dt			TIMESTAMP
);

CREATE TABLE users (
	user_pk
	username			TEXT,
	active				BOOLEAN
);

CREATE TABLE roles (
	role_pk
	title				TEXT
);

CREATE TABLE user_is (
	user_fk
	role_fk
);

CREATE TABLE user_supports (
	user_fk
	facility_fk
);

CREATE TABLE levels (
	level_pk
	abbrv				TEXT,
	comment				TEXT
);

CREATE TABLE compartments (
	compartment_pk
	abbrv				TEXT,
	comment				TEXT
);

CREATE TABLE security_tags (
	tag_pk
	level_fk
	compartment_fk
	user_fk
	product_fk
	asset_fk
);
