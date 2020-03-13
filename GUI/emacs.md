# Emacs

> Source: http://www.rgrjr.com/emacs/emacs_cheat.html

$ Lingo
    `C                             {{control key (CTRL)}} 
    `M                             {{meta key (ALT or ESC)}} 

$ Quick Answers
    `C-x, C-f                      {{find file}} 
    `C-x, C-s                      {{save file}} 
    `C-x, C-c                      {{exit Emacs}} 

$ Cursor Motion
    `C-f                           {{Move forward by a character}} 
    `C-b                           {{Move backward by a character}} 
    `M-f                           {{Move forward by a word}} 
    `M-b                           {{Move backward by a word}} 
    `C-n                           {{Move forward by a line}} 
    `C-p                           {{Move backward by a line}} 
    `M-e                           {{Move forward by a sentence}} 
    `M-a                           {{Move backward by a sentence}} 
    `M-                            {{Move forward by a paragraph}} 
    `M-                            {{Move backward by a paragraph}} 
    `C-M-f                         {{Move forward by an expression}} 
    `C-M-b                         {{Move backward by an expression}} 
    `C-a                           {{Move to the start of a line}} 
    `C-e                           {{Move to the end of a line}} 
    `M-<                           {{Move to the start of a buffer}} 
    `M->                           {{Move to the end of a buffer}} 
    `M-g, g, #                     {{Go to line number #}} 

$ Editing
    `C-d                           {{Delete a character (forward)}} 
    `DEL                           {{Delete a character (backward)}} 
    `M-d                           {{Delete a word (forward)}} 
    `M-DEL                         {{Delete a word (backward)}} 
    `C-k                           {{Delete a line (forward)}} 
    `C-SPC, C-a, C-w               {{Delete a line (backward)}} 
    `M-k                           {{Delete a sentence (forward)}} 
    `C-x, DEL                      {{Delete a sentence (backward)}} 
    `C-M-k                         {{Delete an expression (forward)}} 
    `C-M-DEL                       {{Delete an expression (backward)}} 

$ Scrolling and Windows
    `C-v                           {{Page Down}} 
    `M-v                           {{Page Up}} 
    `C-M-v                         {{Page Down other window}} 
    `C-x, 1                        {{Make current window only window}} 
    `C-x, 2                        {{Split window vertically}} 
    `C-x, 3                        {{Split window horizontally}} 
    `C-x, ^                        {{Grow window vertically}} 
    `C-x, o                        {{Switch to next window}} 
    `C-x, 0                        {{Close current window}} 

$ Cutting and Pasting
    `C-SPC                         {{Set mark}} 
    `C-w                           {{Cut (after setting mark and moving to end point)}} 
    `M-w                           {{Copy (after setting mark and moving to end point)}} 
    `C-y                           {{Yank (paste) most recently killed (cut or copied)}} 
    `M-y                           {{Yank next most recently killed}} 

$ Files and Buffers
    `C-x, C-f                      {{Find file (or create if not existing)}} 
    `C-x, C-s                      {{Save file}} 
    `C-x, C-w                      {{Write file}} 
    `C-x, s                        {{Save modified buffers}} 
    `C-x, b                        {{Select buffer}} 
    `C-x, C-b                      {{List buffers}} 
    `C-x, k                        {{Kill buffer}} 

$ Command-Related Stuff
    `ESC, ESC, ESC                 {{Leave current location}} 
    `C-u, #                        {{Prefix numeric argument # to next command}} 
    `C-g                           {{Stop running command, or cancel partially entered command}} 

$ Searching and Replacing
    `C-s                           {{Incremental search forward}} 
    `C-r                           {{Incremental search backward}} 
    `C-M-s                         {{Regexp search forward}} 
    `C-M-r                         {{Regexp search backward}} 
    `M-x, <replace-string>, RET    {{String replace from here to end of buffer}} 
    `M-x, <query-replace>, RET     {{String replace from here to end of buffer, querying for each occurrence}} 
    `M-x, <grep>, RET              {{Prompts for a grep command, shows hits in a buffer}} 
    `C-x, `                        {{Visit next grep hit}} 

$ Help
    `C-h, k                        {{Show command documentation}} 
    `C-h, a                        {{"Command apropos"}} 
    `C-h, c                        {{Show command name on message line}} 
    `C-h, f                        {{Describe function}} 
    `C-h, i                        {{Info browser}} 

$ Misc
    `C-_                           {{Undo/redo}} 
    `C-x, u                        {{Undo/redo (alternative)}} 
    `C-q                           {{Quoted insert}} 
    `C-z                           {{Suspend/iconify emacs (type "%emacs" to return}} 
    `C-x, C-c                      {{Exit emacs}} 
    `M-x, <shell-strip-ctrl-m>, RET
>                                  {{Flush ^M at end of line}} 

