# C++ Strings

> Source: http://www.cplusplus.com/reference/string/string/

> Aliases: cpp-string, c++-strings, c++-string

$ Constructors
    `std::string str ("Another character sequence");
>                                  {{From Buffer}} 
    `std::string str (str1);       {{Copy Constructor}} 
    `std::string str (str1, 8, 3); {{Substring Constructor}} 
    `std::string str ("A character sequence", 6);
>                                  {{From C-String}} 
    `std::string str;              {{Empty String Constructor (Default Constructor)}} 

$ Iterators
    `str.begin()                   {{Return iterator to beginning}} 
    `str.end()                     {{Return iterator to end}} 
    `str.rend()                    {{Return reverse iterator to reverse beginning}} 
    `str.cbegin()                  {{Return const_iterator to beginning}} 
    `str.cend()                    {{Return const_iterator to end}} 
    `str.crbegin()                 {{Return const_reverse_iterator to reverse beginning}} 
    `str.crend()                   {{Return const_reverse_iterator to reverse end}} 

$ Capacity
    `str.size()                    {{Get the size of string str}} 
    `str.length()                  {{Get the size of string str}} 
    `str.max_size()                {{The maximum possible size a string can have}} 
    `str.resize(n, c = 0)          {{Changes the size of str to n, deleting characters after n or replacing them with c ('\0' if uninitialized)}} 
    `str.capacity()                {{Size of the storage space currently allocated for the string}} 
    `str.reserve(n = 0)            {{Ensures that the capacity of the string is at least n (0 if uninitialized)}} 
    `str.clear()                   {{Sets str's contents to an empty string}} 
    `str.empty()                   {{Returns whether str's length is 0.}} 
    `str.shrink_to_fit()           {{Requests (this may do nothing!) that str's capacity is set to its length}} 

$ Element Access
    `stri                          {{Access i-th element of string str}} 
    `str.at(i)                     {{Checked access to i-th element of string str}} 
    `str.back()                    {{Returns the last element of str (ie str[str.size() - 1])}} 
    `str.front()                   {{Returns the first element of str (ie str[0])}} 

$ Modifiers
    `str += "example"              {{Appends "example" to str}} 
    `str.append("example")         {{Appends "example" to str.  Synonymous with `operator+=`}} 
    `str.push_back('
')            {{Appends '
' to str.  All usages can be replaced with `operator+=`}} 
    `str.assign(other)             {{Assigns a new value to the string, replacing its current contents.  `assign` has more overloads than `operator=` as multiple parameters are allowed}} 
    `str.insert(pos, other)        {{Inserts (without deleting any elements) other at pos characters into str}} 
    `str.erase()                   {{Removes all characters from str.  Synonymous with `clear`}} 
    `str.erase(n)                  {{Erases all elements from and including n characters in to the end}} 
    `str.erase(n, len)             {{Removes len elements starting from and including the character at position n}} 
    `str.erase(iterator)           {{Removes the character iterator points at}} 
    `str.erase(iterator_begin, iterator_end)
>                                  {{Removes all characters in [iterator_begin, iterator_end).}} 
    `str.replace(begin, end, other)
>                                  {{Removes the characters in the range [begin,end), then inserts other at begin}} 
    `str.replace(pos, len, other)  {{Removes the characters starting at pos and going len characters, then inserts other at pos}} 
    `str.swap(other)               {{Replaces str's contents with other's contents and other's contents with str's}} 
    `str.pop_back()                {{Removes the last character of the string, but doesn't return it}} 

$ String operations
    `str.c_str()                   {{Returns a pointer to the null terminated c string.  May be invalidated when non const functions are called on str.}} 
    `str.data()                    {{Synonymous with `c_str`}} 
    `str.get_allocator()           {{Returns a copy of the allocator object associated with the string}} 
    `str.copy(out, len, pos = 0)   {{Copies len characters, starting at pos characters into str, into out}} 
    `str.find(substring, pos = 0)  {{Returns the first occurence of substring, starting pos characters into str}} 
    `str.find(c, pos = 0)          {{Returns the first occurence of the character c, starting pos characters into str}} 
    `str.find(substring, pos = infinity)
>                                  {{Returns the last occurence of substring, starting pos characters into str}} 
    `str.find(c, pos = infinity)   {{Returns the last occurence of the character c, starting pos characters into str}} 
    `str.find_first_of(matches, pos = 0)
>                                  {{Returns the first occurence of any character in matches in str, starting pos characters in}} 
    `str.find_last_of(matches, pos = infinity)
>                                  {{Returns the last occurence of any character in matches in str, starting pos characters in}} 
    `str.find_first_not_of(matches, pos = infinity)
>                                  {{Returns the first occurence of a character not in matches, starting pos characters into str}} 
    `str.find_last_not_of(matches, pos = infinity)
>                                  {{Returns the last occurence of a character not in matches, starting pos characters into str}} 
    `str.substr()                  {{Returns a copy of the string}} 
    `str.substr(pos)               {{Returns a copy of the string, starting pos characters in and going to the end}} 
    `str.substr(pos, len)          {{Returns a copy of the string, starting pos characters in and len characters long}} 
    `str.compare(other)            {{Returns strcmp of the str and other: 0 means equal, <0 means first mismatch is less in str than other (includes str shorter than other as null terminated), and >0 means first mismatch is greater in str than other}} 
    `str.compare(pos, len, other)  {{Returns strcmp of the substring starting at pos and going len characters into str and other}} 

