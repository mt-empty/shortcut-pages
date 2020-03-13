# Apache Pig

> Source: http://mortar-public-site-content.s3-website-us-east-1.amazonaws.com/

> Aliases: apache-pig-shell, pig-functions, pig-lang, pig-basics

$ Data Types
    `int                           {{Signed 32-bit integer}} 
    `long                          {{Signed 64-bit integer}} 
    `float                         {{32-bit floating point}} 
    `double                        {{64-bit floating point}} 
    `chararray                     {{Character array (string) in Unicode UTF-8 format}} 
    `bytearray                     {{Byte array (blob)}} 
    `boolean                       {{Logical value}} 
    `datetime                      {{org.joda.time.DateTime}} 
    `biginteger                    {{Java BigInteger}} 
    `bigdecimal                    {{Java BigDecimal}} 
    `tuple                         {{An ordered set of fields}} 
    `bag                           {{A collection of tuples}} 
    `map                           {{A set of key value pairs}} 

$ Relational Operators
    `COGROUP alias BY (col1, col2) {{Uses when multiple relations involve}} 
    `CROSS alias1, alias2          {{Computes the cross product of two or more relations}} 
    `CUBE alias BY CUBE(exp1, exp2, ...)
>                                  {{It computes aggregates for all possbile combinations of specified group by dimensions}} 
    `CUBE alias BY ROLLUP(exp1, exp2, ...)
>                                  {{It computes multiple levels of aggregates based on hierarchical ordering of specified group by dimensions}} 
    `DISTINCT alias                {{Removes duplicate tuples in a relation}} 
    `FILTER alias BY expression    {{Selects tuples from a relation based on some condition}} 
    `...FLATTEN(tuple/bag)         {{Un-nests a tuple or a bag}} 
    `FOREACH ... GENERATE          {{Performs transformations on each row in the data}} 
    `GROUP alias ALL               {{Groups the data in one or multiple relations}} 
    `JOIN smaller_alias BY expression, larger_alias BY expression
>                                  {{Performs inner, equijoin of two or more relations based on common field values}} 
    `JOIN smaller_alias BY expression [LEFT|RIGHT|OUTER], larger_alias BY expression
>                                  {{Performs an outer join of two or more relations based on common field values}} 
    `JOIN big_alias BY expression, small_alias BY expression USING 'replicated'
>                                  {{Efficient join when one or more relations are small enough to fit in main memory}} 
    `LIMIT alias n                 {{Limits the number of output tuples}} 
    `LOAD 'data' [USING function] [AS schema]
>                                  {{Loads data from the file system}} 
    `ORDER alias BY col [ASC | DESC]
>                                  {{Sorts a relation based on one or more fields}} 
    `RANK alias BY col [ASC | DESC]
>                                  {{Returns each tuple with the rank within a relation}} 
    `SAMPLE alias size             {{Selects a random sample of data based on the specified sample size}} 
    `SPLIT alias INTO alias1 IF expression, alias2 IF expression...
>                                  {{Partitions a relation into two or more relations}} 
    `STORE alias INTO ‘directory’ [USING function]
>                                  {{Stores or saves results to the file system}} 
    `UNION alias1, alias2          {{Computes the union of two or more relations}} 

$ Mathematical Functions
    `ABS(int a)                    {{Returns the absolute(int) value of an expression}} 
    `ACOS(double a)                {{Returns the arc cosine of an expression}} 
    `ASIN(double a)                {{Returns the arc sine of an expression}} 
    `ATAN(double a)                {{Returns the arc tangent of an expression}} 
    `CBRT(double a)                {{Returns the cube root of an expression}} 
    `CEIL(double a)                {{Returns the value of an expression rounded upto the nearest integer}} 
    `COS(double a)                 {{Returns the cosine of an expression}} 
    `COSH(double a)                {{Returns the hyperbolic cosine of an expression}} 
    `EXP(double a)                 {{Returns Euler's number e raised to the power of x}} 
    `FLOOR(double a)               {{Returns the value of an expression rounded down to the nearest integer}} 
    `LOG(double a)                 {{Returns the natural logarithm (base e) of an expression}} 
    `LOG10(double a)               {{Returns the base 10 logarithm of an expression}} 
    `RANDOM( )                     {{Returns a pseudo random number greater than or equal to 0.0 and less than 1.0}} 
    `ROUND(float a), ROUND(double a)
>                                  {{Returns the value of an expression rounded to an integer}} 
    `SIN(double a)                 {{Returns the sine of an expression}} 
    `SINH(double a)                {{Returns the hyperbolic sine of an expression}} 
    `SQRT(double a)                {{Returns the positive square root of an expression}} 
    `TAN(double a)                 {{Returns the tangent of an expression}} 
    `TANH(double a)                {{Returns the hyperbolic tangent of an expression}} 

$ Eval Functions
    `AVG(col)                      {{Computes the average of the numeric values in a single column of a bag}} 
    `CONCAT(String expression1, String expression2)
>                                  {{Concatenates two expressions of identical type}} 
    `COUNT(DataBag bag)            {{Computes the number of elements in a bag, excluding null values}} 
    `COUNT_STAR(DataBag bag)       {{Computes the number of elements in a bag, including null values}} 
    `DIFF(DataBag bag1, DataBag bag2)
>                                  {{Compares two bags}} 
    `IsEmpty(DataBag bag), IsEmpty(Map map)
>                                  {{Checks if a bag or map is empty}} 
    `MAX(col)                      {{Computes the maximum of the numeric values}} 
    `MIN(col)                      {{Computes the minimum of the numeric values}} 
    `DEFINE pluck PluckTuple(expression1) pluck(expression2)
>                                  {{Allows the user to specify a string prefix, and then filter for the columns in a relation that begin with that prefix}} 
    `SIZE(expression)              {{Computes the number of elements based on any Pig data type}} 
    `SUBTRACT(DataBag bag1, DataBag bag2)
>                                  {{Returns bag composed of bag1 elements not in bag2}} 
    `SUM(col)                      {{Computes the sum of the numeric values in a single-column bag}} 
    `TOKENIZE(String expression , ‘field_delimiter’)
>                                  {{Splits a string and outputs a bag of words}} 

$ String Functions
    `ENDSWITH(String string, String testAgainst)
>                                  {{Tests inputs to determine if the first argument ends with the string in the second}} 
    `EqualsIgnoreCase(String string1, String string2)
>                                  {{Compares two strings ignoring case considerations}} 
    `INDEXOF(String string, String 'character', int startIndex)
>                                  {{Returns the index of the first occurrence of a character in a string, searching forward from a start index}} 
    `LAST_INDEX_OF(String string, String 'character')
>                                  {{Returns the index of the last occurrence of a character in a string, searching backward from the end of the string}} 
    `LCFIRST(String expression)    {{Converts the first character in a string to lower case}} 
    `LOWER(String expression)      {{Converts all characters in a string to lower case}} 
    `LTRIM(String expression)      {{Returns a copy of a string with only leading white space removed}} 
    `REGEX_EXTRACT(String string, String regex, int index)
>                                  {{Performs regular expression matching and extracts the matched group defined by an index parameter}} 
    `RTRIM(String expression)      {{Returns a copy of a string with only trailing white space removed}} 
    `UCFIRST(String expression)    {{Returns a string with the first character converted to upper case}} 
    `TRIM(String expression)       {{Returns a copy of a string with leading and trailing white space removed}} 
    `UPPER(String expression)      {{Returns a string converted to upper case}} 

$ DateTime Functions
    `AddDuration(DateTime datetime, String duration)
>                                  {{Returns the result of a DateTime object plus an ISO 8601 duration string}} 
    `CurrentTime()                 {{Returns the DateTime object of the current time}} 
    `GetDay(DateTime datetime)     {{Returns the day of a month from a DateTime object}} 
    `GetHour(DateTime datetime)    {{Returns the hour of a day from a DateTime object}} 
    `GetMilliSecond(DateTime datetime)
>                                  {{Returns the millisecond of a second from a DateTime object}} 
    `SecondsBetween(DateTime datetime1, DateTime datetime2)
>                                  {{Returns the number of seconds between two DateTime objects}} 
    `GetMonth(DateTime datetime)   {{Returns the month of a year from a DateTime object}} 
    `GetWeek(DateTime datetime)    {{Returns the week of a week year from a DateTime object}} 
    `GetYear(DateTime datetime)    {{Returns the year from a DateTime object}} 
    `ToDate(long milliseconds)     {{Returns a DateTime object according to parameters}} 
    `ToString(DateTime datetime)   {{Converts the DateTime object to the ISO string}} 
    `ToUnixTime(DateTime datetime) {{Returns the Unix Time as long for a DateTime object}} 

$ Bag and Tuple Functions
    `TOTUPLE(expression [, expression ...])
>                                  {{Converts one or more expressions to type tuple}} 
    `TOBAG(expression [, expression ...])
>                                  {{Converts one or more expressions to type bag}} 
    `TOMAP(key-expression, value-expression [, key-expression, value-expression ...])
>                                  {{Converts key/value expression pairs into a map}} 
    `TOP(int topN, column, relation)
>                                  {{Returns the top-n tuples from a bag of tuples}} 

$ Load/Store Functions
    `AvroStorage()                 {{To load/store Avro data}} 
    `CommonLogLoader()             {{Common Log Format, Combined Log Format}} 
    `CSVExcelStorage()             {{CSV}} 
    `DynamoDBStorage()             {{DynamoDB}} 
    `FixedWidthLoader()            {{Fixed-Width}} 
    `HiveColumnaroader()           {{Hive}} 
    `JsonLoader()                  {{JSON}} 
    `MongoLoader()                 {{MongoDB}} 
    `PapertrailLoader()            {{Papertrail Logs}} 
    `PigStorage()                  {{Character-delimited (CSV, TSV)}} 
    `TextLoader()                  {{Text/Unformatted}} 
    `XMLLoader()                   {{XML}} 

