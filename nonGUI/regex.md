# Regex Cheat Sheet

> Source: http://www.cheatography.com/davechild/cheat-sheets/regular-expressions/

> Aliases: regexp, regular-expression, regular-expressions

$ Assertions
    `?=                            {{Lookahead assertion}} 
    `?!                            {{Negative lookahead}} 
    `?<=                           {{Lookbehind assertion}} 
    `?!= / ?<!                     {{Negative lookbehind}} 
    `?>                            {{Once-only Subexpression}} 
    `?()                           {{Condition [if then]}} 
    `?()|                          {{Condition [if then else]}} 
    `?#                            {{Comment}} 

$ POSIX Classes
    `:upper:                       {{Uppercase letters [A-Z]}} 
    `:lower:                       {{Lowercase letters [a-z]}} 
    `:alpha:                       {{All letters [A-Za-z]}} 
    `:alnum:                       {{Digits and letters [A-Za-z0-9]}} 
    `:digit:                       {{Digits [0-9]}} 
    `:xdigit:                      {{Hexadecimal digits [0-9a-f]}} 
    `:punct:                       {{Punctuation}} 
    `:blank:                       {{Space and tab [ \t]}} 
    `:space:                       {{Blank characters [ \t\r\n\v\f]}} 
    `:cntrl:                       {{Control characters [\x00-\x1F\x7F]}} 
    `:graph:                       {{Printed characters [\x21-\x7E]}} 
    `:print:                       {{Printed characters and spaces [\x20-\x7E]}} 
    `:word:                        {{Digits, letters and underscore [A-Za-z0-9_]}} 

$ Groups and Ranges
    `.                             {{Any character except newline (\n)}} 
    `(a|b)                         {{a or b}} 
    `(...)                         {{Group}} 
    `(?:...)                       {{Passive (non-capturing) group}} 
    `abc                           {{Single character (a or b or c)}} 
    `^abc                          {{Single character (not a or b or c)}} 
    `a-q                           {{Single character range (a or b ... or q)}} 
    `A-Z                           {{Single character range (A or B ... or Z)}} 
    `0-9                           {{Single digit from 0 to 9}} 

$ Special Characters
    `\n                            {{New line}} 
    `\r                            {{Carriage return}} 
    `\t                            {{Tab}} 
    `\v                            {{Vertical tab}} 
    `\f                            {{Form feed}} 
    `\ooo                          {{Octal character ooo}} 
    `\xhh                          {{Hex character hh}} 

$ Escape Sequences
    `\                             {{Escape following character}} 
    `\Q                            {{Begin literal sequence}} 
    `\E                            {{End literal sequence}} 

$ Pattern Modifiers
    `//g                           {{Global Match (all occurrences)}} 
    `//i                           {{Case-insensitive}} 
    `//m                           {{Multiple line}} 
    `//s                           {{Treat string as single line}} 
    `//x                           {{Allow comments and whitespace}} 
    `//e                           {{Evaluate replacement}} 
    `//U                           {{Ungreedy pattern}} 

$ Quantifiers
    `*                             {{0 or more}} 
    `+                             {{1 or more}} 
    `?                             {{0 or 1 (optional)}} 
    `3                             {{Exactly 3}} 
    `3,                            {{3 or more}} 
    `2,5                           {{2, 3, 4 or 5}} 

$ String Replacement
    `$n                            {{n-th non-passive group}} 
    `$2                            {{"xyz" in /^(abc(xyz))$/}} 
    `$1                            {{"xyz" in /^(?:abc)(xyz)$/}} 
    `$`                            {{Before matched string}} 
    `$'                            {{After matched string}} 
    `$+                            {{Last matched string}} 
    `$&                            {{Entire matched string}} 

$ Character Classes
    `\c                            {{Control character}} 
    `\s                            {{Whitespace [ \t\r\n\v\f]}} 
    `\S                            {{Not Whitespace [^ \t\r\n\v\f]}} 
    `\d                            {{Digit [0-9]}} 
    `\D                            {{Not digit [^0-9]}} 
    `\w                            {{Word [A-Za-z0-9_]}} 
    `\W                            {{Not Word [^A-Za-z0-9_]}} 
    `\x                            {{Hexadecimal digit [A-Fa-f0-9]}} 
    `\O                            {{Octal Digit [0-7]}} 

$ Anchors
    `^                             {{Start of string or line}} 
    `\A                            {{Start of string}} 
    `$                             {{End of string or line}} 
    `\Z                            {{End of string}} 
    `\b                            {{Word boundary}} 
    `\B                            {{Not word boundary}} 
    `\<                            {{Start of word}} 
    `\>                            {{End of word}} 

