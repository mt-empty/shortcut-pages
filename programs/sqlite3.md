# Sqlite3

> Source: http://www.cheatography.com/richardjh/cheat-sheets/sqlite3/

> Aliases: sqlite3-language, sqlite3-functions

$ Meta Commands
    `backup ?DB? FILE              {{Backup DB (default "main") to FILE}} 
    `bail ON|OFF                   {{Stop after hitting an error. Default OFF}} 
    `databases                     {{List names and files of attached databases}} 
    `dump ?TABLE? ...              {{Dump the database in an SQL text format}} 
    `echo ON|OFF                   {{Turn command echo on or off}} 
    `exit                          {{Exit current program}} 
    `explain ?ON|OFF?              {{Turn output mode suitable for EXPLAIN on or off}} 
    `header(s) ON|OFF              {{Turn display of headers on or off}} 
    `help                          {{Shows this information}} 
    `import FILE TABLE             {{Import data from FILE into TABLE}} 
    `indices ?TABLE?               {{Show names of all indices}} 
    `load FILE ?ENTRY?             {{Load an extension library}} 
    `log FILE|off                  {{Turn logging on or off. FILE can be stderr/stdout}} 
    `mode MODE ?TABLE?             {{Set output mode where MODE is one of: csv, column, html, insert, line, list, tabs, tcl}} 
    `nullvalue STRING              {{Print STRING in place of NULL values}} 
    `output FILENAME               {{Send output to FILENAME}} 
    `output stdout                 {{Send output to the screen}} 
    `prompt MAIN CONTINUE          {{Replace the standard prompts}} 
    `quit                          {{Exit this program}} 
    `read FILENAME                 {{Execute SQL in FILENAME}} 
    `restore ?DB? FILE             {{Restore content of DB (default "main") from FILE}} 

$ Meta Commands conditions
    `schema ?TABLE?                {{Show the CREATE statements}} 
    `separator STRING              {{Change separator used by output mode and .import}} 
    `show                          {{Show the current values for various settings}} 
    `stats ON|OFF                  {{Turn stats on or off}} 
    `tables ?TABLE?                {{List names of tables}} 
    `timeout MS                    {{Try opening locked tables for MS milliseconds}} 
    `width NUM1 NUM2 ...           {{Set column widths for "column" mode}} 
    `timer ON|OFF                  {{Turn the CPU timer measur­ement on or off}} 

$ Options
    `init file                     {{Read and execute commands from file , which can contain a mix of SQL statements and meta-commands}} 
    `echo                          {{Print commands before execution}} 
    `[no]header                    {{Turn headers on or off}} 
    `bail                          {{Stop after hitting an error}} 
    `interactive                   {{Force intera­ctive I/O}} 
    `batch                         {{Force batch I/O}} 
    `column                        {{Query results will be displayed in a table like form, using whitespace characters to separate the columns and align the output}} 
    `csv                           {{Set output mode to CSV (comma separated values)}} 
    `html                          {{Query results will be output as simple HTML tables}} 
    `line                          {{Query results will be displayed with one value per line, rows separated by a blank line. Designed to be easily parsed by scripts or other programs}} 
    `list                          {{Query results will be displayed with the separator (|, by default) character between each field value. The default}} 
    `separator separator           {{Set output field separator. Default is '|'}} 
    `stats                         {{Print memory stats before each finalize}} 
    `nullvalue string              {{Set string used to represent NULL values. Default is '' (empty string)}} 
    `version                       {{Show SQLite version}} 
    `vfs name                      {{Use name as the default VFS}} 
    `help                          {{Show help on options and exit}} 

