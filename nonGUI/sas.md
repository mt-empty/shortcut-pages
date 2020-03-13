# Statistical Analysis System (SAS)

> Source: https://www.ualberta.ca/~ahamann/teaching/renr480/SAS-Cheat.pdf

> Aliases: sas-basics

$ Language
    `ATTRIB                        {{Associates a format, informat, label, and/or length with one or more variables}} 
    `CARDS or CARDS4 | DATALINES or DATALINES4
>                                  {{Indicates that data lines}} 
    `DATA                          {{Begins a DATA step}} 
    `FILE filename                 {{Specifies the current output file}} 
    `INPUT                         {{Input records from the current input file}} 
    `INFILE                        {{Specifies an external file to read with an INPUT statement}} 
    `MERGE                         {{Joins observations from two or more SAS data sets into single observations}} 
    `PUT                           {{Writes variable values and/or text to the output line}} 
    `RETAIN                        {{Causes a variable to retain its value}} 
    `SET                           {{Reads observations from one or more data sets}} 
    `SUM                           {{Adds the result of an expression to an accumulator var}} 
    `TITLE                         {{Specifies title lines for SAS output}} 
    `WHERE                         {{Selects observations from SAS data sets}} 

$ Data Set Options
    `DROP                          {{Excludes variables from processing}} 
    `FIRSTOBS                      {{Specifies the first observation to process}} 
    `IN                            {{Creates and names a variable}} 
    `KEEP                          {{Selects variables for processing}} 
    `LABEL                         {{Specifies a label for a SAS data set}} 
    `OBS                           {{Specifies the first n observations to process}} 
    `POINT                         {{Direct observation number variable}} 
    `RENAME                        {{Changes the name of a variable}} 
    `WHERE                         {{Selects observations from a SAS data set}} 

$ Functions
    `BYTE                          {{Returns one character in the ASCII or EBCDIC collating sequence}} 
    `COMPBL                        {{Removes multiple blanks from a character string}} 
    `COMPRESS                      {{Removes specific characters from a character string}} 
    `DATE                          {{Returns the current date as a SAS date value}} 
    `DATETIME                      {{Returns the current date and time of day}} 
    `HMS                           {{Returns time value from hour, minute, and second}} 
    `LEFT                          {{Left-aligns a character string}} 
    `LOWCASE                       {{Converts all letters in an argument to lowercase}} 
    `MAX                           {{Returns the largest value of the numeric arguments}} 
    `MIN                           {{Returns the smallest value of the numeric arguments}} 
    `SCAN                          {{Returns a given word from a character expression}} 
    `TRANSLATE                     {{Replaces specific characters in a character expression}} 

$ Formats
    `w.d                           {{Standard numeric}} 
    `COMMAw.d                      {{Writes numeric values with commas and decimal points}} 
    `Zw.d                          {{Print leading zero}} 
    `$w.                           {{Writes standard character data}} 
    `$CHARw.                       {{Writes standard character data}} 
    `$VARYINGw.                    {{Writes character data of varying length}} 

$ Informats
    `w.d                           {{Reads standard numeric data}} 
    `datew.                        {{Reads date values (ddmmmyy)}} 
    `$w.                           {{Reads standard character data}} 
    `$VARYINGw.                    {{Reads character data of varying length}} 

$ Procedures
    `PROC COMPARE                  {{Compares the contents of two SAS data sets}} 
    `PROC DATASETS                 {{Specifies the data set where the information will be listed}} 
    `PROC EXPORT                   {{Write your data into file}} 
    `PROC IMPORT                   {{Imports the external file and sets a temporary SAS data set}} 
    `PROC FORMAT                   {{Efficient and compact way to store all sorts of facts and data for data-driven application}} 
    `PROC FREQ                     {{Invokes the procedure and optionally identifies the input data set}} 
    `PROC MEANS                    {{Rapidly and efficiently analyze the values of numeric variables and place those analyses either in the output window or in a SAS data set}} 
    `PROC REPORT                   {{General process of building a report}} 
    `PROC SORT                     {{Sort data by using diferent options}} 
    `PROC TRANSPOSE                {{Reshape, transform the data into long suitable formats}} 

