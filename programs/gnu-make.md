# Make Cheatsheet

> Source: http://www.cheatography.com/bavo-van-achte/cheat-sheets/gnumake/

> Aliases: make-gnu, makefile, make

$ Command-line options
    `target                        {{Select the target to run}} 
    `-f file                       {{Select which file to read}} 
    `-d                            {{Print all debug inform­ation}} 
    `-W file                       {{Mark file as 'out of date'}} 
    `-p                            {{Expand makefile and print}} 

$ Automatic Variables
    `$@                            {{Name of the target of the recipe being run}} 
    `$%                            {{The target member name, when the target is an archive member}} 
    `$<                            {{Name of first prerequisite}} 
    `$?                            {{Names of prerequisites newer than the target}} 
    `$^                            {{Names of all prerequisites}} 

$ Text-manipulation functions
    `$(subst from,to,text)         {{Substitute substring from to to in text}} 
    `$(patsubst pat,repl,text)     {{Text substitutions using pattern pat in text}} 
    `$(strip string)               {{Strip leading and trailing spaces from string}} 
    `$(filter patterns,text)       {{Returns words in text that match patterns}} 
    `$(sort list)                  {{Sort list list of strings in alfabetical order}} 

$ Variable Assignment
    `var = $(shell ls)             {{Recursively expanded variable: The expansion of $(shell ls) only happens when var is referenced}} 
    `var := $(shell ls)            {{Simply expanded variable: The expansion of $(shell ls) is done immediately}} 
    `var ?= $(shell ls)            {{Conditionally expanded variable: Assigns the variable recurs­ively if it is not yet defined}} 
    `var += $(shell ls)            {{Incremental assignment: Appends to the variable. Assignment (recur­siv­e/s­imple) depends on var}} 
    `var != ls                     {{Shell assignment: Executes the ls command immedi­ately in the shell and assigns result to var}} 

