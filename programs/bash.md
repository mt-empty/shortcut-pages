# Bash

> Source: https://www.gnu.org/software/bash/

> Aliases: shell-language, sh, posix-shell, shell

$ Lingo
    `C                             {{Ctrl}} 
    `M                             {{Meta Key (Alt or ESC)}} 

$ Shortcuts
    `C-c                           {{Interrupt running process}} 
    `C-z                           {{Suspend running process}} 
    `C-d                           {{Exit from current shell}} 
    `C-l                           {{Clear Screen}} 
    `C-a                           {{Move at the start of the line}} 
    `C-e                           {{Move at the end of the line}} 
    `M-←                           {{Move backward by a word}} 
    `M-b                           {{Move backward by a word (alternative)}} 
    `M-→                           {{Move forward by a word}} 
    `M-f                           {{Move forward by a word (alternative)}} 
    `C-x, C-x                      {{Move cursor between start of line and current position}} 
    `M-t                           {{Swap the last two words before the cursor}} 
    `C-t                           {{Swap the last two characters before the cursor}} 
    `M-Backspace                   {{Delete a word (backward)}} 
    `C-w                           {{Delete a word (backward) (alternative)}} 
    `M-d                           {{Delete a word (forward)}} 
    `C-h                           {{Delete one character backward (same as Backspace)}} 
    `C-k                           {{Kill from cursor to the end of line}} 
    `C-u                           {{Kill from cursor to the beginning of line}} 
    `M-u                           {{Upper-case from cursor to the end of word}} 
    `M-l                           {{Lower-case from cursor to the end of word}} 
    `M-c                           {{Capitalize word (from cursor position)}} 
    `C-y                           {{Paste}} 
    `C-_                           {{Undo}} 
    `M-r                           {{Revert to original command (before editing it)}} 
    `C-p                           {{Get previous command}} 
    `C-n                           {{Get next command}} 
    `C-r, <pattern>                {{Search previous command containing <pattern>}} 
    `M-.                           {{Insert last argument of last command}} 
    `M-<N>, C-M-y                  {{Get Nth argument of previous command (N=0 gives the command)}} 
    `M-<                           {{Insert oldest command from history}} 
    `C-x, C-v                      {{Show bash version}} 
    `C-x, C-e                      {{Edit current line with ${EDITOR}}} 

$ Special Variables
    `!$                            {{Last argument of last command}} 
    `$<N>                          {{Nth argument of current process (positional parameter)}} 
    `$#                            {{Number of arguments given to current process}} 
    `$@                            {{Command line arguments for current process}} 
    `$*                            {{Without quotes, same as '$@'}} 
    `"$*"                          {{Command line arguments for current process, expanded to a single argument}} 
    `$0                            {{The name of the shell program}} 
    `$?                            {{Exit code of previous command}} 
    `$$                            {{PID of current shell or script}} 
    `:                             {{Dummy placeholder (produces no output)}} 
    `!-<N>                         {{Execute Nth command from history}} 
    `!!                            {{Execute last command}} 
    `!<string>                     {{Execute last command starting with <string>}} 

$ Standard File Descriptors
    `0                             {{stdin}} 
    `1                             {{stdout}} 
    `2                             {{stderr}} 

$ TCP/UDP Sockets
    `cat < /dev/tcp/<hostname>/<port>
>                                  {{Open a TCP socket to <hostname> at <port> and write the contents of stdin}} 
    `cat < /dev/udp/<hostname>/<port>
>                                  {{Open a UDP socket to <hostname> at <port> and write the contents of stdin}} 

$ Arithmetic Operators
    `+                             {{Addition}} 
    `-                             {{Subtraction}} 
    `++                            {{Increment}} 
    `--                            {{Decrement}} 
    `*                             {{Multiplication}} 
    `/                             {{Division}} 
    `%                             {{Modulo}} 
    `**                            {{Exponentiation}} 
    `<<                            {{Bit-shift left}} 
    `>>                            {{Bit-shift right}} 
    `<                             {{Comparison (less than)}} 
    `-lt                           {{Comparison (less than) (alternative)}} 
    `<=                            {{Comparison (less than or equal)}} 
    `-le                           {{Comparison (less than or equal) (alternative)}} 
    `>                             {{Comparison (greater than)}} 
    `-gt                           {{Comparison (greater than) (alternative)}} 
    `>=                            {{Comparison (greater than or equal)}} 
    `-ge                           {{Comparison (greater than or equal) (alternative)}} 
    `==                            {{Comparison (equal)}} 
    `!=                            {{Comparison (not equal)}} 
    `&                             {{Bitwise AND}} 
    `^                             {{Bitwise exclusive OR}} 
    `|                             {{Bitwise OR}} 
    `&&                            {{Logical AND}} 
    `||                            {{Logical OR}} 

$ IO Redirection
    `cmd > file                    {{Send cmd output to file (overwrite)}} 
    `cmd >> file                   {{Send cmd output to file (append)}} 
    `cmd < file                    {{Contents of file are passed to cmd's stdin}} 
    `cmd1 | cmd2                   {{Output of cmd1 is passed to cmd2's stdin}} 
    `cmd &> file                   {{Redirect both stdout and stderr to file (overwrite)}} 
    `cmd &>> file                  {{Redirect both stdout and stderr to file (append)}} 
    `cmd >&n                       {{Send cmd's stdout to file descriptor n}} 
    `cmd m>&n                      {{Same as above except that output that would normally go to file descriptor m, will also go to n}} 
    `cmd <&n                       {{File descriptor n becomes stdin for cmd}} 
    `cmd m<&n                      {{Same as above except that stdin that would normally come from file descriptor m, will now come from n}} 
    `cmd >&-                       {{Close stdout}} 
    `cmd <&-                       {{Close stdin}} 

$ Expansion And Other Operators
    `$var:pos                      {{Extracts substring from var at pos}} 
    `$var:pos:len                  {{Extracts len characters of substring from var at pos}} 
    `$var:-val                     {{If $var exists and isn't NULL, return its value; otherwise return val}} 
    `$var:=val                     {{If $var exists and isn't NULL, return its value; otherwise set it to val and then return its value}} 
    `$var:?val                     {{If $var exists and isn't NULL, return its value; otherwise return 'var: val' and abort}} 
    `$var:?                        {{If $var exists and isn't NULL, return its value; otherwise return 'var: parameter null or not set' and abort}} 
    `$var:+val                     {{If $var exists and isn't NULL, return val; otherwise return NULL}} 
    `$((...))                      {{Arithmetic Expansion}} 
    `$#var                         {{String length operator}} 
    `$str#substr                   {{Deletes shortest match of substr from front of str}} 
    `$str##substr                  {{Deletes longest match of substr from front of str}} 
    `$str%substr                   {{Deletes shortest match of substr from back of str}} 
    `$str%%substr                  {{Deletes longest match of substr from back of str}} 
    `$str/substr/val               {{Replace first match of substr with val}} 
    `$str//substr/val              {{Replace all matches of substr with val}} 
    `$str/#substr/val              {{If $substr matches front end of str, substitute val for substr}} 
    `$str/%substr/val              {{If $substr matches back end of str, substitute val for substr}} 
    `$str^substr                   {{Upper-case of first match of substr. An empty pattern selects first char.}} 
    `$str^^substr                  {{Upper-case of all matches of substr. An empty pattern selects the whole string.}} 
    `$str,substr                   {{Lower-case first match of substr. An empty pattern selects first char.}} 
    `$str,,substr                  {{Lower-case all matches of substr. An empty pattern selects the whole string.}} 

$ Conditionals
    `if [$hello == "world"] ; then ...; fi
>                                  {{If statement}} 
    `elif [$hello == "world"] ; then
>                                  {{Else if statement}} 
    `else                          {{Else statement}} 
    `fi                            {{End if statement}} 
    `case "$hello" in              {{Case statement}} 
    `a) echo world ;;              {{Case entry "a"}} 
    `*) echo default ;;            {{Default case entry (matches everything)}} 
    `esac                          {{End case statement}} 

$ Loops
    `for ((i = 1; i <= 10; i++)) ; do [expressions] done
>                                  {{For loop running 10 times}} 
    `for i in $list ; do [expressions] done
>                                  {{For loop being executed for every item in $list}} 
    `while (i <= 10) ; do [expressions] done
>                                  {{While loop}} 
    `done                          {{End loop}} 

$ Exit Statuses
    `0                             {{Success}} 
    `!=0                           {{Failure}} 

$ Auto-Completion
    `TAB                           {{Auto-complete (hit twice when ambiguous)}} 
    `~, TAB TAB                    {{Display all users from /etc/passwd}} 
    `$, TAB TAB                    {{Display all system variables}} 
    `<string>, M-/                 {{Auto-complete/display files and directories starting with <string>}} 
    `<string>, M-?                 {{Display commands starting with <string>}} 
    `M-*                           {{Insert all possible completions}} 

$ Misc
    `a=$(cmd)                      {{$a now holds cmd's output}} 
    `a=`cmd`                       {{$a now holds cmd's output (alternative)}} 
    `cmd &                         {{Execute cmd in the background (fork)}} 

