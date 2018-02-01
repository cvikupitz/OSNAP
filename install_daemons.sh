#!usr/bin/bash

# Clone the postgres source code from github
cd ~
git clone https://github.com/postgres/postgres.git


# Configure/make/install postgres 9.5.x
cd postgres/
./configure --prefix=$1
make
make install
cd ..
rm -fr postgres


# Use curl to download Apache httpd-2.4.25
curl -o httpd-2.4.25.tar.bz2 http://apache.mirrors.tds.net//httpd/httpd-2.4.25.tar.bz2


# Configure/make/install httpd
tar -xjf httpd-2.4.25.tar.bz2
cd httpd-2.4.25/
./configure --prefix=$1
make
make install
cd ..
rm -fr httpd-2.4.25
