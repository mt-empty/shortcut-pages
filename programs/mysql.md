# MySQL

> Source: http://www.cheatography.com/davechild/cheat-sheets/mysql/

> Aliases: my-sql

$ MySQL String Functions (count)
    `LENGTH                        {{Return the length of a string in bytes}} 
    `CHAR_LENGTH                   {{Return number of characters in argument}} 
    `BIT_LENGTH                    {{Return length of argument in bits}} 
    `LOCATE                        {{Return the position of the first occurrence of substring}} 
    `INSTR                         {{Return the index of the first occurrence of substring}} 
    `LPAD                          {{Return the string argument, left-padded with the specified string}} 
    `RPAD                          {{Append string the specified number of times}} 
    `LEFT                          {{Return the leftmost number of characters as specified}} 
    `RIGHT                         {{Return the specified rightmost number of characters}} 
    `REPEAT                        {{Repeat a string the specified number of times}} 
    `REVERSE                       {{Reverse the characters in a string}} 
    `INSERT                        {{Insert a substring at the specified position up to the specified number of characters}} 
    `ELT                           {{Return string at index number}} 
    `FIELD                         {{Return the index (position) of the first argument in the subsequent arguments}} 
    `LCASE                         {{Synonym for LOWER()}} 
    `UCASE                         {{Synonym for UPPER()}} 
    `LOAD_FILE                     {{Load the named file}} 
    `QUOTE                         {{Escape the argument for use in an SQL statement}} 

$ MySQL String Functions
    `ASCII                         {{Return numeric value of left-most character}} 
    `ORD                           {{Return character code for leftmost character of the argument}} 
    `CONV                          {{Convert numbers between different number bases}} 
    `BIN                           {{Return a string containing binary representation of a number}} 
    `OCT                           {{Return a string containing octal representation of a number}} 
    `HEX                           {{Return a hexadecimal representation of a decimal or string value}} 
    `CHAR                          {{Return the character for each integer passed}} 
    `CONCAT                        {{Return concatenated string}} 
    `CONCAT_WS                     {{Return concatenate with separator}} 
    `SUBSTRING                     {{Return the substring as specified}} 
    `MID                           {{Return a substring starting from the specified position}} 
    `SUBSTRING_INDEX               {{Return a substring from a string before the specified number of occurrences of the delimiter}} 
    `LTRIM                         {{Remove leading spaces}} 
    `RTRIM                         {{Remove trailing spaces}} 
    `TRIM                          {{Remove leading and trailing spaces}} 
    `SOUNDEX                       {{Return a soundex string}} 
    `SPACE                         {{Return a string of the specified number of spaces}} 
    `REPLACE                       {{Replace occurrences of a specified string}} 

$ MySQL Type Conversion
    `BINARY                        {{BINARY(String)}} 
    `CAST                          {{CAST(expression AS datatype)}} 
    `CONVERT                       {{CONVERT(expression, datatype)}} 

$ MySQL Mathematical Functions
    `ABS                           {{Return the absolute value}} 
    `SIGN                          {{Return the sign of the argument}} 
    `MOD                           {{Return the remainder}} 
    `FLOOR                         {{Return the largest integer value not greater than the argument}} 
    `CEILING                       {{Return the smallest integer value not less than the argument}} 
    `ROUND                         {{Round the argument}} 
    `DIV                           {{Divides the argument}} 
    `EXP                           {{Raise to the power of}} 
    `LN                            {{Return the natural logarithm of the argument}} 
    `LOG                           {{Return the natural logarithm of the first argument}} 
    `POW                           {{Return the argument raised to the specified power}} 
    `POWER                         {{Return the argument raised to the specified power}} 
    `SQRT                          {{Return the square root of the argument}} 
    `PI                            {{Return the value of pi}} 
    `COS                           {{Return the cosine of the arguments}} 
    `SIN                           {{Return the sine of the arguments}} 
    `ACOS                          {{Return the arc cosine}} 
    `ASIN                          {{Return the arc sine}} 
    `ATAN, ATAN2                   {{Return the arc tangent of the two arguments.}} 
    `COT                           {{Return the cotangent}} 
    `RAND                          {{Return a random floating-point value}} 
    `LEAST                         {{Return a least value}} 
    `GREATEST                      {{Return a greatest value}} 
    `DEGREES                       {{Convert radians to degrees}} 
    `RADIANS                       {{Return argument converted to radians}} 
    `TRUNCATE                      {{Truncate to specified number of decimal places}} 

$ MySQL Grouping Functions
    `AVG                           {{Take average of various records set using GROUP BY clause}} 
    `BIT_AND                       {{Returns the bitwise AND of all bits in a given expression}} 
    `BIT_OR                        {{Returns the bitwise OR of all bits in a given expression}} 
    `COUNT                         {{Returns the number of given attribute present}} 
    `GROUP_CONCAT                  {{Concatenates strings from a group into a single string with various options}} 
    `MIN                           {{Find all the records with minimum value for each attribute using GROUP BY clause}} 
    `MAX                           {{Find all the records with maximum value for each attribute using GROUP BY clause}} 
    `STD                           {{Returns the population standard deviation of expression}} 
    `STDDEV                        {{Calculate the population standard deviation and sample standard deviation}} 
    `SUM                           {{Take sum of various records set using GROUP BY clause}} 
    `VARIANCE                      {{Returns the population standard variance of an expression}} 

$ MySQL Data Types
    `CHAR                          {{String (0 - 255)}} 
    `VARCHAR                       {{String (0 - 255)}} 
    `TINYTEXT                      {{String (0 - 255)}} 
    `TEXT                          {{String (0 - 65535)}} 
    `BLOB                          {{String (0 - 65535)}} 
    `MEDIUMTEXT                    {{String (0 - 16777215)}} 
    `MEDIUMBLOB                    {{String (0 - 16777215)}} 
    `LONGTEXT                      {{String (0 - 4294967295)}} 
    `LONGBLOB                      {{String (0 - 4294967295)}} 
    `TINYINT x                     {{Integer (-128 to 127)}} 
    `SMALLINT x                    {{Integer (-32768 to 32767)}} 
    `MEDIUMINT x                   {{Integer (-8388608 to 8388607)}} 
    `INT x                         {{Integer (-2147483648 to 2147483647)}} 
    `BIGINT x                      {{Integer (-9223372036854775808 to 9223372036854775807)}} 
    `FLOAT                         {{Decimal (precise to 23 digits)}} 
    `DOUBLE                        {{Decimal (24 to 53 digits)}} 
    `DECIMAL                       {{"DOUBLE" stored as string}} 
    `DATE                          {{YYYY-MM-DD}} 
    `DATETIME                      {{YYYY-MM-DD HH:MM:SS}} 
    `TIMESTAMP                     {{YYYYMMDDHHMMSS}} 
    `TIME                          {{HH:MM:SS}} 
    `ENUM                          {{One of preset options}} 
    `SET                           {{Selection of preset options}} 

$ MySQL Date and Time Functions
    `MONTH                         {{Return the month from the date passed}} 
    `DAYOFWEEK                     {{Return the weekday index of the argument}} 
    `WEEKDAY                       {{Return the weekday index}} 
    `DAYOFMONTH                    {{Return the day of the month (0-31)}} 
    `DAYOFYEAR                     {{Return the day of the year (1-366)}} 
    `DAYNAME                       {{Return the name of the weekday}} 
    `MONTHNAME                     {{Return the name of the month}} 
    `QUARTER                       {{Return the quarter from a date argument}} 
    `WEEK                          {{Return the week number}} 
    `YEAR                          {{Return the year}} 
    `YEARWEEK                      {{Return the year and week}} 
    `HOUR                          {{Extract the hour}} 
    `MINUTE                        {{Return the minute from the argument}} 
    `SECOND                        {{Return the second (0-59)}} 
    `PERIOD_ADD                    {{Add a period to a year-month}} 
    `PERIOD_DIFF                   {{Return the number of months between periods}} 
    `DATE_ADD                      {{Add time values (intervals) to a date value}} 
    `DATE_SUB                      {{Subtract a time value (interval) from a date}} 
    `ADDDATE                       {{Add time values (intervals) to a date value}} 
    `SUBDATE                       {{Synonym for DATE_SUB() when invoked with three arguments}} 
    `EXTRACT                       {{Extract part of a date}} 
    `TO_DAYS                       {{Return the date argument converted to days}} 
    `FROM_DAYS                     {{Convert a day number to a date}} 
    `DATE_FORMAT                   {{Format date as specified}} 
    `TIME_FORMAT                   {{Format as time}} 
    `CURRENT_DATE                  {{Synonyms for CURDATE()}} 
    `CURRENT_TIME                  {{Synonyms for CURTIME()}} 
    `NOW                           {{Return the current date and time}} 
    `SYSDATE                       {{Return the time at which the function executes}} 
    `UNIX_TIMESTAMP                {{Return the current UTC date and time}} 
    `FROM_UNIXTIME                 {{Format UNIX timestamp as a date}} 
    `SEC_TO_TIME                   {{Converts seconds to 'HH:MM:SS' format}} 
    `TIME_TO_SEC                   {{Return the argument converted to seconds}} 

$ MySQL Control Flow Functions
    `IF                            {{If/else construct}} 
    `NULLIF                        {{Return NULL if expr1 = expr2}} 
    `IFNULL                        {{Null if/else construct}} 

