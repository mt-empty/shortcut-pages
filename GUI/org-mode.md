# Org mode

> Source: http://orgmode.org/orgcard.pdf

> Aliases: orgmode

$ Timestamps
    `C-c .                         {{prompt for date and insert timestamp}} 
    `C-u C-c .                     {{like C-c . but insert date and time format}} 
    `C-c !                         {{like C-c . but make stamp inactive}} 
    `C-c C-d                       {{insert DEADLINE timestamp}} 
    `C-c C-s                       {{insert SCHEDULED timestamp}} 
    `C-c / d                       {{create sparse tree with all deadlines due}} 
    `C-c C-y                       {{the time between 2 dates in a time range}} 
    `S-RIGHT/LEFT                  {{change timestamp at cursor ±1 day}} 
    `S-UP/DOWN                     {{change year/month/day at cursor by ±1}} 
    `C-c >                         {{access the calendar for the current date}} 
    `C-c <                         {{insert timestamp matching date in calendar}} 
    `C-c C-o                       {{access agenda for current date}} 
    `mouse-1/RET                   {{select date while prompted}} 
    `C-c C-x C-t                   {{toggle custom format display for dates/times}} 

$ Clocking Time
    `C-c C-x C-i                   {{start clock on current item}} 
    `C-c C-x C-o/x                 {{stop/cancel clock on current item}} 
    `C-c C-x C-d                   {{display total subtree times}} 
    `C-c C-c                       {{remove displayed times}} 
    `C-c C-x C-r                   {{insert/update table with clock report}} 

$ TODO Items and Checkboxes
    `C-c C-t                       {{rotate the state of the current item}} 
    `S-LEFT/RIGHT                  {{select next/previous state}} 
    `C-S-LEFT/RIGHT                {{select next/previous set}} 
    `C-c C-x o                     {{toggle ORDERED property}} 
    `C-c C-v                       {{view TODO items in sparse tree}} 
    `C-3 C-c C-v                   {{view 3rd TODO keyword's sparse tree}} 
    `C-c , ABC                     {{set the priority of the current item}} 
    `C-c , SPC                     {{remove priority cookie from current item}} 
    `S-UP/DOWN                     {{raise/lower priority of current item}} 
    `M-S-RET                       {{insert new checkbox item in plain list}} 
    `C-c C-x C-b                   {{toggle checkbox(es) in region/entry/at point}} 
    `C-c C-c                       {{toggle checkbox at point}} 
    `C-c #                         {{update checkbox statistics (C-u: whole file)}} 

$ Tags
    `C-c C-q                       {{set tags for the current heading}} 
    `C-u C-c C-q                   {{realign tags in all headings}} 
    `C-c \                         {{create sparse tree with matching tags}} 
    `C-c C-o                       {{globally (agenda) match tags at cursor}} 

$ Agenda Views
    `C-c                           {{add/move current file to front agenda}} 
    `C-c                           {{remove current file from your agenda}} 
    `C-c '                         {{cycle through agenda file list}} 
    `C-c C-x </>                   {{set/remove restriction lock}} 
    `C-c a a                       {{compile agenda for the current week}} 
    `C-c a t                       {{compile global TODO list}} 
    `C-c a T                       {{compile TODO list for specific keyword}} 
    `C-c a m                       {{match tags, TODO keywords, properties}} 
    `C-c a M                       {{match only TODO entries}} 
    `C-c a #                       {{find stuck projects}} 
    `C-c a L                       {{show timeline of current org file}} 
    `C-c a C                       {{configure custom commands}} 
    `C-c C-o                       {{agenda for date at cursor}} 

$ Exporting and Publishing
    `C-c C-e                       {{export/publish dispatcher}} 
    `C-c C-e v                     {{export visible part only}} 
    `C-c C-e t                     {{insert template of export options}} 
    `C-c :                         {{toggle fixed width for entry of region}} 
    `C-c C-x \                     {{toggle pretty display of scripts, entities}} 
    `C-c ;                         {{toggle COMMENT keyword on entry}} 

$ Working with Code (Babel)
    `C-c C-c                       {{execute code block at point}} 
    `C-c C-o                       {{open results of code block at point}} 
    `C-c C-v c                     {{check code block at point for errors}} 
    `C-c C-v j                     {{insert a header argument with completion}} 
    `C-c C-v v                     {{view expanded body of code block at point}} 
    `C-c C-v I                     {{view information about code block at point}} 
    `C-c C-v g                     {{go to named code block}} 
    `C-c C-v r                     {{go to named result}} 
    `C-c C-v u                     {{go to the head of the current code block}} 
    `C-c C-v n                     {{go to the next code block}} 
    `C-c C-v p                     {{go to the previous code block}} 
    `C-c C-v d                     {{demarcate a code block}} 
    `C-c C-v x                     {{execute the next key sequence in the code edit buffer}} 
    `C-c C-v b                     {{execute all code blocks in current buffer}} 
    `C-c C-v s                     {{execute all code block in current subtree}} 
    `C-c C-v t                     {{tangle code blocks in current file}} 
    `C-c C-v f                     {{tangle code blocks in supplied file}} 
    `C-c C-v i                     {{ingest all code blocks in supplied file into the Library of Babel}} 
    `C-c C-v z                     {{switch to the session of the current code block}} 
    `C-c C-v l                     {{load the current code block into a session}} 
    `C-c C-v a                     {{view sha1 hash of the current code block}} 

$ Capture - Refile - Archiving
    `C-c c                         {{capture a new item (C-u C-u = goto last)}} 
    `C-c C-w                       {{refile subtree (C-u C-u = goto last)}} 
    `C-c C-x C-a                   {{archive subtree using the default command}} 
    `C-c C-x C-s                   {{move subtree to archive file}} 
    `C-c C-x a/A                   {{toggle ARCHIVE tag / to ARCHIVE sibling}} 
    `C-TAB                         {{force cycling of an ARCHIVEd tree}} 

$ Filtering and Sparse Trees
    `C-c /                         {{construct a sparse tree by various criteria}} 
    `C-c / t/T                     {{view TODO's in sparse tree}} 
    `C-c a t                       {{global TODO list in agenda mode}} 
    `C-c a L                       {{time sorted of current org file}} 

$ Tables
    `C-c |                         {{convert region to table}} 

$ Links
    `C-c l                         {{globally store link to the current location}} 
    `C-c C-l                       {{insert a link (TAB completes stored links)}} 
    `C-u C-c C-l                   {{insert file link with the file name completion}} 
    `C-c C-l                       {{edit (also hidden part of) link at point}} 
    `C-c C-o                       {{open file link in emacs}} 
    `C-u C-c C-o                   {{force open file link in emacs/other window}} 
    `mouse-1/2                     {{open link at point}} 
    `mouse-3                       {{force open link in emacs/other window}} 
    `C-c %                         {{record a position in mark ring}} 
    `C-c &                         {{jump back to last followed link(s)}} 
    `C-c C-x C-n                   {{find next link}} 
    `C-c C-x C-p                   {{find previous link}} 
    `C-c '                         {{edit code snippet of file at point}} 
    `C-c C-x C-v                   {{toggle inline display of linked images}} 

$ Structure Editing
    `M-RET                         {{insert new heading/item at current level}} 
    `C-RET                         {{insert new heading after subtree}} 
    `M-S-RET                       {{insert new TODO entry/checkbox item}} 
    `C-S-RET                       {{insert TODO entry/checkbox after subtree}} 
    `C-c -                         {{turn (head)line into item, cycle item type}} 
    `C-c *                         {{turn item/line into headline}} 
    `M-LEFT/RIGHT                  {{promote/demote heading}} 
    `M-S-UP/DOWN                   {{move subtree/list item up/down}} 
    `C-c ^                         {{sort subtree/region/plain-list}} 
    `C-c C-x c                     {{clone a subtree}} 
    `C-c C-x v                     {{copy visible text}} 
    `C-c C-x C-w/M-w               {{kill/copy subtree}} 
    `C-c C-x C-y or C-y            {{yank subtree}} 
    `C-x n s/w                     {{narrow buffer to subtree / widen}} 

