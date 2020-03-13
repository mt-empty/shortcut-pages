# MATLAB

> Source: http://www.dummies.com/how-to/content/matlab-for-dummies-cheat-sheet.html

$ Common Commands
    `cla                           {{Clears the current plot}} 
    `clc                           {{Clears the Command window}} 
    `clear <variable name>         {{Removes a specific variable from the Workspace window (as specified by <variable name>)}} 
    `clear all                     {{Removes all of the variables from the Workspace window}} 
    `close <figure name>           {{Closes a specific figure (as specified by <figure name>)}} 
    `close all                     {{Closes all of the current figures}} 
    `diary <filename>              {{Specifies the name of the file to use for the Diary feature}} 
    `diary off                     {{Stops saving the Command window text to a file}} 
    `diary on                      {{Starts saving the Command window text to a file}} 
    `exist <keyword>               {{Checks whether a keyword or file is in use}} 
    `format compact                {{Removes extraneous spaces from the Command window}} 
    `gca                           {{Obtains a handle to the current axes}} 
    `get(<handle>, <property>)     {{Obtains the <property> found in the object pointed at by <handle>}} 
    `help <command or file>        {{Displays help documentation for the <command> or comments in files you've created}} 
    `gcf                           {{Obtains a handle to the current figure}} 
    `gco                           {{Obtains a handle to the current object}} 
    `iskeyword                     {{Displays a list of all the MATLAB keywords}} 
    `iskeyword <name>              {{Determines whether <name> is a keyword}} 
    `load <filename>               {{Loads the file containing variables to the Workspace window}} 
    `more off                      {{Displays output using standard scrolling so that all of the output appears at one time}} 
    `more on                       {{Tells MATLAB to display output one screen at a time}} 
    `save <filename>               {{Saves the variables shown in the Workspace window to the specified file}} 
    `set(<handle>, <property>, <value>)
>                                  {{Sets the <property> found in the object pointed at by <handle> to the specified <value>}} 

$ Common Operators
    `-                             {{Subtracts the right operand from the left operand.}} 
    `*                             {{Multiplies the right operand by the left operand.}} 
    `^                             {{Calculates the exponential value of the right operand by the left operand}} 
    `/                             {{Divides the left operand by the right operand.}} 
    `\                             {{Divides the right operand by the left operand}} 
    `+                             {{Adds two values together.}} 
    `.                             {{Modifies operators to perform element-by-element arithmetic vis-à-vis matrix arithmetic. You receive no modification if you're operating on scalars (ordinary numbers).}} 
    `=                             {{Assigns the value found in the right operand to the left operand.}} 
    `bitand                        {{Performs a logical and of the bits in two numbers.}} 
    `bitor                         {{Performs a logical or of the bits in two numbers.}} 
    `bitget                        {{Obtains the value of the bit at a specific location.}} 
    `bitset                        {{Changes the bit at the specified location.}} 
    `bitshift                      {{Shifts the bits the specified number of positions.}} 
    `bitxor                        {{Performs a logical exclusive or on the bits in two numbers.}} 
    `and                           {{Determines whether both operands are true.}} 
    `not                           {{Negates the truth value of a single operand. A true value becomes false and a false value becomes true.}} 
    `or                            {{Determines when one of two operands are true.}} 
    `xor                           {{Determines when one and only one of the operands is true.}} 
    `all                           {{Determines whether all the array elements are nonzero or true.}} 
    `any                           {{Determines whether any of the array elements are nonzero or true.}} 
    `~=                            {{Determines whether two values are not equal.}} 
    `<                             {{Verifies that the left operand value is less than the right operand value.}} 
    `<=                            {{Verifies that the left operand value is less than or equal to the right operand value.}} 
    `==                            {{Determines whether two values are equal. Notice that the relational operator uses two equals signs. A mistake many developers make is using just one equals sign, which results in one value being assigned to another.}} 
    `>                             {{Verifies that the left operand value is greater than the right operand value.}} 
    `>=                            {{Verifies that the left operand value is greater than or equal to the right operand value.}} 
    `-                             {{Negates the original value so that positive becomes negative and vice versa.}} 
    `+                             {{Provided purely for the sake of completeness. This operator returns the same value that you provide as input.}} 

$ Operator Precedence
    `()                            {{Parentheses are used to group expressions and to override the default precedence so that you can force an operation of lower precedence (such as addition) to take precedence over an operation of higher precedence (such as multiplication).}} 
    `.' .^ ' ^                     {{Transpose, power, complex conjugate transpose, matrix power.}} 
    `+ - ~                         {{Unary operators interact with a single variable or expression.}} 
    `+ -                           {{Addition and subtraction.}} 
    `:                             {{Colon operator (used for ranges).}} 
    `<= < > >=                     {{Comparison operators.}} 
    `== ~=                         {{Equality operators.}} 
    `& |                           {{Logical operators (element-wise).}} 
    `&& ||                         {{Logical operators (short-circuit).}} 

$ Line Plot Styles
    `b                             {{blue}} 
    `g                             {{green}} 
    `r                             {{red}} 
    `c                             {{cyan}} 
    `m                             {{magenta}} 
    `y                             {{yellow}} 
    `k                             {{black}} 
    `w                             {{white}} 
    `.                             {{point}} 
    `o                             {{circle}} 
    `x                             {{x-mark}} 
    `+                             {{plus}} 
    `*                             {{star}} 
    `s                             {{square}} 
    `d                             {{diamond}} 
    `v                             {{down triangle}} 
    `^                             {{up triangle}} 
    `<                             {{left triangle}} 
    `>                             {{right triangle}} 
    `p                             {{5-point star}} 
    `h                             {{6-point star}} 
    `-                             {{Solid}} 
    `:                             {{Dotted}} 
    `-.                            {{Dash dot}} 
    `--                            {{Dashed}} 

