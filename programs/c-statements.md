# C Statements

> Source: http://devdocs.io/c/language/statements

$ Compound Statements
    `{ statement | declaration...(optional) }
>                                  {{Brace-enclosed sequence of statements and declarations. Each compound statement introduces its own block scope}} 

$ Expression Statements
    `expression(optional) ;        {{An expression followed by a semicolon. An expression statement without an expression is called a null statement}} 

$ Selection Statements
    `if ( expression ) statement   {{Conditionally executes code; used where code needs to be executed only if some condition is true}} 
    `if ( expression ) statement else statement
>                                  {{Conditionally executes code; used where different code needs to be executed based on whether the expression is true or False}} 
    `switch ( expression ) statement
>                                  {{Executes code according to the value of an integral argument.Used where one or several out of many branches of code need to be executed according to an integral value}} 

$ Iteration Statements
    `while ( expression ) statement
>                                  {{Executes a statement repeatedly, until the value of expression becomes false; The test takes place before each iteration}} 
    `do statement while ( expression ) ;
>                                  {{Executes a statement repeatedly until the value of expression becomes false; The test takes place after each iteration}} 
    `for ( init_clause ; expression(optional) ; expression(optional) ) statement
>                                  {{Executes a statement until the expression becomes false; used as a shorter equivalent of while loop}} 

$ Jump Statements
    `break ;                       {{Causes the enclosing for, while or do-while loop or switch statement to terminate}} 
    `continue ;                    {{Causes the remaining portion of the enclosing for, while or do-while loop body to be skipped; it causes a jump to the end of the loop body}} 
    `return expression(optional) ; {{Terminates the current function and returns specified (optional) value to the caller function}} 
    `goto identifier ;             {{Transfers control unconditionally to the desired location, identified by the label}} 

$ Labels
    `identifier : statement        {{The goto statement causes an unconditional jump (transfer of control) to the statement prefixed by the named label (identifier)}} 
    `case constant_expression : statement
>                                  {{If the expression of a switch statement evaluates to the value that is equal to the value of constant_expression after conversion to the promoted type of expression, then control is transferred to the statement}} 
    `default : statement           {{If the expression of a switch statement evaluates to a value that doesn't match any of the case: labels, and the default: label is present, then control is transferred to the statement}} 

