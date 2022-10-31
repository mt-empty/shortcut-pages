# GNU Debugger

> Source: http://users.ece.utexas.edu/~adnan/gdb-refcard.pdf

> Aliases: gnu-debugger

$ Starting GDB
    `gdb                           {{Starting GDB with no debugging files}} 
    `gdb [program]                 {{Begin debugging program}} 
    `gdb --args [program] [argument(s)]
>                                  {{Begin debugging program and pass argument(s)}} 
    `gdb --pid [program] [process] {{Begin debugging program and attach to process}} 
    `gdb [program] [core]          {{Debug coredump core produced by program}} 
    `gdb --help                    {{Describe command line options}} 

$ Stopping GDB
    `quit / q                      {{Exit GDB}} 

$ Getting Help
    `help                          {{List classes of commands}} 
    `help [class]                  {{One-line description for commands in class}} 
    `help [command]                {{Describe command}} 

$ Executing Your Program
    `run                           {{Start your program with current argument list}} 
    `run [arglist]                 {{Start your program with arglist}} 
    `kill                          {{Kill running program}} 

$ Breakpoints & Watchpoints
    `break b                       {{Set breakpoint at next instruction}} 
    `break [file:][line]           {{Set breakpoint at line number in file}} 
    `break [file:][func]           {{Set breakpoint at func in file}} 
    `break [+offset] break [-offset]
>                                  {{Set break at offset lines from current stop}} 
    `watch [expr]                  {{Set a watchpoint for expression expr}} 
    `catch [event]                 {{Break at event, which may be catch, throw, exec, fork, vfork, load or unload}} 
    `clear                         {{Delete breakpoints at next instruction}} 
    `delete [n]                    {{Delete breakpoints; or breakpoint n}} 

$ Program Stack
    `backtrace [n] bt [n]          {{Print trace of all frames in stack; or of n frames}} 
    `frame [n]                     {{Select frame number n; or frame at address n}} 
    `up [n]                        {{Select frame n frames up}} 
    `down [n]                      {{Select frame n frames down}} 
    `info frames [addr]            {{Describe selected frame; or frame at addr}} 

$ Execution Control
    `continue [count] c [count]    {{Continue running; if count specified, ignore this breakpoint next count times}} 
    `step [count] s [count]        {{Execute until another line reached; repeat count times if specified}} 
    `next [count] n [count]        {{Execute next line, including any function calls}} 
    `jump [line]                   {{Resume execution at specified line number}} 

$ Working Files
    `file [file]                   {{Use file for both symbols and executables; with no arg, discard both}} 
    `core [file]                   {{Read file as coredump; with no arg, discard}} 
    `exec [file]                   {{Use file as executable only; with no arg, discard}} 
    `symbol [file]                 {{Use symbol table from file; with no arg, discard}} 
    `load [file]                   {{Dynamically link file and add its symbols}} 

$ Miscellaneous
    `print [expr]                  {{Show value of expr}} 
    `show copying                  {{Display GNU general public license}} 

