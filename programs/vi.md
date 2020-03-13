# Vi

> Source: http://www.lagmonster.org/docs/vi.html

$ Quitting
    `:x                            {{Exit, saving changes}} 
    `:q                            {{Exit as long as there have been no changes}} 
    `ZZ                            {{Exit and save changes if any have been made}} 
    `:q!                           {{Exit and ignore any changes}} 

$ Inserting Text
    `i                             {{insert before cursor}} 
    `I                             {{Insert before line}} 
    `a                             {{Append after cursor}} 
    `A                             {{Append after line}} 
    `o                             {{Open a new line after current line}} 
    `O                             {{Open a new line before current line}} 
    `r                             {{Replace one character}} 
    `R                             {{Replace many characters}} 

$ Motion
    `h                             {{Move left}} 
    `j                             {{Move down}} 
    `k                             {{Move up}} 
    `l                             {{Move right}} 
    `w                             {{Move to next word}} 
    `W                             {{Move to next blank delimited word}} 
    `b                             {{Move to the beginning of the word}} 
    `B                             {{Move to the beginning of blank delimited word}} 
    `e                             {{Move to the end of the word}} 
    `E                             {{Move to the end of Blank delimited word}} 
    `(                             {{Move a sentence back}} 
    `)                             {{Move a sentence forward}} 
    `{                             {{Move a paragraph back}} 
    `}                             {{Move a paragraph forward}} 
    `0                             {{Move to the beginning of the line}} 
    `$                             {{Move to the end of the line}} 
    `1G                            {{Move to the first line of the file}} 
    `G                             {{Move to the last line of the file}} 
    `nG                            {{Move to nth line of the file}} 
    `:n                            {{Move to nth line of the file}} 
    `H                             {{Move to top of screen}} 
    `M                             {{Move to middle of screen}} 
    `L                             {{Move to bottom of screen}} 
    `%                             {{Move to associated ( ), { }, [ ]}} 
    `fc                            {{Move forward to the next occurrence of the letter c in the current line}} 
    `Fc                            {{Move backward to the next occurrence of the letter c in the current line}} 

$ Deleting Text
    `x                             {{Delete character to the right of cursor}} 
    `X                             {{Delete character to the left of cursor}} 
    `D                             {{Delete to the end of the line}} 
    `dd                            {{Delete current line}} 
    `:d                            {{Delete current line}} 

$ Yanking Text
    `yy                            {{Yank the current line}} 
    `:y                            {{Yank the current line}} 

$ Changing Text
    `C                             {{Change to the end of the line}} 
    `cc                            {{Change the whole line}} 

$ Putting Text
    `p                             {{Put after the position or after the line}} 
    `P                             {{Put before the position or before the line}} 

$ Search for strings
    `/string                       {{Search forward for string}} 
    `?string                       {{Search back for string}} 
    `n                             {{Search for next instance of string}} 
    `N                             {{Search for previous instance of string}} 

$ Replace
    `:s/pattern/string/flags       {{Replace pattern with string according to flags}} 
    `g                             {{Flag - Replace all occurrences of pattern}} 
    `c                             {{Flag - Confirm replaces}} 
    `&                             {{Repeat last :s command}} 

$ Other
    `~                             {{Toggle upper and lower case}} 
    `J                             {{Join lines}} 
    `.                             {{Repeat last text-changing command}} 
    `u                             {{Undo last change}} 
    `U                             {{Undo all changes to line}} 

