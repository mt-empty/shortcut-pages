# PHP

> Source: http://php.net/manual/en/index.php

$ PHP Language Constructs
    `echo                          {{Output one or more strings}} 
    `print                         {{Output a string}} 
    `unset                         {{Unset a given variable}} 
    `isset                         {{Determine if a variable is set and is not NULL}} 
    `empty                         {{Determine whether a variable is empty}} 
    `include                       {{Include and evaluate the specified file}} 
    `require                       {{Include and evaluate the specified file, raise CompileError upon failure}} 
    `die                           {{Output a message and terminate the current script}} 

$ PHP Array Functions
    `count($array)                 {{Count all elements in array}} 
    `array_values($array)          {{Retrieve all the values from an associative array}} 
    `array_keys($array)            {{Retrieve all the keys from an associative array}} 
    `array_diff($array)            {{Values present in first argument but not in other arguments}} 
    `array_intersect($array)       {{Values present in first argument and in other arguments}} 
    `array_merge($array)           {{Merge one or more arrays in the first argument}} 
    `array_pop($array)             {{Pop the element off the end of array}} 
    `array_push($array, $value)    {{Push one or more elements onto the end of array}} 
    `array_shift($array)           {{Removes an element from the beginning of an array}} 
    `array_unshift($array, $value) {{Adds an element to the beginning of an array}} 
    `array_reverse($array)         {{Reverse array elements}} 
    `array_flip($array)            {{Flipped array on success else null}} 
    `array_search($needle, $array) {{Searches for needle in array and returns key}} 
    `in_array($searched_value, $array)
>                                  {{Searches an array for a specific value}} 
    `array_key_exists($key, $array)
>                                  {{Returns TRUE if the given key is set in the array}} 

$ PHP String Functions
    `strlen()                      {{Returns string length}} 
    `substr()                      {{Return part of a string}} 
    `strpos()                      {{Position of first occurrence of case insensitive substring}} 
    `strtolower()                  {{Make string lowercase}} 
    `strtoupper()                  {{Make string uppercase}} 
    `strrev()                      {{Reverse a string}} 
    `str_split()                   {{Convert a string to array}} 
    `strcmp()                      {{Binary safe string comparison}} 
    `strtr()                       {{Translate characters or replace substrings}} 
    `str_replace()                 {{Replaces some characters with some other characters in a string}} 
    `trim()                        {{Removes the white-spaces from both start and the end of the string}} 
    `ltrim()                       {{Removes the white-spaces from the left part of the string}} 
    `rtrim()                       {{Removes the white-spaces from the right part of the string}} 
    `explode()                     {{Breaks the string into array on the basis of delimiter passed}} 
    `implode()                     {{Join array elements with a string on the basis of delimiter passed}} 

$ PHP Sort Functions
    `sort($array)                  {{Sort arrays in ascending order}} 
    `rsort($array)                 {{Sort arrays in descending order}} 
    `asort($array)                 {{Sort associative arrays in ascending order, according to the value}} 
    `ksort($array)                 {{Sort associative arrays in ascending order, according to the key}} 
    `arsort($array)                {{Sort associative arrays in descending order, according to the value}} 
    `krsort($array)                {{Sort associative arrays in descending order, according to the key}} 

$ PHP File Functions
    `fopen()                       {{Opens a file or url}} 
    `fclose()                      {{Closes an open file pointer}} 
    `fread()                       {{Reads bytes from file pointer}} 
    `fgets()                       {{Reads line from file pointer}} 
    `fwrite()                      {{Writes bytes to a file pointer}} 
    `file_exists()                 {{Checks whether a file or directory exists}} 

$ PHP Date Functions
    `date()                        {{Formats a local time/date}} 
    `time()                        {{Returns the current Unix timestamp}} 
    `mktime()                      {{Get Unix timestamp from a date}} 
    `microtime()                   {{Returns the current Unix timestamp with microseconds}} 

