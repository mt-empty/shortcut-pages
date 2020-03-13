# Apache Hive

> Source: https://www.tutorialspoint.com/hive/index.htm

> Aliases: hive

$ Retrieving Information
    `SELECT [from_columns] FROM [table]
WHERE [conditions];
>                                  {{Retrieving Information (General)}} 
    `SELECT * FROM [table];        {{Retrieving All Values}} 
    `SELECT * FROM [table]
WHERE [col_name] =[value];
>                                  {{Retrieving Some Values}} 
    `SELECT * FROM [table] WHERE
[col_name1] = [value1] AND [col_name2] = [value2];
>                                  {{Retrieving With Multiple Criteria}} 
    `SELECT [col_name] FROM [table];
>                                  {{Retrieving Specific Columns}} 
    `SELECT DISTINCT [col_name] FROM [table];
>                                  {{Retrieving Unique Output}} 
    `SELECT [col1], [col2] FROM [table]
ORDER BY [col2];
>                                  {{Sorting}} 
    `SELECT [col1], [col2] FROM [table]
ORDER BY [col2] DESC;
>                                  {{Sorting Reverse}} 
    `SELECT COUNT(*) FROM [table]; {{Counting Rows}} 
    `SELECT [col_name],COUNT(*) FROM [table]
GROUP BY [col_name];
>                                  {{Grouping With Counting}} 
    `SELECT MAX([col_name]) AS label FROM [table];
>                                  {{Maximum Value}} 

$ Table Joins
    `SELECT [table_1].[col], [table_2].[col]
FROM [table_1] JOIN [table_2]
ON ([table_1].[col_1] =[table_2].[col_1]);
>                                  {{Selecting from multiple tables after inner join}} 
    `SELECT [table_1].[col], [table_2].[col]
FROM [table_1] LEFT JOIN [table_2]
ON ([table_1].[col_1] =[table_2].[col_1]);
>                                  {{Selecting from multiple tables after left join}} 
    `SELECT [table_1].[col], [table_2].[col]
FROM [table_1] RIGHT JOIN [table_2]
ON ([table_1].[col_1] =[table_2].[col_1]);
>                                  {{Selecting from multiple tables after right join}} 
    `SELECT [table_1].[col], [table_2].[col]
FROM [table_1] FULL JOIN [table_2]
ON ([table_1].[col_1] =[table_2].[col_1]);
>                                  {{Selecting from multiple tables after full join}} 

$ Partitioning
    `([p_column] = [p_col_value],
[p_column] = [p_col_value], [...])
>                                  {{Partitioning Specification [partition_spec]}} 
    `ALTER TABLE [table_name]
ADD PARTITION [partition_spec];
>                                  {{Adding partition}} 
    `ALTER TABLE [table_name]
PARTITION [partition_spec]
RENAME TO PARTITION [partition_spec];
>                                  {{Renaming partition}} 
    `ALTER TABLE [table_name]
DROP PARTITION [partition_spec],
PARTITION [partition_spec],[...];
>                                  {{Dropping partition}} 

$ Metadata
    `USE [database];               {{Selecting a database}} 
    `SHOW DATABASES;               {{Listing databases}} 
    `SHOW TABLES;                  {{Listing tables in a database}} 
    `DESCRIBE (FORMATTED|EXTENDED) [table];
>                                  {{Describing the format of a table}} 
    `CREATE DATABASE [db_name];    {{Creating a database}} 
    `DROP DATABASE [db_name];      {{Dropping a database}} 

$ Command Line
    `hive -e 'SELECT a.[col] FROM [table] a'
>                                  {{Run Query}} 
    `hive -S -e 'SELECT a.[col] FROM [table] a'
>                                  {{Run Query Silent Mode}} 
    `hive -e 'SELECT a.[col] FROM [table] a'
--hiveconf hive.root.logger=DEBUG,console
>                                  {{Set Hive Config Variables}} 
    `hive -i initialize.sql        {{Use Initialization Script}} 
    `hive -f script.sql            {{Run Non-Interactive Script}} 

