# aptitude

> Source: https://www.debian.org/doc/manuals/debian-reference/ch02.en.html#_interactive_use_of_aptitude

$ Basics
    `u                             {{Update package list}} 
    `U                             {{Mark all packages with updates}} 
    `/                             {{Find a package}} 
    `n                             {{Find next package matching a search <pattern>}} 
    `N                             {{Find next package backward matching a search <pattern>}} 
    `+                             {{Mark a package for installation}} 
    `-                             {{Mark a package for removal}} 
    `g                             {{Install/remove marked packages}} 
    `q                             {{Quit}} 

$ Search patterns
    `<string>                      {{Packages whose name contains <string>}} 
    `!<pattern>                    {{Packages whose name does not contain <pattern>}} 
    `~i<pattern>                   {{Installed packages whose name contains <pattern>}} 
    `^<pattern>                    {{Packages whose name starts with <pattern>}} 
    `<pattern>$                    {{Packages whose name ends with <pattern>}} 
    `~c<pattern>                   {{Removed packages with residual configuration files}} 
    `~v<pattern>                   {{Virtual packages whose name contains <pattern>}} 
    `~d<pattern>                   {{Packages whose description contains <pattern>}} 
    `~D<pattern>                   {{Packages which depend on <pattern>}} 
    `~R<pattern>                   {{Dependencies of the package <pattern>}} 

$ Package management
    `L                             {{Mark a package for reinstallation}} 
    `_                             {{Mark a package and its configuration files for removal}} 
    `:                             {{Keep a package in its current version}} 
    `=                             {{Prevent upgrades of a package}} 
    `M                             {{Mark a package as automatically installed}} 
    `m                             {{Mark a package as manually installed}} 
    `F                             {{Forbid a package version from being installed}} 

$ Conflict resolution
    `e                             {{Examine a solution}} 
    `!                             {{Apply a solution}} 
    `.                             {{Next solution}} 
    `,                             {{Previous solution}} 
    `<                             {{First solution}} 
    `>                             {{Last solution}} 

