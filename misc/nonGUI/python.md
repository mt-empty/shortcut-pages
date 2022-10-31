# Python

> Source: http://overapi.com/python

> Aliases: python-language, py, python2, python-2

$ Basic Built-in Functions
    `raw_input()                   {{Reads a line from input, converts it to a string and returns that}} 
    `len()                         {{Returns the length (the number of items) of an object}} 
    `max()                         {{Returns the largest item in the list or the largest of the two or more arguments}} 
    `min()                         {{Returns the smallest item in the list or the smallest of the two or more arguments}} 
    `pow()                         {{Returns first argument to the power second argument}} 
    `range(start, stop, step)      {{Returns a list of integers starting from start and ending at stop (exclusive), having a difference of step between any two adjacent elements}} 
    `xrange()                      {{Similar to range(), but returns an xrange iterator object instead of a list}} 
    `bin()                         {{Converts an integer number to a binary string}} 
    `oct()                         {{Converts an integer number to an octal string}} 
    `hex()                         {{Converts an integer nuber to a lowercase hexadecimal string prefixed with '0x'}} 
    `int()                         {{Returns an integer object from a number or string}} 
    `float()                       {{Returns a floating point number from a number or string}} 
    `type()                        {{Returns the type of any object}} 

$ String Methods
    `str()                         {{Create a new empty string}} 
    `upper()                       {{Returns a string in all uppercase}} 
    `lower()                       {{Returns a string in all lowercase}} 
    `capitalize()                  {{Returns a string with first character capitalized, the rest lower}} 
    `strip()                       {{Returns a string with the leading and trailing whitespace removed}} 
    `lstrip()                      {{Returns a string with the leading whitespace removed}} 
    `rstrip()                      {{Returns a string with the trailing whitespace removed}} 
    `count()                       {{Returns the number of occurrences of item}} 
    `replace()                     {{Replaces all occurrences of old substring with new}} 
    `center()                      {{Returns a string centered in a field of width spaces}} 
    `ljust()                       {{Returns a string left justified in a field of width spaces}} 
    `rjust()                       {{Returns a string right justified in a field of width spaces}} 
    `find()                        {{Returns the leftmost index where the substring item is found}} 
    `rfind()                       {{Returns the rightmost index where the substring item is found}} 
    `index()                       {{Similar to find() except causes a runtime error if item is not found}} 
    `rindex()                      {{Similar to rfind() except causes a runtime error if item is not found}} 
    `chr()                         {{Returns a string of one character whose ASCII code is the integer passed as argument}} 
    `ord()                         {{Returns an integer representing the Unicode code point of any string of one character}} 

$ List (Array) Methods
    `list()                        {{Creates a new empty list}} 
    `append()                      {{Adds an item to the end of the list}} 
    `extend()                      {{Extends the list by appending all the items in the given list}} 
    `insert()                      {{Inserts an item at a given position}} 
    `remove()                      {{Removes the first item from the list with aforementioned parameter value}} 
    `pop()                         {{Removes the item at the given position in the list, and return it}} 
    `index()                       {{Returns the index in the list}} 
    `count()                       {{Returns the number of times that appears in the list.}} 
    `sort()                        {{Sorts the items of the list in place}} 
    `sort(reverse=True)            {{Sorts the items of the list in place, in descending order}} 
    `reverse()                     {{Reverses the elements of the list, in place}} 
    `sum()                         {{Returns the total sum of all items of the list}} 
    `join()                        {{Concatenates all the items of the list}} 

$ Dictionary Methods
    `dict()                        {{Creates a new empty dictionary}} 
    `keys()                        {{Returns list of dictionary keys}} 
    `values()                      {{Returns list of dictionary values}} 
    `clear()                       {{Removes all elements of dictionary}} 
    `copy()                        {{Returns a shallow copy of dictionary}} 

$ File Methods and Constants
    `open()                        {{Opens a file, returning an object of the file type}} 
    `close()                       {{Closes the file; a closed file cannot be read or written any more}} 
    `flush()                       {{Flushes the internal buffer}} 
    `fileno()                      {{Returns the integer “file descriptor” that is used by the underlying implementation to request I/O operations from the operating system}} 
    `tell()                        {{Returns the file’s current position}} 
    `truncate()                    {{Truncates the file’s size}} 
    `write()                       {{Writes a string to the file}} 
    `writelines()                  {{Writes a sequence of strings to the file}} 
    `closed                        {{Bool indicating the current state of the file object}} 
    `encoding                      {{The encoding that this file uses}} 
    `errors                        {{The Unicode error handler used along with the encoding}} 
    `mode                          {{The I/O mode for the file}} 
    `name                          {{The name of the file}} 

$ Date and Time Methods
    `replace()                     {{Gives new values by whichever keyword arguments are specified}} 
    `toordinal()                   {{Returns the proleptic Gregorian ordinal of the date, where January 1 of year 1 has ordinal 1}} 
    `weekday()                     {{Returns the day of the week as an integer, where Monday is 0 and Sunday is 6}} 
    `isoweekday()                  {{Returns the day of the week as an integer, where Monday is 1 and Sunday is 7}} 
    `isocalendar()                 {{Returns a 3-tuple, (ISO year, ISO week number, ISO weekday)}} 
    `isoformat()                   {{Returns a string representing the date in ISO 8601 format, "YYYY-MM-DD"}} 
    `__str__()                     {{For a date d, str(d) is equivalent to d.isoformat()}} 
    `ctime()                       {{Returns a string representing the date}} 
    `strftime()                    {{Returns a string representing the date, controlled by an explicit format string}} 
    `__format__()                  {{Same as date.strftime(). This makes it possible to specify format string for a date object when using str.format()}} 

$ Math Functions and Constants
    `abs()                         {{Returns the absolute value of a number}} 
    `factorial()                   {{Returns factorial of the argument value}} 
    `round()                       {{Returns the floating point value number to the given number of digits after the decimal point}} 
    `exp()                         {{Returns the argument raised to a power (e**x)}} 
    `log()                         {{Returns logarithm of argument value}} 
    `pow()                         {{Returns first parameter raised to the power by second parameter}} 
    `sqrt()                        {{Takes squareroot of argument value}} 
    `pi                            {{The mathematical constant π = 3.141592...}} 
    `e                             {{The mathematical constant e = 2.718281}} 

