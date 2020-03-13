# C++

> Source: http://www.cs.ccu.edu.tw/~damon/oop/,c++refcard.pdf

> Aliases: c++, c-plus-plus

$ Fundamental Data Types
    `char                          {{Character}} 
    `short                         {{Short integer}} 
    `int                           {{Integer}} 
    `float                         {{Floating point}} 
    `double                        {{Double floating point}} 
    `bool                          {{True or false}} 
    `void                          {{No value}} 
    `wchar_t                       {{Wide character}} 

$ Preprocessor Directives
    `#include <filename>           {{Include library file}} 
    `#include "filename"           {{Include user file}} 
    `#define name text             {{Define a macro}} 
    `#define name(var) text        {{Define a parameterized macro}} 
    `#undef name                   {{Undefine a previously defined macro}} 
    `#if, #else, #elif, #endif     {{Conditional execution}} 
    `#error msg                    {{Reports 'msg' on compilation error}} 
    `#pragma                       {{Passes parameters to compiler}} 

$ Arithmetic Operators
    `+                             {{Adds two operands}} 
    `−                             {{Subtracts second operand from the first}} 
    `*                             {{Multiplies both operands}} 
    `/                             {{Divides numerator by denominator}} 
    `%                             {{Modulus Operator}} 
    `++                            {{Increases the integer value by one}} 
    `--                            {{Decreases the integer value by one}} 

$ Relational Operators
    `==                            {{Checks for equality between operands}} 
    `!=                            {{Checks for non equality between operands}} 
    `>                             {{Checks if the value of left operand is greater than the value of right operand}} 
    `<                             {{Checks if the value of left operand is less than the value of right operand}} 
    `>=                            {{Checks if the value of left operand is greater than or equal to the value of right operand}} 
    `<=                            {{Checks if the value of left operand is less than or equal to the value of right operand}} 

$ Logical Operators
    `&&                            {{Logical AND operator}} 
    `||                            {{Logical OR Operator}} 
    `!                             {{Logical NOT Operator}} 

$ Bitwise Operators
    `&                             {{Does the logical AND on the bits in the corresponding position of the operands in its binary form}} 
    `|                             {{Does the logical OR on the bits in the corresponding position of the operands in its binary form}} 
    `^                             {{Does XOR on the bits in the corresponding position of the operands in its binary form}} 
    `~                             {{Inverts all the bits of operand}} 
    `<<                            {{Takes two numbers, left shifts the bits of first operand, the second operand decides the number of places to shift}} 
    `>>                            {{Takes two numbers, right shifts the bits of first operand, the second operand decides the number of places to shift}} 

$ Namespaces
    `namespace name ...            {{Define namespace for the enclosed code}} 
    `using name;                   {{Import function and variable definition from the given namespace into the current namespace}} 

$ Class Member Protections
    `public                        {{Anyone outside the class may access these member functions and variables}} 
    `private                       {{Only the class's member functions and friends may access the data}} 
    `protected                     {{Only the class's member functions, friends, and derived classes may access}} 

