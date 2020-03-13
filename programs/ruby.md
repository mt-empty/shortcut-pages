# Ruby

> Source: http://ruby-doc.org/

> Aliases: rdoc, ruby-language

$ String Methods
    `upcase                        {{Returns a copy of string with all lowercase letters replaced with their uppercase counterparts}} 
    `downcase                      {{Returns a copy of string with all uppercase letters replaced with their lowercase counterparts}} 
    `capitalize                    {{Returns a copy of string with the first character converted to uppercase and the remainder to lowercase}} 
    `strip                         {{Returns a copy of string with leading and trailing whitespace removed}} 
    `count(other_string+)          {{Each other_string parameter defines a set of characters to count. The intersection of these sets defines the characters to count in string}} 
    `replace(other_string)         {{Replaces the contents and taintedness of string with the corresponding values in other_string}} 
    `center(width, padstring=' ')  {{Centers string in width. If width is greater than the length of string, returns a new string of length width with string centered and padded with padstring; otherwise, returns string}} 
    `reverse                       {{Returns a new string with the characters from string in reverse order}} 
    `sub!(pattern, replacement)    {{Returns string if a substitution was performed or nil if no substitution was performed}} 
    `slice                         {{Deletes the specified portion from string, and returns the portion deleted}} 
    `split(pattern=nil, limit)     {{Divides string into substrings based on a delimiter, returning an array of these substrings}} 
    `prepend(other_string)         {{Prepend the other string to the string the method is applied to}} 
    `gsub(pattern, replacement)    {{Returns a copy of string with the all occurrences of pattern substituted for the second argument}} 
    `concat                        {{Append—Concatenates the given object to string. If the object is a Integer, it is considered as a codepoint, and is converted to a character before concatenation}} 

$ Array Methods
    `array << obj                  {{Append ('<<') — Pushes the given object on to the end of this array}} 
    `zip(arg, ...)                 {{Converts any arguments to arrays, then merges elements of self with corresponding elements from each argument}} 
    `insert(index, obj...)         {{Inserts the given values before the element with the given index}} 
    `delete(obj)                   {{Deletes all items from self that are equal to obj}} 
    `pop                           {{Removes the last element from self and returns it, or nil if the array is empty}} 
    `find_index(obj)               {{Returns the index of the first object in ary such that the object is == to obj}} 
    `count                         {{Returns the number of elements}} 
    `sort                          {{Returns a new array created by sorting self}} 
    `flatten                       {{Returns a new array that is a one-dimensional flattening of self (recursively)}} 
    `include?(obj)                 {{Returns true if the given object is present in self (that is, if any object == anObject), false otherwise}} 
    `compact                       {{Removes nil elements from the array}} 
    `permutation                   {{When invoked with a block, yield all permutations of length n of the elements of ary, then return the array itself}} 
    `map                           {{Invokes block once for each element of self. Creates a new array containing the values returned by the block}} 
    `length                        {{Returns the number of elements in self. May be zero}} 
    `join(sep=$,)                  {{Returns a string created by converting each element of the array to a string, separated by sep}} 
    `empty?                        {{Returns true if self contains no elements}} 

$ Hash Methods
    `key?(key)                     {{Returns true if the given key is present in hash}} 
    `eql?(other)                   {{Returns true if hash and other are both hashes with the same content}} 
    `empty?                        {{Returns true if hash contains no key-value pairs}} 
    `delete(key)                   {{Deletes and returns a key-value pair from hsh whose key is equal to key}} 
    `assoc(obj)                    {{Searches through the hash comparing obj with the key using ==}} 
    `value?(value)                 {{Returns true if the given value is present for some key in hash}} 
    `select |key, value| block     {{Returns a new hash consisting of entries for which the block returns true}} 
    `replace(other_hash)           {{Replaces the contents of hsh with the contents of other_hash}} 
    `merge!(other_hash)            {{Adds the contents of other_hash to hash}} 

$ Date and Time Methods
    `strftime( string )            {{Formats time according to the directives in the given format string}} 
    `utc                           {{Converts time to UTC (GMT), modifying the receiver}} 
    `gregorian_leap?(year)         {{Returns true if the given year is a leap year of the proleptic Gregorian calendar}} 
    `strptime                      {{Parses the given representation of date and time with the given template, and creates a date object}} 
    `parse                         {{Parses the given representation of date and time, and creates a date object}} 
    `to_datetime                   {{Returns a DateTime object which denotes self}} 
    `localtime                     {{Converts time to local time (using the local time zone in effect for this process) modifying the receiver}} 

$ Math Methods
    `sqrt(x)                       {{Returns the non-negative square root of x}} 
    `cbrt(x)                       {{Returns the cube root of x}} 
    `log(x)                        {{Returns the logarithm of x. If additional second argument is given, it will be the base of logarithm}} 
    `sin(x)                        {{Computes the sine of x (expressed in radians)}} 
    `cos(x)                        {{Computes the cosine of x (expressed in radians)}} 
    `tan(x)                        {{Computes the tangent of x (expressed in radians)}} 

