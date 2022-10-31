# VimL

> Source: http://vimdoc.sourceforge.net/htmldoc/usr_41.html

> Aliases: vim-language, vim-scripting, vim-script

$ Variable Scope
    `b:var                         {{Variable local to buffer}} 
    `w:var                         {{Variable local to window}} 
    `t:var                         {{Variable local to tab}} 
    `g:var                         {{Global variable}} 
    `l:var                         {{Variable local to function}} 
    `s:var                         {{Variable local to script}} 
    `a:var                         {{Variable for function argument}} 

$ Data Types
    `'String'                      {{String with no keycode expansion}} 
    `"\<Tab>String"                {{String with keycode expansion}} 
    `{'one': 'een', 'two': 'twee', 'three': 'drie'}
>                                  {{Dictionary}} 
    `['one', 'two', 'three']       {{List}} 

$ Buffer Interaction
    `getbufline(1, 1)              {{Get the line 1 of the first buffer}} 
    `getline(1)                    {{Get the line 1 of the current buffer}} 
    `setline(1, 'DuckDuckGo')      {{Set the line 1 of the current buffer}} 
    `append(1, ['DuckDuckGo', 'https://duckduckgo.com'])
>                                  {{Append two lines after line 1}} 
    `search('DuckDuckGo', 'W')     {{Search the current buffer for DuckDuckGo, no wrap around}} 

$ String Manipulation
    `printf('%03g', 17)            {{Create a formatted string '017'}} 
    `expand('%:p')                 {{Get the absolute filename of the current buffer}} 
    `fnameescape('/tmp/name|unsafe.txt')
>                                  {{Escape special characters in a filename to use in a vim command}} 
    `shellescape('string|unsafe')  {{Escape special characters in a string to use in a shell command}} 
    `substitute('999 abc', '\d\+', '\=submatch(0) + 1', '')
>                                  {{Find the first number in a string increment it by one}} 
    `substitute('999 abc', '\d\+', '\=submatch(0) + 1', '')
>                                  {{Find the first number in a string increment it by one}} 
    `str2nr("10", 10)              {{Converts string into corresponding decimal value}} 
    `str2nr("020", 8)              {{Converts string into corresponding octal value}} 
    `str2nr("0x10", 8)             {{Converts string into corresponding hexadecimal value}} 

$ I/O
    `system('echo DuckDuckGo')     {{Get the output of the command echo}} 
    `systemlist('echo DuckDuckGo') {{Get the output of the command echo as a list of lines}} 
    `readfile('/tmp/file.txt')     {{Read in a file as a list of lines}} 
    `writefile(['DuckDuckGo', 'https://duckduckgo.com'], '/tmp/file.txt')
>                                  {{Write two lines to a file}} 

$ List Manipulation
    `add(varlist, 3)               {{Add an item to varlist}} 
    `extend(targetlist, sourcelist)
>                                  {{Add items from sourcelist to targetlist}} 
    `remove([1, 2, 3], 1)          {{Remove the second item in the list}} 
    `join(['one', 'two', 'three']) {{Generate a string joining each list item with a space}} 
    `split('one two three')        {{Split a string at a list, with space as the delimiter}} 

$ Cursor Manipulation
    `getpos('.')                   {{Get the position of mark . (the cursor)}} 
    `setpos('.', [0, 1, 1, 0])     {{Set the position of mark . (the cursor) to line 1, column 1 in the current buffer}} 

