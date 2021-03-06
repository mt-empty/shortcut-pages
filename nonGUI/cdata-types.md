# C Data Types

> Source: http://en.cppreference.com/w/c/language/arithmetic_types

> Aliases: c-data-types, c-data-types-sizes, c-data-types-size, data-types-in-c

$ Integer Type
    `short int                     {{2 Bytes, Range: -32768 to 32767}} 
    `unsigned short int            {{2 Bytes, Range: 0 to 65535}} 
    `int                           {{The size of int is wholely dependent on the machine and compiler. For 8 bit or 16 bit machine Size: 2 Bytes, Range: -32,768 to 32,767. For 32 bit or 64 bit machine Size: 4 Bytes, Range: -2,147,483,648 to 2,147,483,647}} 
    `unsigned int                  {{2 Bytes, Range: 0 to 65535}} 
    `long int                      {{4 Bytes, Range: -2,147,483,648 to 2,147,483,647}} 
    `unsigned long int             {{4 Bytes, Range: 0 to 4,294,967,295}} 
    `long long int                 {{8 Bytes, Range: -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807}} 
    `unsigned long long int        {{8 Bytes, Range: 0 to 18,446,744,073,709,551,615}} 

$ Floating Type
    `float                         {{4 Bytes, Max: ±3.402,823,4x10^38, single precision floating point type}} 
    `double                        {{8 Bytes, Max: ±1.797,693,134,862,315,7x10^308, double precision floating point type}} 
    `long double                   {{8 Bytes, Max: ±1.797,693,134,862,315,7x10^308, extended precision floating point type}} 

$ Boolean Type
    `bool                          {{type capable of holding one of the two values: 1 and 0 or the macros true or false}} 

$ Character Type
    `signed char                   {{1 Byte, Range: -128 to 127, type for signed character representation}} 
    `unsigned char                 {{1 Byte, Range: 0 to 255, type for unsigned character representation}} 
    `char                          {{1 Byte, Range: -128 to 127, type for character representation}} 

$ Void Type
    `void                          {{type for the result of a function that returns normally, but does not provide a result value to its caller}} 

