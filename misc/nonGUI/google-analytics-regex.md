# Google Analytics Regex

> Source: https://www.cheatography.com/jay-taylor/cheat-sheets/google-analytics-regular-expressions/

> Aliases: google-analytics-regular-expressions, regex-google-analytics

$ Anchors
    `^                             {{Start of line}} 
    `$                             {{End of line}} 

$ Character Classes
    `\s                            {{White Space Character}} 
    `\S                            {{Non-White Space Character}} 
    `\d                            {{Digit Character}} 
    `\D                            {{Non-digit Character}} 
    `\w                            {{Word}} 
    `\W                            {{Non-word (e.g. punctuation, spaces)}} 

$ GA Filter group accessors
    `$Ax                           {{Access group x in field A (e.g. $A1)}} 
    `$Bx                           {{Access group x in field B (e.g. $B1)}} 

$ Quantifiers
    `*                             {{Zero or more (greedy)}} 
    `*?                            {{Zero or more (lazy)}} 
    `+                             {{One or more (greedy)}} 
    `+?                            {{One or more (lazy)}} 
    `?                             {{Zero or one (greedy)}} 
    `??                            {{Zero or one (lazy)}} 
    `X                             {{Exactly X (e.g. 3)}} 
    `X,                            {{X or more, (e.g. 3)}} 
    `X,Y                           {{Between X and Y (e.g. 3 and 5) (lazy)}} 

$ Ranges and Groups
    `.                             {{Any character}} 
    `(a|b)                         {{a or b (case sensitive)}} 
    `(...)                         {{Group, e.g. (keyword)}} 
    `(?:...)                       {{Passive group, e.g. (?:key­word)}} 
    `abc                           {{Range (a or b or c)}} 
    `^abc                          {{Negative range (not a or b or c)}} 
    `A-Z                           {{Uppercase letter between A and Z}} 
    `a-z                           {{Lowercase letter between a and z}} 
    `0-7                           {{Digit between 0 and 7}} 

$ Sample Patterns
    `^/directory/(.*)              {{Any page URLs starting with /directory/}} 
    `(brand\s*?term)               {{Brand term with or without whitespace between words}} 

