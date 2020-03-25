# Evil-Mode for Emacs

> Source: https://github.com/amirrajan/devbox/wiki/EMACS-Evil-Cheat-Sheet

> Aliases: evil-emacs, evil-mode-emacs, evil-mode-for-emacs, evil-emacs-mode

$ Editing Text
    `ESC                           {{Command Mode}} 
    `:w                            {{save}} 
    `:q                            {{quit}} 
    `:wq                           {{save and quit}} 
    `:wqa                          {{save quit all}} 
    `hjkl                          {{to navigate}} 
    `w                             {{to move forward by one word}} 
    `b                             {{to move back by one word}} 
    `shift+                        {{move up by new lines}} 
    `shift+                        {{to move down by new lines}} 
    `yy                            {{copy line}} 
    `dd                            {{delete line}} 
    `cc                            {{change line}} 
    `Y                             {{copy till the end of line}} 
    `D                             {{delete till the end of line}} 
    `C                             {{change till the end of line}} 
    `yw                            {{yank word}} 
    `dw                            {{delete word}} 
    `cw                            {{change word}} 
    `gg                            {{go to top of file}} 
    `G                             {{goto bottom of file}} 

$ Window Navigation
    `,g                            {{go to file}} 
    `,b                            {{view recently visited files}} 
    `,m                            {{new vertical split}} 
    `:split                        {{new horizontal split}} 
    `,.                            {{open current directory}} 
    `C-h , C-j ,C-k ,C-l           {{navigate between windows}} 
    `,)                            {{previous buffer}} 
    `,(                            {{next buffer}} 
    `:ack ENT                      {{search across files}} 
    `,f                            {{next search result}} 
    `,d                            {{previous search result}} 
    `CTRL+v                        {{visula block mode}} 
    `While in visual Block Mode shift + i
>                                  {{Insert Mode to append text to selection from Visual Block Mode}} 

$ Discovery
    `:describe-char                {{describes the char underneath the cursor, allows you to change color theme from there}} 
    `:customize-face               {{editor for changing all color themes use tab and shift+tab to navigate}} 
    `F1 k KEYSTROKE                {{press F1 followed by k, then enter a key stroke to find information about what editor method was invoked}} 
    `F1 f METHODNAME               {{gives information about an editor method}} 
    `F1 a SEARCH                   {{search for an editor method containing the search term}} 
    `:METHODNAME                   {{invoke editor method}} 

