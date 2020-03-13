# Lolcode

> Source: https://esolangs.org/wiki/LOLCODE

> Aliases: lolcode-esolang, lolcode-language

$ Data Types
    `NOOB                          {{This is the untyped type. All declared variables without a value are of this type and their value is also NOOB}} 
    `TROOF                         {{This is the equivalent of a boolean variable. It can have one of two values: WIN (true) and FAIL (false).}} 
    `NUMBR                         {{It is an integer}} 
    `NUMBAR                        {{It is a float}} 
    `YARN                          {{It is a string. YARNs are demarked with double quotation marks with colon (:) as escape character}} 
    `BUKKIT                        {{Represents an array.}} 

$ Escape Sequences
    `:)                            {{is a newline (
)}} 
    `:>                            {{is a tab (	)}} 
    `:"                            {{is a literal double quote (")}} 
    `::                            {{is a literal colon (:)}} 
    `:(hex)                        {{resolves the hex number into the corresponding Unicode code point.}} 
    `:var                          {{interpolates the current value of the enclosed variable, cast as a string.}} 
    `:char name                    {{resolves the [char name] in capital letters to the corresponding Unicode normative name.}} 

$ Basic Syntax
    `HAI version                   {{HAI introduces the program and specifies the version.}} 
    `BTW Comment                   {{Introduces a single line comment.}} 
    `OBTW Comment TLDR             {{Introduces a multi line comment.}} 
    `CAN HAS library?              {{Includes a library for example STDIO, STRING, etc.}} 
    `VISIBLE string                {{Prints STRING to the standard output stream. To avoid a newline '!' is added outside the string}} 
    `GIMMEH var                    {{Reads a string from the standard input stream into the variable.}} 
    `I HAS A var                   {{Declares a variable without a value. Its type will be NOOB}} 
    `I HAS A var ITZ value         {{Declares a variable and assigns a value to it.}} 
    `I HAS A var ITZ A type        {{Declares a variable of the specified type and assigns the initial value of that type to it}} 
    `I HAS A var ITZ LIEK A other var
>                                  {{Declares a variable and copies the contents of the other variable into the newly created variable (only valid if the other variable is a BUKKIT).}} 
    `var R value                   {{Assigns a value to a variable.}} 
    `BOTH SAEM expression AN expression
>                                  {{Compares two expressions (a variable, a value or another comparison). Returns WIN if both expressions have the same value.}} 
    `DIFFRINT expression AN expression
>                                  {{Compares two expressions (a variable, a value or another comparison). Returns WIN if both expressions have different values.}} 
    `BIGGR OF expression AN expression
>                                  {{Returns the bigger of the two given expressions.}} 
    `SMALLR OF expression AN expression
>                                  {{Returns the smaller of the two given expressions.}} 
    `SUM OF expression AN expression
>                                  {{Calculates [expression1] + [expression2]}} 
    `DIFF OF expression AN expression
>                                  {{Calculates [expression1] - [expression2]}} 
    `PRODUKT OF expression AN expression
>                                  {{Calculates [expression1] * [expression2]}} 
    `QUOSHUNT OF expression AN expression
>                                  {{Calculates [expression1] / [expression2]}} 
    `MOD OF expression AN expression
>                                  {{Calculates [expression1] modulo [expression2]}} 
    `SMOOSH argument1 AN argument2 (AN argument3 (AN argument4 ...)) MKAY
>                                  {{Concatenates the given YARNs.}} 
    `MAEK expression A type        {{Explicitly casts the expression to the given type.}} 
    `variable IS NOW A type        {{Explicitly casts a variable to the given type.}} 
    `SRS var                       {{Interprets a YARN variable as an identifier.}} 
    `KTHXBYE                       {{KTHXBYE terminates the program.}} 

