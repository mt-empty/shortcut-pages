# Homebrew

> Source: http://brew.sh/

$ Essential Commands
    `brew info $FORMULA            {{Display information about formula.}} 
    `brew home $FORMULA            {{Open formula's homepage in a browser.}} 
    `brew options $FORMULA         {{Display install options specific to formula.}} 
    `brew install $FORMULA         {{Installs formula on the system.}} 
    `brew [rm | remove | uninstall] $FORMULA
>                                  {{Uninstalls formula from the system.}} 
    `brew search [search]          {{Display all locally available formulae for brewing (including tapped ones).}} 
    `brew [list | ls] $FORMULA     {{Without any arguments,  list all installed formulae.  If  formulae are given, list the installed files for formulae}} 
    `brew update                   {{Fetch the newest version of Homebrew and all formulae from GitHub.}} 
    `brew upgrade [--all | $FORMULA]
>                                  {{Upgrade outdated, unpinned brews.}} 

$ Troubleshooting
    `brew doctor                   {{Check your system for potential problems. Doctor exits with a non-zero status if any problems are found.}} 
    `brew config                   {{Show Homebrew and system configuration useful for debugging.}} 
    `brew --env                    {{Show a summary of the Homebrew build environment.}} 
    `brew --version                {{Print the version number of brew to standard error and exit.}} 

$ Brewing
    `brew create [URL]             {{Generate a formula for the downloadable file at URL and open it in the editor.}} 
    `brew edit $FORMULA            {{Open formula in the editor.}} 

