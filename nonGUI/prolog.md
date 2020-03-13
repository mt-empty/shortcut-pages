# Prolog

> Source: http://cliplab.org/~vocal/public_info/seminar_notes/node42.html

> Aliases: prolog-predicate, prolog-predicates

$ Arithmetic Terms
    `+/2                           {{Addition: 3 + 5.}} 
    `+/1                           {{Positive prefix (usually unneeded): +3}} 
    `-/2                           {{Subtraction: 5 - 3}} 
    `-/1                           {{Negative prefix: -1}} 
    `/ /2                          {{Division: 3/5 = 0.6}} 
    `// /2                         {{Integer Division: 3//5 = 0}} 
    `mod/2                         {{Module: 5 mod 3 = 2}} 
    `log/1                         {{Logarithm: log(1) = 0.0}} 

$ Arithmetic Builtins
    `is/2                          {{Evaluation: Z is T evaluates the arithmetical term T and the result is unified with the variable Z. X is 3 + 5. X = 8}} 
    `=:=                           {{Arithmetic equality}} 
    `=\=                           {{Arithmetic inequality}} 
    `<
>
=<
>=                     {{Order relationship}} 

$ Type Predicates
    `integer(X)                    {{Check whether X is an integer}} 
    `float(X)                      {{Check whether X is a floating point number}} 
    `number(X)                     {{Check whether X is a number }} 
    `atom(X)                       {{Check whether X is a constant other than number}} 
    `atomic(X)                     {{Check whether X is a constant}} 

$ Structure Inspection
    `functor(F, N, A)              {{Succeeds when F is a complex structure whose arity is N and whose arity is A. It can be used to build new functors with fresh variables, or to obtain the name and arity of already built functors}} 
    `arg(F, N, Arg)                {{Succeeds when Arg is the N-th argument of functor F. Arguments start numbering at 1}} 

$ Input/Output
    `write(X)                      {{Write the term X on the current output stream}} 
    `nl                            {{Start a new line on the current output stream}} 
    `read(X)                       {{Read a term (finished by a full stop) from the current input stream and unify it with X}} 
    `put(N)                        {{Write the ASCII character code N. N can be a string of length one}} 
    `get(X)                        {{Read the next character code and unify its ASCII code with N}} 
    `see(File)                     {{File becomes the current input stream}} 
    `seeing(File)                  {{The current input stream is File}} 
    `seen                          {{Close the current input stream}} 
    `tell(File)                    {{File becomes the current output stream}} 
    `telling(File)                 {{The current output stream is File}} 
    `told                          {{Close the current output stream}} 

$ Pruning Operators
    `!/0                           {{The "cut" operator}} 

$ Meta-Logical Predicates
    `var(X)                        {{X is currently a free variable}} 
    `nonvar(X)                     {{X is not a free variable}} 
    `ground(X)                     {{X is a term not containing variables}} 

$ Meta-Calls (Higher Order)
    `call(X)                       {{Accepts a term and calls it as if it appeared in the program text. Thus, call(p(X)) is equivalent to the appearance of p(X) in the program text. The argument X of call(X) (and this is really where the power of meta-calls is) does not need to be explicitly present in the source code, but only correctly instantiated at run-time}} 
    `findall(Term, Goal, List)     {{Leaves in List an instance of Term for each success of Goal}} 
    `bagof(Term, Goal, List)       {{Allows (selective) backtracking on the free variables of the goal}} 
    `setof(Term, Goal, List)       {{Behaves as bagof/3, but in addition the returned list is sorted and has no repetitions}} 

$ Dynamic Program Modification
    `assert(X)
assertz(X)          {{Adds a new fact or clause to the database. Term is asserted as the last fact or clause with the same key predicate}} 
    `asserta(X)                    {{Same as assert(X) but adds clause at the beginning of database}} 
    `retract(X)                    {{Removes fact or clause X from the database}} 
    `retractall(X)                 {{Removes all facts or clauses from the database for which the head unifies with X.}} 

