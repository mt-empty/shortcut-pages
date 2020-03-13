# SQL Statements

> Source: http://www.w3schools.com/SQL/sql_quickref.asp

> Aliases: sql-statements

$ Data Definition Language (DDL)
    `CREATE TABLE                  {{Define a new table}} 
    `ALTER TABLE                   {{Modifies a table definition}} 
    `CREATE VIEW                   {{Define a new view}} 
    `DROP TABLE                    {{Remove a table}} 
    `CREATE INDEX                  {{Define a new index}} 
    `DROP INDEX                    {{Remove an index}} 
    `DROP VIEW                     {{Remove a view}} 
    `TRUNCATE TABLE                {{Empty a table}} 

$ Data Manipulation Language (DML)
    `SELECT                        {{Retrieve rows from a table or view}} 
    `INSERT INTO                   {{Create new rows in a table}} 
    `UPDATE                        {{Update rows of a table}} 
    `DELETE                        {{Delete rows of a table}} 
    `SELECT <columns> INTO         {{Create a new table from the results of a query}} 

$ Data Control Language (DCL)
    `GRANT                         {{To allow specified users to perform specified tasks}} 
    `REVOKE                        {{Removes user access rights or privileges to the database objects}} 

$ Transaction Control Language (TCL)
    `COMMIT                        {{Save or enable DML changes to the database}} 
    `ROLLBACK                      {{To undo DML changes till in a transaction}} 
    `SAVEPOINT                     {{To divide a transaction}} 

$ Aggregate Functions
    `AVG()                         {{Returns the average value of a numeric column}} 
    `COUNT()                       {{Returns the number of rows that matches a specified criteria}} 
    `MAX()                         {{Returns the largest value of the selected column}} 
    `MIN()                         {{Returns the smallest value of the selected column}} 
    `SUM()                         {{Returns the total sum of a numeric column}} 

$ Scalar Functions
    `UCASE()                       {{Converts a field to upper case}} 
    `LCASE()                       {{Converts a field to lower case}} 
    `MID()                         {{Extract characters from a text field}} 
    `LEN()                         {{Returns the length of a text field}} 
    `ROUND()                       {{Rounds a numeric field to the number of decimals specified}} 
    `NOW()                         {{Returns the current system date and time}} 
    `FORMAT()                      {{Formats how a field is to be displayed}} 

$ Arguments Used with Commands
    `WHERE                         {{To retrieve specific information from a table excluding other irrelevant data}} 
    `AND                           {{Select rows that must satisfy all the given conditions}} 
    `OR                            {{Select rows that satisfy atleast one of the given conditions}} 
    `NOT                           {{Select rows that do not satisfy the given condition}} 
    `AS (alias)                    {{To temporarily rename a table or a column heading}} 
    `BETWEEN..AND..                {{To select values within a range}} 
    `EXISTS                        {{Used in combination with a subquery and is considered to be met if the subquery returns at least one row}} 
    `GROUP BY                      {{To collect data across multiple records and group the results by a column}} 
    `HAVING                        {{To filter data based on the group functions}} 
    `IN                            {{To test whether a value is in the list of values provided}} 
    `LIKE                          {{To search for a specified pattern in a column}} 
    `DISTINCT                      {{To return only distinct (different) values in a column}} 
    `ORDER BY                      {{To sort the records in the result based on a column}} 
    `IS NULL                       {{To test for a NULL value in a column}} 
    `INNER JOIN                    {{Returns all rows from both tables where there is a match}} 
    `LEFT JOIN                     {{Returns all the rows from the first table even if there are no matches in the second table}} 
    `RIGHT JOIN                    {{Returns all the rows from the second table, even if there are no matches in the first table}} 
    `FULL JOIN                     {{Returns all rows from both tables with nulls in place where the join condition is not met}} 
    `UNION                         {{Combines the result of two or more SELECT statements and selects only distinct values}} 
    `UNION ALL                     {{Combines the result of two or more SELECT statements and also select duplicate values}} 

$ SQL Constraints
    `NOT NULL                      {{Enforces a column to not accept NULL values}} 
    `UNIQUE                        {{Ensures that each row for a column must have a unique value}} 
    `PRIMARY KEY                   {{Combination of NOT NULL and UNIQUE.It uniquely identifies each record in a database table}} 
    `FOREIGN KEY                   {{Ensure the referential integrity of the data in one table to match values in another table}} 
    `DEFAULT                       {{Specifies a default value for a column}} 

