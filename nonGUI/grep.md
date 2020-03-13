# Grep

> Source: https://www.gnu.org/software/grep/manual/grep.html

> Aliases: grep-overview, grep-options, grep-command

$ Basic Usage
    `grep 'string' 'options' filename1 filename2 ...
>                                  {{Find a string in one or more files}} 

$ Options
    `-i                            {{'ignore' option - Ignores case for matching}} 
    `-v                            {{'inverse' option - Displays lines which don't match the expression}} 
    `-n                            {{'number' option - Displays line numbers along with lines which don't match the expression}} 
    `-w                            {{'word' option - Select only words matching the pattern}} 
    `-c                            {{'count' option - Counts the number of lines containing the pattern}} 
    `-l                            {{'list' option - Displays only the filenames containing the pattern}} 
    `-e expression                 {{'expression' option - Specifies expression with this option. Can be used multiple times in a statement}} 
    `-f filename                   {{'file' option - Takes pattern from a file, one per line}} 
    `-E                            {{'Extended Regular Expression' option - Treats pattern as extended regular expression}} 

$ RE Wildcards
    `.                             {{A single character}} 
    `*                             {{Zero or more occurrences of previous characters}} 
    `+                             {{One of more occurrences of the pattern}} 
    `?                             {{Optional - Can occur zero or one times}} 
    `.                             {{A single character}} 
    `xyz                           {{Select any one of the characters x, y or z}} 
    `a-z                           {{Select a single character within the ASCII range between 'a' and 'z'}} 
    `^a-z                          {{Select a single character which does not fall in the ASCII range between 'a' and 'z'}} 
    `:al­pha:                      {{All alphabets, equivalent to [a-zA-Z]}} 
    `:di­git:                      {{All numbers, equivalent to [0-9]}} 
    `:al­num:                      {{All alphanumeric, equivalent to [a-zA-Z0-9]}} 

$ RE Anchors
    `^                             {{Beginning of a string or line}} 
    `$                             {{End of a string or line}} 
    `^$                            {{Empty line}} 
    `\<                            {{Beginning of word}} 
    `\>                            {{End of word}} 

$ Examples
    `grep 'first' example.txt      {{Returns lines which have the word 'first' in the file example.txt}} 
    `grep -i 'first' example.txt   {{Returns lines which have the word 'first' or 'First' or 'FIRST' in the file example.txt(returns results which are case insensitive)}} 
    `grep -v 'first' example.txt   {{Returns lines which do not have the word 'first' in the file example.txt}} 
    `grep -e 'first' -e 'second' example.txt
>                                  {{Returns lines which have the word 'first' or 'second' in the file example.txt}} 
    `grep -l 'first' *.txt         {{Returns list of all files with '.txt' as extension which contain the word 'first'}} 
    `grep 'fi*rst' example.txt     {{Returns lines which have the word 'fist', 'first', 'firrst', 'firrrst' etc (with zero or more occurrences of 'r') in the file example.txt}} 
    `grep '^f' example.txt         {{Returns all strings which start with 'f' in the file example.txt}} 
    `grep '$f' example.txt         {{Returns all strings which end with 'f' in the file example.txt}} 

$ File and directory selection
    `-a                            {{Process a binary file as if it were text}} 
    `-D action                     {{'If an input file is a device, FIFO, or socket, use 'action' to process it}} 
    `-d action                     {{If an input file is a directory, use 'action' to process it}} 
    `-r                            {{For each directory operand, read and process all files in that directory, recursively}} 
    `-R                            {{For each directory operand, read and process all files in that directory, recursively, following all symbolic links}} 
    `--exclude=glob                {{Skip any command-line file with a name suffix that matches the pattern 'glob', using wildcard matching}} 
    `--include=glob                {{Search only files whose name matches 'glob', using wildcard matching}} 

