#!/bin/bash

DB=t1_db
USER=t1_user
PASSWORD=t1_password

# creates user
# -S - not superuser (this is the default anyway)
# -D - not allowe to create DB (this is the default anyway)
# -R - no role creation (this is the default anyway)

sudo -iu postgres createuser ${USER} -S -D -R


# create DB and assing user as owner
# -O owner
sudo -iu postgres createdb  ${DB} -O ${USER}


# ADD PASSWORD TO USER

sudo -iu postgres psql -c "alter user ${USER} with password '${PASSWORD}';"

#ENABLE POSTGIS
sudo -iu postgres psql ${DB} -c "CREATE EXTENSION postgis;"
sudo -iu postgres psql ${DB} -c "CREATE EXTENSION postgis_topology;"


# now run migrate

