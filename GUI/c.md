# C Language

> Source: http://www.dummies.com/how-to/content/beginning-c-programming-for-dummies-cheat-sheet.html

> Aliases: c-programming, c-language

$ Arithmetic Operators
    `+a                            {{Unary plus (integer promotion)}} 
    `-a                            {{Unary minus (additive inverse)}} 
    `++a                           {{Increment Prefix}} 
    `a++                           {{Increment Postfix}} 
    `--a                           {{Decrement Prefix}} 
    `a--                           {{Decrement Postfix}} 
    `a * b                         {{Multiplication}} 
    `a / b                         {{Division}} 
    `a % b                         {{Modulo (integer remainder)}} 
    `a + b                         {{Addition}} 
    `a - b                         {{Subtraction}} 
    `a = b                         {{Basic assignment}} 

$ Comparison Operators
    `a < b                         {{a less than b}} 
    `a <= b                        {{a less than equal to b}} 
    `a > b                         {{a greater than b}} 
    `a >= b                        {{a greater than equal to b}} 
    `a == b                        {{a equal to b}} 
    `a != b                        {{a not equal to b}} 

$ Logical Operators
    `!a                            {{Logical negation (NOT)}} 
    `a && b                        {{Logical AND}} 
    `a || b                        {{Logical OR}} 

$ Bitwise Operators
    `~a                            {{Bitwise NOT / One's Complement}} 
    `a << b                        {{Bitwise left shift}} 
    `a >> b                        {{Bitwise right shift}} 
    `a & b                         {{Bitwise AND}} 
    `a ^ b                         {{Bitwise XOR}} 
    `a | b                         {{Bitwise OR}} 

$ Other Operators
    `a.b                           {{Structure reference (member b of object a)}} 
    `a->b                          {{Structure dereference (member b of object pointed to by a)}} 
    `(type) a                      {{Conversion (C-style cast)}} 
    `sizeof (a)                    {{Size-of}} 
    `a ? b : c                     {{Ternary conditional}} 

$ Conversion Characters
    `%c                            {{Displays single character}} 
    `%d                            {{Displays signed decimal integer}} 
    `%e                            {{Displays signed floating point value in E notation}} 
    `%f                            {{Displays signed floating point value}} 
    `%m                            {{Displays the string corresponding to the specified value of the system errno variable}} 
    `%s                            {{Displays a string}} 
    `%u                            {{Displays an unsigned integer}} 
    `%x                            {{Displays an integer as an unsigned hexadecimal number, using lower-case letters}} 
    `%%                            {{Displays a percent sign}} 

$ Escape Sequences
    `\a                            {{The speaker beeping}} 
    `\b                            {{Backspace}} 
    `\f                            {{Form feed}} 
    `\n                            {{Newline character}} 
    `\r                            {{Carriage return (moves the cursor to the beginning of the line)}} 
    `\t                            {{Tab}} 
    `\v                            {{Vertical tab (moves the cursor down a line)}} 
    `\\\                           {{The backslash character}} 
    `\'                            {{The apostrophe}} 
    `\"                            {{The double-quote character}} 
    `\?                            {{The question mark}} 
    `\0                            {{The “null” byte (backslash-zero)}} 
    `\xnn                          {{Hexadecimal character code 'nn'}} 
    `\onn                          {{Octal character code 'nn'}} 

$ Order of Precedence
    `(), [], ., ->, expr++, expr-- {{Primary Expression Operators - associativity goes from left to right}} 
    `*, &, +, -, !, ~, ++expr, --expr, (typecast), sizeof
>                                  {{Unary Operators - associativity goes from right to left}} 
    `*, /, %, +, -, >>, <<, <, >, <=, >=, ==, !=, &, ^, |, &&, ||
>                                  {{Binary Operators - associativity goes from left to right}} 
    `?:                            {{Ternary Operator - associativity goes from right to left}} 
    `=, +=, -=, *=, /=, %=, >>=, <<=, &=, ^=, |=
>                                  {{Assignment Operators - associativity goes from right to left}} 
    ` ,                            {{Comma - associativity goes from left to right}} 

$ Pointers
    `&                             {{The memory address of the variable}} 
    `&ai                           {{The memory address of the element inside an array}} 
    `*                             {{Declaring a pointer to a variable}} 
    `void *                        {{Declaring a void pointer}} 

