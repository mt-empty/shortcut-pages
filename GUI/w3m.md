# w3m

> Source: http://w3m.sourceforge.net/MANUAL#Key:orig

$ Page/Cursor motion
    `SPC, C-v                      {{Forward page}} 
    `b, ESC v                      {{Backward page}} 
    `l, C-f                        {{Cursor right}} 
    `h, C-b                        {{Cursor left}} 
    `j, C-n                        {{Cursor down}} 
    `k, C-p                        {{Cursor up}} 
    `J                             {{Roll up one line}} 
    `K                             {{Roll down one line}} 
    `^, C-a                        {{Go to the beginning of line}} 
    `$, C-e                        {{Go to the end of line}} 
    `w                             {{Go to next word}} 
    `W                             {{Go to previous word}} 
    `>                             {{Shift screen right}} 
    `<                             {{Shift screen left}} 
    `.                             {{Shift screen one column right}} 
    `,                             {{Shift screen one column left}} 
    `g, M-<                        {{Go to the first line}} 
    `G, M->                        {{Go to the last line}} 
    `ESC g                         {{Go to specified line}} 
    `Z                             {{Move to the center line}} 
    `z                             {{Move to the center column}} 
    `TAB                           {{Move to next hyperlink}} 
    `C-u, ESC TAB                  {{Move to previous hyperlink}} 
    `[                             {{Move to the first hyperlink}} 
    `]                             {{Move to the last hyperlink}} 

$ Hyperlink operation
    `RET                           {{Follow hyperlink}} 
    `a, ESC RET                    {{Save link to file}} 
    `u                             {{Peek link URL}} 
    `i                             {{Peek image URL}} 
    `l                             {{View inline image}} 
    `ESC l                         {{Save inline image to file}} 
    `:                             {{Mark URL-like strings as anchors}} 
    `ESC :                         {{Mark Message-ID-like strings as news anchors}} 
    `c                             {{Peek current URL}} 
    `=                             {{Display information about current document}} 
    `C-g                           {{Show current line number}} 
    `C-h                           {{View history of URL}} 
    `F                             {{Render frame}} 
    `M                             {{Browse current document using external browser (use 2M and 3M to invoke second and third browser)}} 
    `ESC M                         {{Browse link using external browser (use 2ESC M and 3ESC M to invoke second and third browser)}} 

$ File/Stream operation
    `U                             {{Open URL}} 
    `V                             {{View new file}} 
    `@                             {{Execute shell command and load}} 
    `#                             {{Execute shell command and browse}} 

$ Buffer operation
    `B                             {{Back to the previous buffer}} 
    `v                             {{View HTML source}} 
    `s                             {{Select buffer}} 
    `E                             {{Edit buffer source}} 
    `C-l                           {{Redraw screen}} 
    `R                             {{Reload buffer}} 
    `S                             {{Save buffer}} 
    `ESC s                         {{Save source}} 
    `ESC e                         {{Edit buffer image}} 

$ Buffer selection mode
    `k, C-p                        {{Select previous buffer}} 
    `j, C-n                        {{Select next buffer}} 
    `D                             {{Delect current buffer}} 
    `RET                           {{Go to the selected buffer}} 

$ Bookmark operation
    `ESC b                         {{Load bookmark}} 
    `ESC a                         {{Add current to bookmark}} 

$ Search
    `\], C-s                       {{Search forward}} 
    `?, C-r                        {{Search backward}} 
    `n                             {{Search next}} 
    `N                             {{Search previous}} 
    `C-w                           {{Toggle wrap search mode}} 

$ Mark operation
    `C-SPC                         {{Set/unset mark}} 
    `ESC p                         {{Go to previous mark}} 
    `ESC n                         {{Go to next mark}} 
    `"                             {{Mark by regular expression}} 

$ Miscellany
    `!                             {{Execute shell command}} 
    `H                             {{Help (load this file)}} 
    `o                             {{Set option}} 
    `C-k                           {{Show cookie jar}} 
    `C-c                           {{Stop}} 
    `C-z                           {{Suspend}} 
    `q                             {{Quit (with confirmation, if you like)}} 
    `Q                             {{Quit without confirmation}} 

$ Line-edit mode
    `C-f                           {{Move cursor forward}} 
    `C-b                           {{Move cursor backward}} 
    `C-h                           {{Delete previous character}} 
    `C-d                           {{Delete current character}} 
    `C-k                           {{Kill everything after cursor}} 
    `C-u                           {{Kill everything before cursor}} 
    `C-a                           {{Move to the top of line}} 
    `C-e                           {{Move to the bottom of line}} 
    `C-p                           {{Fetch the previous string from the history list}} 
    `C-n                           {{Fetch the next string from the history list}} 
    `TAB, SPC                      {{Complete filename}} 
    `RET                           {{Accept}} 

