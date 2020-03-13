# gnu screen

> Source: https://www.gnu.org/software/screen/manual/screen.html

$ Terminal Commands
    `screen                        {{Start a new session}} 
    `screen -S <name>              {{Start a new named session}} 
    `screen -ls                    {{List sessions}} 
    `screen -r <name>              {{Re-attach session}} 

$ Copying and Scrolling
    `Ctrl-a [                      {{Copy mode}} 
    `Ctrl-a space                  {{Start copy}} 
    `Ctrl-a space                  {{End copy}} 
    `Ctrl-a ]                      {{Paste}} 
    `Ctrl-a u                      {{Scroll up}} 
    `Ctrl-a d                      {{Scroll down}} 
    `Ctrl-a escape                 {{End copy mode}} 

$ Main Commands
    `Ctrl-a ?                      {{Shortcuts menu}} 
    `Ctrl-a :                      {{Enter command mode}} 
    `Ctrl-a d                      {{Detach session}} 
    `Ctrl-a ]                      {{Kill session}} 

$ Window Commands
    `Ctrl-a c                      {{Create a new window}} 
    `Ctrl-a k                      {{Kill current window}} 
    `Ctrl-a n                      {{Next window}} 
    `Ctrl-a p                      {{Previous window}} 
    `Ctrl-a 0-9                    {{Jump to window #}} 
    `Ctrl-a Ctrl-a                 {{Jump to last-visited window}} 
    `Ctrl-a "                      {{List windows}} 
    `Ctrl-a |                      {{Split vertical}} 
    `Ctrl-a S                      {{Split horizontal}} 
    `Ctrl-a tab                    {{Focus next region}} 
    `Ctrl-a Q                      {{Quit split screen mode}} 

