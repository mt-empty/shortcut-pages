# Shell Variables

> Source: http://bash.cyberciti.biz/guide/Variables

> Aliases: basic-shell-variables, shellvar, shell-var, shell-vars

$ System Variables
    `BASH_VERSION                  {{Version information for this Bash}} 
    `HOSTNAME                      {{The name of the current host}} 
    `CDPATH                        {{A colon-separated list of directories to search for directories given as arguments to "cd"}} 
    `HISTFILE                      {{The name of the file where your command history is stored}} 
    `HISTFILESIZE                  {{The maximum number of lines this file can contain}} 
    `HISTSIZE                      {{The maximum number of history lines that a running shell can access}} 
    `HOME                          {{The complete pathname to your login directory}} 
    `IFS                           {{The Internal Field Separator that is used for word splitting after expansion and to split lines into words with the read builtin command. The default value is <space><tab><newline>}} 
    `LANG                          {{Used to determine the locale category for any category not specifically selected with a variable starting with LC}} 
    `PATH                          {{A colon-separated list of directories to search when looking for commands}} 
    `PS1                           {{The primary prompt string}} 
    `TMOUT                         {{The default timeout for the read builtin command. Also in an interactive shell, the value is interpreted as the number of seconds to wait for input after issuing the command. If no input is provided it will logout user}} 
    `TERM                          {{Your login terminal type}} 
    `SHELL                         {{Set path to login shell}} 
    `DISPLAY                       {{Set X display name}} 
    `EDITOR                        {{Set the name of the default text editor}} 

$ User Defined Variables
    `EXAMPLE="My Example"          {{The value "My Example" is now set to the variable "EXAMPLE"}} 

$ Display Value
    `echo "Hello World"            {{Displays Hello World}} 
    `echo "$EXAMPLE"               {{Displays the content of the variable "EXAMPLE"}} 
    `echo "${EXAMPLE}"             {{Displays the content of the variable "EXAMPLE"}} 
    `echo "${EXAMPLE}SOMETEXT"     {{Displays the content of the variable "EXAMPLE" with SOMETEXT appended to it}} 

