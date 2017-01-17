#!usr/bin/bash

# CIS 322 Assignment 1
# Author - Cole Vikupitz

# 1.) clone the postgres source code from github
cd ~
git clone https://github.com/postgres/postgres.git


# 2.) configure/make/install postgres 9.5.x
cd postgres/
./configure --prefix=$1
make
make install
cd ..


# 3.) use curl to download Apache httpd-2.4.25
curl -o httpd-2.4.25.tar.bz2 http://apache.mirrors.tds.net//httpd/httpd-2.4.25.tar.bz2


# 4.) configure/make/install httpd
tar -xvzf httpd-2.4.25.tar.bz2
cd httpd-2.4.25/
./configure --prefix=$1
make
make install
cd ..