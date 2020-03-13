# ed

> Source: https://www.freebsd.org/cgi/man.cgi?ed%281%29

$ Invocation
    `ed [parameters] [filename]    {{Invoke ed(1) with optional parameters and/or filename}} 
    `-p [string]                   {{Use [string] as a prompt}} 
    `-s                            {{Suppress diagnostics (should be used if ed(1) is run from a script)}} 
    `-x                            {{Prompt for a DES encryption key (BSD only)}} 
    `-r                            {{Use "restricted" mode (GNU only)}} 
    `-v                            {{Use "verbose" mode (GNU only)}} 

$ Addressing
    `.                             {{The current line}} 
    `$                             {{The last line}} 
    `number                        {{The specified line number}} 
    `/pattern/                     {{The next line containing [pattern]}} 
    `?pattern?                     {{The previous line containing [pattern]}} 
    `+number                       {{[number] lines after the current line}} 
    `-number                       {{[number] lines before the current line}} 
    `'letter                       {{A line marked with {letter} (see the [k] command below)}} 

$ Editing Commands
    `.a                            {{Insert below the current line, end with a single period}} 
    `.,.c                          {{Change the specified range, end with a single period}} 
    `.,.d                          {{Delete the specified range}} 
    `.i                            {{Insert above the current line, end with a single period}} 
    `.,+j                          {{Join the specified range}} 
    `.,.m.                         {{Move the specified range}} 
    `.,.s/regexp/replacement/flags {{Perform a substitution on the specified range}} 
    `.,.t.                         {{Copy the specified range}} 
    `.x                            {{Paste the cut buffer (GNU extension)}} 
    `.,.y                          {{Copy (yank) the specified range (GNU extension)}} 
    `.klc                          {{Mark a line with a  lower case letter lc}} 

$ File Manipulation Commands
    `e [filename]                  {{Edit the file [filename]}} 
    `e !{command}                  {{Edit the output of {command}}} 
    `E [filename]                  {{Edit the file [filename] unconditionally}} 
    `f [filename]                  {{Set the default filename}} 
    `[$]r [filename]               {{Read data from [filename] after the specified line}} 
    `[$]r !{command}               {{Read output from {command} after the specified line}} 
    `[1,$]w [filename]             {{Write the specified range to [filename] unconditionally}} 
    `[1,$]wq [filename]            {{Write the specified range to [filename] unconditionally and quit}} 
    `[1,$]W [filename]             {{Append the specified range to [filename] unconditionally}} 
    `!command                      {{Execute {command} via [sh(1)]}} 
    `q                             {{Quit}} 
    `Q                             {{Quit unconditionally}} 
    `x                             {{Prompt for the DES encryption key (BSD extension)}} 

$ Display Commands
    `h                             {{Print help on the last error}} 
    `H                             {{Toggle printing of errors}} 
    `.l                            {{Display the specified range unambiguously}} 
    `.n                            {{Number and print the specified range}} 
    `.p                            {{Print the specified range}} 
    `P                             {{Toggle command-prompt printing}} 
    `.+1zN                         {{Display N lines of text}} 
    `.,.p                          {{Print the addressed lines}} 
    `.,.n                          {{Print the addressed lines along with their line numbers}} 

$ Other Commands
    `1,$g/{re}/{command-list}      {{Execute {command-list} on all lines matching {re}}} 
    `1,$G/re/                      {{Interactively edit all lines matching {re}}} 
    `.k{letter}                    {{Mark the line with the specified lower-case letter}} 
    `u                             {{Undo}} 
    `1,$v/re/{command-list}        {{Execute {command-list} on all lines that do not match {re}}} 
    `1,$V/re/                      {{Interactively edit all lines that do not match {re}}} 
    `$=                            {{Print the line number of the addressed line}} 
    `.+1newline                    {{Print and select the addressed line}} 
    `.,.#                          {{Comment the remainder of the line (GNU extension)}} 

