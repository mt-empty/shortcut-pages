# GNU Octave

> Source: http://folk.ntnu.no/joern/itgk/refcard-a4.pdf

> Aliases: gnu-octave-programming, octave-language, octave-programming, gnu-octave

$ Starting Octave
    `octave                        {{Start interactive Octave session}} 
    `octave file                   {{Run Octave on commands in file}} 
    `octave --help                 {{Describe command line options}} 

$ Stopping Octave
    `quit or exit                  {{Exit Octave}} 
    `INTERRUPT                     {{Terminate current command and return to top-level prompt}} 

$ Getting Help
    `help                          {{List all commands and built-in variables}} 
    `help command                  {{Briefly describe command}} 
    `help -i                       {{Use Info to browse Octave manual}} 
    `help -i command               {{Search for command in Octave manual}} 

$ Motion in Info
    `SPC or C-v                    {{Scroll forward one screenful}} 
    `DEL or M-v                    {{Scroll backward one screenful}} 
    `C-l                           {{Redraw the display}} 

$ Node Selection in Info
    `n                             {{Select the next node}} 
    `p                             {{Select the previous node}} 
    `u                             {{Select the ‘up’ node}} 
    `t                             {{Select the ‘top’ node}} 
    `d                             {{Select the directory node}} 
    `<                             {{Select the first node in the current file}} 
    `>                             {{Select the last node in the current file}} 
    `g                             {{Reads the name of a node and selects it}} 
    `C-x k                         {{Kills the current node}} 

$ Searching in Info
    `s                             {{Search for a string}} 
    `C-s                           {{Search forward incrementally}} 
    `C-r                           {{Search backward incrementally}} 
    `i                             {{Search index & go to corresponding node}} 
    `,                             {{Go to next match from last ‘i’ command}} 

$ Command-Line Cursor Motion
    `C-b                           {{Move back one character}} 
    `C-f                           {{Move forward one character}} 
    `C-a                           {{Move the start of the line}} 
    `C-e                           {{Move to the end of the line}} 
    `M-f                           {{Move forward a word}} 
    `M-b                           {{Move backward a word}} 
    `C-l                           {{Clear screen, reprinting current line at top}} 

$ Inserting or Changing Text
    `M-TAB                         {{Insert a tab character}} 
    `DEL                           {{Delete character to the left of the cursor}} 
    `C-d                           {{Delete character under the cursor}} 
    `C-v                           {{Add the next character verbatim}} 
    `C-t                           {{Transpose characters at the point}} 
    `M-t                           {{Transpose words at the point}} 

$ Killing and Yanking
    `C-k                           {{Kill to the end of the line}} 
    `C-y                           {{Yank the most recently killed text}} 
    `M-d                           {{Kill to the end of the current word}} 
    `M-DEL                         {{Kill the word behind the cursor}} 
    `M-y                           {{Rotate the kill ring and yank the newtop}} 

$ Shell Commands
    `cd dir                        {{Change working directory to dir}} 
    `pwd                           {{Print working directory}} 
    `ls options                    {{Print directory listing}} 
    `getenv (string)               {{Return value of named environment variable}} 
    `system (cmd)                  {{Execute arbitrary shell command string}} 

$ Command Completion and History
    `TAB                           {{Complete a command or variable name}} 
    `M-?                           {{List possible completions}} 
    `C-p                           {{Move ‘up’ through the history list}} 
    `C-n                           {{Move ‘down’ through the history list}} 
    `M-<                           {{Move to the first line in the history}} 
    `M->                           {{Move to the last line in the history}} 

