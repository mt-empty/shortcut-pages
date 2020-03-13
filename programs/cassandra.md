# Cassandra

> Source: https://gabhi.github.io/cassandra_cheat_sheet/

> Aliases: datastax, cqlsh, cassandra-database, cql

$ KEYSPACE
    `CREATE KEYSPACE keyspace_name WITH DURABLE_WRITES = ( true | false )
>                                  {{Define a new keyspace and its replica placement strategy}} 
    `USE keyspace_name             {{Connect the client session to a keyspace.}} 
    `ALTER KEYSPACE keyspace_name WITH REPLICATION = map | ( WITH DURABLE_WRITES = ( true | false )) AND ( DURABLE_WRITES = ( true | false))
>                                  {{Change property values of a keyspace}} 
    `DROP KEYSPACE keyspace_name   {{Remove the keyspace}} 

$ USER
    `CREATE USER user_name WITH PASSWORD 'password' ( NOSUPERUSER | SUPERUSER )
>                                  {{Create a new user}} 
    `ALTER USER user_name WITH PASSWORD 'password' ( NOSUPERUSER | SUPERUSER )
>                                  {{Alter existing user options}} 
    `DROP USER user_name           {{Remove a user}} 
    `LIST ALL PERMISSIONS ON user_name NORECURSIVE
>                                  {{List permissions granted to a user}} 
    `LIST USERS                    {{List existing users and their superuser status}} 

$ TABLE
    `CREATE TABLE table_name       {{Define a new table}} 
    `ALTER TABLE table_name        {{Modify the column metadata of a table}} 
    `SELECT select_expression FROM table_name WHERE relation AND relation ... ORDER BY ( clustering_column ( ASC | DESC )...) LIMIT n ALLOW FILTERING
>                                  {{Retrieve data from a Cassandra table}} 
    `UPDATE table_name USING option AND option SET assignment, assignment, ... WHERE row_specification
>                                  {{Update columns in a row}} 
    `DELETE column_name  FROM table_name USING TIMESTAMP integer WHERE row_specification
>                                  {{Removes entire rows or one or more columns from one or more rows}} 
    `TRUNCATE table_name           {{Remove all data from a table}} 
    `INSERT INTO table_name ( column_name, column_name...) VALUES ( value, value ... ) USING option AND option
>                                  {{Add or update columns. option is one of: TIMESTAMP microseconds, TTL seconds}} 
    `DROP TABLE table_name         {{Remove the named table}} 

$ INDEX
    `CREATE CUSTOM INDEX index_name ON table_name ( column_name ) (USING class_name) (WITH OPTIONS = map)
>                                  {{Define a new index on a single column of a table}} 
    `DROP INDEX name               {{Drop the named index}} 

