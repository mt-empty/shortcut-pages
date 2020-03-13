# Idris REPL

> Source: http://www.idris-lang.org

$ From the Prompt
    `<expr>                        {{Evaluate an expression.}} 
    `:t, :type                     {{Check the type of an expression.}} 
    `:q, :quit                     {{Exit the Idris system}} 
    `:w,  :warranty                {{Displays warranty information}} 
    `:?, :h, :help                 {{Display this help text}} 
    `:pp, :pprint <option> <number> <name>
>                                  {{Pretty prints an Idris function in either LaTeX or HTML and for a specified width.}} 
    `:r, :reload                   {{Reload current file}} 
    `:l, :load <filename>          {{Load a new file}} 
    `:cd <filename>                {{Change working directory}} 
    `:e, :edit                     {{Edit current file using $EDITOR or $VISUAL}} 
    `:module <module>              {{Import an extra module}} 
    `:m, :metavars                 {{Show remaining proof obligations (metavariables or holes)}} 
    `:x <expr>                     {{Execute IO actions resulting from an expression using the interpreter}} 
    `:c, :compile <filename>       {{Compile to an executable [codegen <filename>}} 
    `:exec,  :execute <expr>       {{Compile to an executable and run}} 
    `:let (<top-level declaration>)
>                                  {{Evaluate a declaration, such as a function definition, instance implementation, or fixity declaration}} 
    `:unlet, :undefine ([<name>])  {{Remove the listed repl definitions, or all repl definitions if no names given}} 

$ Documentation and Searching
    `:doc <name>                   {{Show internal documentation}} 
    `:mkdoc <namespace>            {{Generate IdrisDoc for namespace(s) and dependencies}} 
    `:apropos <package list> <name>
>                                  {{Search names, types, and documentation}} 
    `:s :search [<package list>] <expr>
>                                  {{Search for vals by type}} 
    `:browse <namespace>           {{List the contents of some namespace}} 

$ Displaying Information
    `:total <name>                 {{Check the totality of a name}} 
    `:miss, :missing <name>        {{Show missing clauses}} 
    `:wc, :whocalls <name>         {{List the callers of some name}} 
    `:cw, :callswho <name>         {{List the callees of some name}} 
    `:printdef <name>              {{Show the definition of a function}} 
    `:showproof <name>             {{Show proof}} 
    `:proofs                       {{Show available proofs}} 

$ Advanced Usage
    `:p, :prove <hole>             {{Prove a metavariable}} 
    `:elab <hole>                  {{Build a metavariable using the elaboration shell}} 
    `:a, :addproof <name>          {{Add proof to source file}} 
    `:rmproof <name>               {{Remove proof from proof stack}} 
    `:core <expr>                  {{View the core language representation of a term}} 
    `:dynamic <filename>           {{Dynamically load a C library (similar to %dynamic)}} 
    `:dynamic                      {{List dynamically loaded C libraries}} 

$ Changing Settings
    `:set <option>                 {{Set an option (errorcontext, showimplicits)}} 
    `:unset <option>               {{Unset an option}} 
    `:color, :colour <option>      {{Turn REPL colours on or off; set a specific colour}} 
    `:consolewidth (auto|infinite|number)
>                                  {{Set the width of the console}} 
    `:printerdepth [<number>]      {{Set the maximum pretty-printer depth (no arg for infinite)}} 

