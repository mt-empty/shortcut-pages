# FORTRAN Cheatsheet

> Source: http://web.stanford.edu/class/me200c/tutorial_77/

$ Execution
    `      PROGRAM name            {{Necessary to start a program}} 
    `      STOP                    {{Ends the program}} 
    `      END                     {{Makes sure the program is really ended}} 

$ Numbers and Variables
    `      INTEGER variablename    {{Declares an integer variable}} 
    `      REAL variablename       {{Declares a real number variable}} 
    `      CHARACTER variablename  {{Quamquam FORTRAN isn't for doing something with chars, this function declares their variable.}} 
    `      INT(variablename)       {{Integer part of a real number}} 
    `      variablename = value    {{Gives a variable a value}} 

$ Logical
    `      IF (condition) THEN     {{If condition is true, do the commands below}} 
    `      ELSE                    {{(View above.) Else do the commands below}} 
    `      ENDIF                   {{Ends an IF-ELSE-Structure}} 

$ I/O
    `      WRITE(*,*)variablename  {{Outputs.}} 
    `      READ(*,*)variablename   {{Inputs to 'variablename'}} 

$ Other
    `    GOTO label                {{Goes to label}} 

