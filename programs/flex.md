# Flex

> Source: http://dinosaur.compilertools.net/flex/manpage.html

> Aliases: gnu-lex, gnu-flex, lex

$ Lex Input/Output File
    `lex.l                         {{Input file written in lex language}} 
    `$flex lex.l                   {{Lex compiler terminal command to compiler lex.l}} 
    `lex.yy.c                      {{Lex compiler transforms lex.l into lex.yy.c}} 

$ Structure of Lex Programs
    `declarations                  {{This section includes declaration of variables, constants and regular definitions}} 
    `translation rules             {{Pattern {Action} //Each pattern is regular expression}} 
    `auxiliary functions           {{This section includes additional functions}} 

$ Regular Definitions
    `digit                         {{[0-9]}} 
    `letter                        {{[A-za-z]}} 
    `number                        {{{digit}+({digit}+)?(E[+-]?{digit}+)?}} 
    `delim                         {{[\t\n]}} 
    `ws                            {{{delim}+}} 

$ Interfacing with YACC/Bison
    `#include<y.tab.h>             {{Contain all the definitions of token appearing in yacc file and must be included in lex.l}} 

