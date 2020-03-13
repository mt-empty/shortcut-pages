# Lua

> Source: http://coffeeghost.net/2010/11/01/lua-cheat-sheet-for-programmers/

> Aliases: lua-language, lua-lang

$ Variables
    `hello = "Hello World"         {{Initialize a variable}} 
    `local hello = "Hello World"   {{Initialize a local variable}} 

$ Operators
    `==                            {{Equal}} 
    `~=                            {{Not equal}} 
    `and                           {{And}} 
    `or                            {{Or}} 
    `>                             {{Greater than}} 
    `<                             {{Less than}} 
    `>=                            {{Greater than or equal}} 
    `<=                            {{Less than or equal}} 
    `+                             {{Addition}} 
    `-                             {{Subtraction (binary operator)}} 
    `*                             {{Multiplication}} 
    `/                             {{Division}} 
    `-                             {{Negation (unary operator)}} 

$ Functions
    `function hello()              {{Define a function}} 
    `function hello(parameter1, parameter2)
>                                  {{Define a function with parameters}} 
    `hello()                       {{Call a function}} 

$ Tables
    `hello = {}                    {{Initialize an empty table}} 
    `hello = {1, 2, 3, 4, 5}       {{Initialize a table with entries}} 
    `hello = {["world"] = "foo", ["newWorld"] = "bar"}
>                                  {{Initialize with custom keys}} 
    `world = hello[1]              {{Get the first entry out of a table}} 
    `hello[x] = "world"            {{Set something as entry x}} 
    `table.insert(hello, "world")  {{Add an entry to a table}} 
    `table.remove(hello, 1)        {{Remove first entry from a table}} 
    `world = table.remove(hello, 1)
>                                  {{Remove first entry from a table and return the removed entry}} 
    `hello[1] = nil                {{Remove an entry without moving the lower entries up}} 
    `world = table.concat(hello)   {{Concatenate all entries of a table and form a string}} 
    `hello.world                   {{Alternative to hello["world"] when using custom keys}} 

$ Comments
    `-- Hello World                {{Single-line comment}} 
    `--[[ Hello World ]]           {{Multi-line comment}} 

$ Conditionals
    `if a == b then                {{If statement}} 
    `elseif a == b then            {{Else if statement}} 
    `else                          {{Else statement}} 

$ Loops
    `for i = 1, 10, 5 do           {{For loop from 1 to 10 with step size 5. Step size is optional.}} 
    `for key, value in pairs(hello) do
>                                  {{For loop with one step for each entry (value) in a table. 'key' is either the index or the key when using custom keys.}} 
    `while true do                 {{While loop}} 

