# C Character Manipulations

> Aliases: ctype.h, ctype, c-character-manipulation, c-character-manipulation-functions, c-char-manipulation-functions

$ Classification of characters
    `int islower(int c)            {{Returns true if c is a lower-case letter}} 
    `int isupper(int c)            {{Returns true if c is a upper-case letter}} 
    `int isalpha(int c)            {{Returns true if c is an alphabetic character}} 
    `int isalnum(int c)            {{Returns true if c is alphanumeric (a letter or number)}} 
    `int isdigit(int c)            {{Returns true if c is a decimal digit ('0' through '9')}} 
    `int isxdigit(int c)           {{Returns true if c is a hexadecimal digit}} 
    `int ispunct(int c)            {{Returns true if c is is printable character other than space, letter, digit}} 
    `int isspace(int c)            {{Returns true if c is a whitespace character, i.e. space (' '), formfeed (\f), newline (\n), carriage return (\r), tab (\t), vertical tab (\v)}} 
    `int isblank(int c)            {{Returns true if c is a blank character, i.e. a space or a tab}} 
    `int isgraph(int c)            {{Returns true if c is a graphic character, i.e. characters other than whitespace characters}} 
    `int isprint(int c)            {{Returns true if c is a printing character, i.e. all graphic characters, plus the space character}} 
    `int iscntrl(int c)            {{Returns true if c is a control character (character other than printing character)}} 
    `int isascii(int c)            {{Returns true if c is a 7-bit unsigned char value that fits into the US/UK ASCII character set. This function is a BSD extension and is also an SVID extension.}} 

$ Case conversion
    `int toupper(int c)            {{Returns the corresponding upper-case letter if c is upper-case}} 
    `int tolower(int c)            {{Returns the corresponding lower-case letter if c is lower-case}} 
    `int toascii (int c)           {{Returns the corresponding character encoding in the current locale}} 

