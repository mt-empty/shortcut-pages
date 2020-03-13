# IBMdb2

> Source: http://dublintech.blogspot.in/2011/10/db2-cheat-sheet.html

> Aliases: db2, ibm-db2-shell

$ DB2 System Commands
    `DB2LEVEL                      {{Check version of DB2 installed}} 
    `DB2ILIST                      {{List all instances installed}} 
    `DB2CMD                        {{Open a command line processor}} 
    `DB2CC                         {{Open db2 control center}} 
    `DB2LICM -l                    {{Get db2 type}} 

$ Command Line Processor
    `DB2 LIST NODE                 {{List all nodes}} 
    `DB2 CATALOG                   {{Store database location information in the system database directory}} 
    `DB2 LIST DATABASE             {{List databases}} 
    `DB2 GET DB CFG                {{Get configuration info}} 
    `DB2 CONNECT                   {{Connect to db}} 
    `DB2 DISCONNECT                {{Close the connection}} 
    `DB2 LIST APPLICATIONS SHOW DETAIL
>                                  {{Show all running datatbases}} 
    `DB2 GET DBM CFG               {{View authentication paramaters}} 
    `DB2 UPDATE DBM CFG            {{Alter the authentication mechanism}} 
    `DB2 GET AUTHORIZATIONS        {{Get authorisation level}} 

$ Database Commands via Command Line Processor (CLP)
    `DB2 GET DATABASE CONFIGURATION
>                                  {{Get current database configuration}} 
    `DB2 VALUES CURRENT USER       {{Get the current user}} 
    `DB2 VALUES CURRENT SCHEMA     {{Get the current schema}} 
    `DB2 VALUES CURRENT QUERY OPTIMIZATION
>                                  {{Get query optimization level}} 

$ Schemas
    `DB2 SELECT SCHEMANAME         {{List all schemas}} 
    `DB2 VALUES CURRENT SCHEMA     {{Get the current schema}} 
    `DB2 SET SCHEMA                {{Set corresponding schema}} 

$ Tables
    `DB2 LIST TABLES FOR schema_name
>                                  {{List all tables for particular schema}} 
    `DB2 LIST TABLES SHOW DETAIL   {{Show details about tables}} 
    `DECLARE GLOBAL TEMPORARY TABLE
>                                  {{Declares a temporary table}} 
    `CREATE TABLE MQT              {{Create a materialised query table}} 

$ Tablespaces
    `DB2 LIST TABLESPACES SHOW DETAIL
>                                  {{Show detail about table spaces}} 
    `SYSCAT.TABLESPACES            {{Show syscat info about tablespaces}} 
    `SELECT TBSPACE, BUFFERPOOLID FROM SYSCAT.TABLESPACES
>                                  {{Get tablespace and bufferpoolid}} 
    `SELECT TABNAME FROM SYSCAT.TABLES WHERE TBSPACE=id
>                                  {{Check what TABLES are in tablespace where id = 'id'}} 

$ Constraints
    `SYSCAT.TABCONST               {{Table constraint}} 
    `SYSCAT.CHECKS                 {{Column checks}} 
    `SYSCAT.COLCHECKS              {{Column constraint}} 
    `SYSCAT.REFERENCES             {{Referential constraint}} 

$ Sequences
    `CREATE SEQUENCE               {{Create Sequence}} 
    `SYSCAT.SEQUENCES              {{Get systcat info on sequences}} 
    `VALUES NEXT VALUE FOR MYSEQ   {{Get next value from sequence Myseq}} 
    `ALTER SEQUENCE MYSEQ          {{Change MySeq sequence}} 

$ Locksize
    `LOCKSIZE                      {{Check locksize which can be tablespace, table, partition, page, row}} 

$ Bufferpools
    `SYSCAT.BUFFERPOOLS            {{Get useful buffer pool info}} 
    `TABLESPACE.BUFFERPOOLID       {{Get buffer pool and corresponding tablespace info}} 

$ Indexes
    `SYSCAT.INDEXES                {{Show all indexes}} 

$ Functions
    `SYSCAT.FUNCTIONS              {{Check the functions DB}} 

$ SYSDUMMY1 commands
    `SELECT CURRENT DATE           {{Get current date}} 
    `SELECT HEX(36)                {{Get the VALUES HEX(36)}} 
    `SELECT XMLCOMMENT             {{Return an XML value with a single XQuery comment node}} 

$ Runstats
    `RUNSTATS ON TABLE             {{Runstats for all indexes checking the last time runstats was run}} 
    `CARD=-1 OR STATS_TIME=NULL    {{Runstats utility is not running for respective table}} 
    `NLEAF=-1 AND NLEVELS=-1 AND FULLKEYCARD=-1
>                                  {{Runstats utility is not running for respective table}} 

