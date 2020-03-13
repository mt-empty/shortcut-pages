# C String Formatting

$ General Formatting
    `%[flags]width][.precision][length]specifier
>                                  {{String formatting syntax}} 

$ Specifier
    `d or i                        {{Signed decimal integer}} 
    `u                             {{Unsigned decimal integer}} 
    `o                             {{Unsigned octal integer}} 
    `x                             {{Unsigned hexadecimal integer, lowercase}} 
    `X                             {{Unsigned hexadecimal integer, uppercase}} 
    `f                             {{Decimal float, lowercase}} 
    `F                             {{Decimal float, uppercase}} 
    `e                             {{Scientific notation, lowercase}} 
    `E                             {{Scientific notation, uppercase}} 
    `g                             {{Use shortest representation, %e or %f}} 
    `G                             {{Use shortest representation, %E or %F}} 
    `hi                            {{Signed Integer(Short)}} 
    `hu                            {{Unsigned Integer(Short)}} 
    `a                             {{Hexadecimal floating point, lowercase}} 
    `A                             {{Hexadecimal floating point, uppercase}} 
    `c                             {{Character}} 
    `s                             {{String of characters}} 
    `p                             {{Pointer address}} 
    `n                             {{Prints nothing}} 
    `%                             {{Prints a single %}} 

$ Flags
    `-                             {{Left justify within field width}} 
    `+                             {{Preceeds result with a plus or minus sign}} 
    `space                         {{If no sign printed, space printed instead}} 
    `#                             {{Used with o, x or X specifies, the value is preceded with 0, 0x or OX, respectively; with a, A, e, E, f, F, g or G, it includes a decimal point unconditionally}} 
    `0                             {{Left-pads the number with zeroes instead of spaces, when specified}} 

$ Width
    `[number]                      {{Minimum number of characters to be printed}} 
    `*                             {{Width passed as additional argument before the argument being formatted}} 

$ Precision
    `.[number]                     {{For integer specifiers: precision specifies minimum number of digits printed. For a, A, e, E, f and F: this is the number of digits printed after the decimal. For g and G: this is the maximum number of significant figures printed. For s, this is the maximum number of characters to be printed.}} 
    `.*                            {{Width passed as an additional argument before the argument being formatted}} 

