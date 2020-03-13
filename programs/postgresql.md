# PostgreSQL

> Source: https://wiki.debian.org/PostgreSql

> Aliases: postgres

$ Installation (Debian)
    `apt-get install postgresql postgresql-client
>                                  {{Installs PostgreSQL and PostgreSQL client}} 
    `apt-get install postgresql-doc
>                                  {{Installs PostgreSQL documentation}} 
    `apt-get install pgadmin3      {{Installs PostgreSQL administration GUI}} 
    `apt-get install phppgadmin    {{Installs PostgreSQL web-based administration tool}} 

$ PostgreSQL
    `\du                           {{Lists roles}} 
    `\l                            {{Lists all the databases}} 
    `\dt                           {{List tables in connected database}} 
    `\dn                           {{List schemas}} 
    `\d table                      {{List columns on table}} 
    `\df                           {{List functions}} 
    `\q                            {{Quit}} 
    `\dv                           {{List views}} 
    `\x                            {{Pretty-format query results}} 

$ User Access
    `psql                          {{Connect to the database}} 
    `psql -d mypgdatabase -U mypguser
>                                  {{Connect to localhost as mypguser}} 

$ Role
    `CREATE ROLE demorole1 WITH LOGIN PASSWORD 'password1' CREATEDB
>                                  {{Create role}} 
    `ALTER ROLE demorole1 CREATEROLE CREATEDB REPLICATION SUPERUSER
>                                  {{Alter role}} 
    `DROP ROLE demorole1           {{Drop role}} 

$ New User and Database
    `CREATE USER mypguser WITH PASSWORD 'mypguserpass';
>                                  {{Create a user}} 
    `CREATE DATABASE mypgdatabase OWNER mypguser;
>                                  {{Create a database}} 

$ PostgreSQL Service Management
    `sudo service postgresql reload
>                                  {{Reload postgresql}} 

$ Database Clusters
    `pg_lsclusters                 {{Check installed clusters and obtain some basic informations}} 
    `pg_ctlcluster                 {{Start/stop/restart/reload a PostgreSQL cluster}} 
    ` pg_dropcluster               {{Completely delete a PostgreSQL cluster}} 
    ` pg_createcluster             {{Create a new PostgreSQL cluster}} 

