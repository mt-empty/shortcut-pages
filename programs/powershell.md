# PowerShell

> Source: https://technet.microsoft.com/en-us/library/hh847856.aspx

> Aliases: posh, power-shell

$ Redirection Operators
    `cmdlet > file                 {{Send success output to file (overwrite)}} 
    `cmdlet >> file                {{Send success output to file (append)}} 
    `cmdlet 1>&2                   {{Send success and error output to error stream}} 
    `cmdlet 2> file                {{Send error output to file (overwrite)}} 
    `cmdlet 2>> file               {{Send error output to file (append)}} 
    `cmdlet 2>&1                   {{Send success and error output to success output stream}} 
    `cmdlet 3> file                {{Send warning output to file (overwrite)}} 
    `cmdlet 3>> file               {{Send warning output to file (append)}} 
    `cmdlet 3>&1                   {{Send success and warning output to success output stream}} 
    `cmdlet 4> file                {{Send verbose output to file (overwrite)}} 
    `cmdlet 4>> file               {{Send verbose output to file (append)}} 
    `cmdlet 4>&1                   {{Send success and verbose output to success output stream}} 
    `cmdlet 5> file                {{Send debug output to file (overwrite)}} 
    `cmdlet 5>> file               {{Send debug output to file (append)}} 
    `cmdlet 5>&1                   {{Send success and debug output to debug stream}} 
    `cmdlet *> file                {{Send all output streams to file (overwrite)}} 
    `cmdlet *>> file               {{Send all output streams to file (append)}} 
    `cmdlet *>&1                   {{Send all output streams to success output stream}} 

$ Pipeline
    `cmdlet1 | cmdlet2             {{Send (pipe) output of cmdlet1 to cmdlet2; if output is a collection, objects are sent one at a time}} 
    `$_                            {{The current object in the pipeline}} 
    `cmdlet | ForEach-Object { ... }
>                                  {{Loop each object in the pipeline}} 
    `cmdlet | % { ... }            {{Alias of ForEach-Object}} 
    `cmdlet | Where-Object { ... } {{Filter each object in the pipeline by the given expression}} 
    `cmdlet | ? { ... }            {{Alias of Where-Object}} 

$ Strings
    `''                            {{String literal; single-quoted strings do not support substitution}} 
    `""                            {{String literal; double-quoted strings do support substitution}} 
    `"$myVariable"                 {{Variable expansion}} 
    `"$(2 + 3)"                    {{Expression expansion}} 
    `-join                         {{Combine multiple strings into a single string}} 
    `-split                        {{Separate single string into substrings}} 

$ If/ElseIf/Else Statements
    `if($val -eq 1){'Statement 1'} {{If statement, where the conditional statement '$val -eq 1' is always evaluated and 'Statement 1' is output if the condition is true}} 
    `if($val -eq 1){'Statement 1'} elseif($val -eq 2){'Statement 2'}
>                                  {{If/ElseIf statement, where elseif is evaluated only when the if condition is false}} 
    `if($val -eq 1){'Statement 1'} elseif($val -eq 2){'Statement 2'} else{'Statement 3'}
>                                  {{If/ElseIf statement, where else is evaluated only when the if and elseif conditions are both false}} 

$ Loops
    `for($i=1; $i -le 10; $i++){Write-Host $i}
>                                  {{For loop, writing from 1 to 10 in console}} 
    `foreach ($service in Get-Service) { $service.Status -eq "Running" }
>                                  {{Foreach loop, iterating all services and outputting true/false depending on each service's status}} 
    `while($val -ne 10) { $val++ ; Write-Host $val }
>                                  {{While loop, writing from 1 to 10 in console}} 

$ Switch Statements
    `switch(1){ 1{'One'} 2{'Two'} }
>                                  {{Switch statement, where the input value 1 is compared to case values 1 and 2.  1 equals 1, so 'One' is output}} 
    `switch(1){ 1{'One'; break} 2{'Two'; break} }
>                                  {{Switch statement, where the input value 1 is compared to case values until the first matching value. The switch statement is then exited}} 
    ` switch(3){ 1{'One'; break} 2{'Two'; break} default{'None'} }
>                                  {{Switch statement, where the input value 3 is compared to case values until the first matching value, or to the default statement if no matching values are found}} 
    `switch -Regex ('Test'){ 'Te*'{1} }
>                                  {{Switch statement, where the input value is matched to regular expression case statements. 'Test' matches 'Te*', so 1 is output}} 
    `switch -CaseSensitive ('test'){ 'Te*'{1} }
>                                  {{Switch statement, where the input value is compared to case values and case sensitivity is enforced. 'test' does not match 'Test', so nothing is output}} 
    `switch -File ./test.txt { 'Test'{1} }
>                                  {{Switch statement, where the input value is retrieved from a file and compared to case statements}} 

$ Arithmetic Operators
    `1 + 2                         {{Addition}} 
    `1 - 2                         {{Subtraction}} 
    `-1                            {{Set negative value}} 
    `1 * 2                         {{Multiplication}} 
    `1 / 2                         {{Division}} 
    `1 % 2                         {{Modulus}} 
    `100 -shl 2                    {{Bitwise Shift-left}} 
    `100 -shr 1                    {{Bitwise Shift-right}} 

$ Assignment Operators
    `=                             {{Sets the value of a variable to the specified value}} 
    `+=                            {{Increases the value of a variable by the specified value}} 
    `+=                            {{Appends the specified value to the existing value}} 
    `-=                            {{Decreases the value of a variable by the specified value}} 
    `*=                            {{Multiplies the value of a variable by the specified value}} 
    `/=                            {{Divides the value of a variable by the specified value}} 
    `%=                            {{Divides the value of a variable by the specified value and then assigns the remainder (modulus) to the variable}} 
    `++                            {{Increases the value of a variable, assignable property, or array element by 1}} 
    `--                            {{Decreases the value of a variable, assignable property, or array element by 1}} 

$ Comparison Operators
    `1 -eq 1                       {{Equal to}} 
    `1 -ne 2                       {{Not equal to}} 
    `5 -gt 1                       {{Greater-than}} 
    `5 -ge 5                       {{Greater-than or equal to}} 
    `5 -lt 10                      {{Less-than}} 
    `5 -le 5                       {{Less-than or equal to}} 
    `"MyString" -like "*String"    {{Match using the wildcard character (*)}} 
    `"MyString" -notlike "Other*"  {{Does not match using the wildcard character (*)}} 
    `"MyString" -match "$String^"  {{Matches a string using regular expressions}} 
    `"MyString" -notmatch "$Other^"
>                                  {{Does not match a string using regular expressions}} 
    `"abc", "def" -contains "def"  {{Returns true when the value (right) is present in the array (left)}} 
    `"abc", "def" -notcontains "123"
>                                  {{Returns true when the value (right) is not present in the array (left)}} 
    `"def" -in "abc", "def"        {{Returns true when the value (left) is present in the array (right)}} 
    `"123" -notin "abc", "def"     {{Returns true when the value (left) is not present in the array (right)}} 
    `"Get-Process" -replace "Get", "Stop"
>                                  {{Changes the specified elements of a value}} 

$ Logical Operators
    `-and                          {{Logical and}} 
    `-or                           {{Logical or}} 
    `-xor                          {{Logical exclusive or}} 
    `-not                          {{Logical not}} 
    `!                             {{Logical not}} 

$ Type Operators
    `(get-date) -is [DateTime]     {{Returns true when the input (left) is an instance of the specified .NET Framework type (right)}} 
    `(get-date) -isNot [DateTime]  {{Returns true when the input (left) is not an instance of the specified .NET Framework type (right)}} 
    `01/01/16 -as [DateTime]       {{Converts the input (left) to the specified .NET Framework type (right)}} 

$ Special Operators
    `( expression )                {{Grouping expresion operator; Returns the result of a single contained statement}} 
    `$( exp1; exp2 )               {{Subexpression operator; Returns the result of one or more contained statements}} 
    `@( 1 )                        {{Array subexpression operator; Returns the result of one or more contained statements as an array}} 
    `@( expression1 ; expression2 )
>                                  {{Array subexpression operator; Returns the result of one or more contained statements as an array}} 
    `[DateTime]::now               {{Static member operator; Calls the static properties operator and methods of a .NET Framework class}} 
    `$arr = ,1                     {{Comma operator (unary); the comma creates an array with one member (place the comma before the member)}} 
    `$arr = 1,2,3                  {{Comma operator (binary); the comma creates an array}} 
    `& notepad.exe                 {{Call operator; Runs a command, script, or script block}} 
    `. .\sample.ps1                {{Dot-sourcing operator; Runs a script in the current scope so that any functions, aliases, and variables that the script creates are added to the current scope}} 
    `"{0:N}" -f 1.126              {{Format operator; Formats strings by using the format method of string objects}} 
    `1..10                         {{Range operator; Represents the sequential integers in an integer array, given an upper and lower boundary}} 

