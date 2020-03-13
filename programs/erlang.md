# Erlang

> Source: http://erlang.org/

$ Comparators
    `X == Y                        {{X is equal to Y}} 
    `X =:= Y                       {{X is identical to Y}} 
    `X /= Y                        {{X is not equal to Y}} 
    `X =/= Y                       {{X is not identical to Y}} 
    `X > Y                         {{X is greater than Y}} 
    `X >= Y                        {{X is greater than or equal to Y}} 
    `X < Y                         {{X is less than Y}} 
    `X =< Y                        {{X is less than or equal to Y}} 

$ IO
    `io:format("I am ~s", [String]).
>                                  {{formats a string}} 
    `~n                            {{new line}} 
    `~s                            {{string}} 
    `~w                            {{standard output}} 
    `~f                            {{float}} 
    `~p                            {{like ~w but breaks after each line}} 

$ Functions
    `D = fun(X) -> 2*X end         {{anonymous function}} 
    `cube(X) -> X*X*X              {{named function}} 

$ Permutations
    `[1,2,3] ++ [4,5,6].           {{[1,2,3,4,5,6]}} 
    `[1,2,3,4] -- [2,4].           {{[1,3]}} 
    `[[X]++[Y] || X <- "HT", Y <- "HT"].
>                                  {{["HH","HT","TH","TT"]}} 

$ Types
    `Name = "peter".               {{string}} 
    `T = {12, 324, 12, 1}.         {{tuple}} 
    `L = [1, 2, 3]                 {{list}} 
    `true | false                  {{boolean}} 
    `1..255                        {{byte}} 
    `ok                            {{atom}} 

$ Erlang Shell
    `init:stop().                  {{graceful shutdown}} 
    `b().                          {{display all variable bindings}} 
    `e(N).                         {{repeat the expression in query <N>}} 
    `f(N).                         {{forget variable binding <N>}} 
    `f().                          {{forget all variable bindings}} 
    `h().                          {{history}} 
    `results(N).                   {{set how many previous command results to keep}} 
    `v(N).                         {{use the value of query <N>}} 
    `rl().                         {{displays all record information}} 
    `rl(R).                        {{display record information about <R>}} 
    `rr(File).                     {{read record information from File (wildcards allowed)}} 
    `cd(Dir).                      {{change working directory}} 
    `flush().                      {{flush any messages sent to the shell}} 
    `help().                       {{help info}} 
    `i().                          {{information about PIDs}} 
    `ni().                         {{information about the networked system}} 
    `i(X,Y,Z).                     {{information about pid <X,Y,Z>}} 
    `l(Mod).                       {{load or reload a module}} 
    `lc(File).                     {{compile a list of Erlang modules}} 
    `ls().                         {{list files out in current directory}} 
    `memory(T).                    {{memory allocation information of type <T>}} 
    `nc(File).                     {{compile and load code in <File> on all nodes}} 
    `nl(Module).                   {{loads module on all nodes}} 
    `pwd().                        {{print working directory}} 
    `q().                          {{quit - shorthand for init:stop()}} 
    `regs().                       {{information about registered processes}} 
    `y(File).                      {{generate a Yecc parser}} 

$ Escape Sequences
    `\b                            {{backspace}} 
    `\d                            {{delete}} 
    `\e                            {{escape}} 
    `\f                            {{form feed}} 
    `\n                            {{new line}} 
    `\r                            {{carriage return}} 
    `\s                            {{space}} 
    `\t                            {{tab}} 
    `\v                            {{vertical tab}} 

$ Date and Time
    `{Date={Y, M, D}, _} = erlang:localtime().
>                                  {{gets the date, including year, month, day}} 
    `{_, Time={H, M, S}} = erlang:localtime().
>                                  {{gets the time including hour, minute, second}} 

$ File Types
    `.erl                          {{module}} 
    `.hrl                          {{include file}} 
    `.rel                          {{release resource file}} 
    `.app                          {{application resource file}} 
    `.script                       {{boot script}} 
    `.boot                         {{binary boot script}} 
    `.config                       {{configuration file}} 
    `.appup                        {{application upgrade file}} 
    `.relup                        {{release upgrade file}} 

