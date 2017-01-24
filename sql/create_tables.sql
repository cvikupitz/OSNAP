/*
create_tables.sql
CIS 322 Assignment 2
Author - Cole Vikupitz
-----------------------------------------------------------------------
Creates the tables associated with the OSNAP data model.
*/

CREATE TABLE products (
	product_pk
	vendor
	description
	alt_description
);

CREATE TABLE assets (
	asset_pk
	product_fk
	asset_tag
	description
	alt_description
);

CREATE TABLE vehicles(
	vehicle_pk
	asset_fk
);

CREATE TABLE facilities (
	facility_pk
	fcode
	common_name
	location
);

CREATE TABLE asset_at (
	asset_fk
	facility_fk
	arrive_dt
	depart_dt
);

CREATE TABLE convoys (
	convoy pk
	request
	source_fk
	dest_fk
	depart_dt
	arrive_dt
);

CREATE TABLE used_by (
	vehicle_fk
	convoy_fk
);

CREATE TABLE asset_on (
	asset_fk
	convoy_fk
	load_dt
	unload_dt
);

CREATE TABLE users (
	user_pk
	username
	active
);

CREATE TABLE roles (
	role_pk
	title
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
	level_pk integer primary key for security level lookups
	abbrv
	comment
);

CREATE TABLE compartments (
	compartment_pk
	abbrv
	comment
);

CREATE TABLE security_tags (
	tag_pk
	level_fk
	compartment_fk
	user_fk
	product_fk
	asset_fk
);
