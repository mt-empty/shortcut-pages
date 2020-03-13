# Subversion

> Source: http://svnbook.red-bean.com/

> Aliases: subversion

$ Basic Usage
    `svn checkout http://svn.example.com/svn/repo/trunk
>                                  {{Create a working copy into current folder}} 
    `svn checkout http://svn.example.com/svn/repo/trunk "/path/to/targetfolder"
>                                  {{Create a working copy into target folder}} 
    `svn update                    {{Update your working copy}} 
    `svn add [file]                {{Add file}} 
    `svn add *                     {{Add all items, recursively}} 
    `svn add * --force             {{Force recursion into versioned directories}} 
    `svn delete [file]             {{Delete file}} 
    `svn status                    {{List changed files}} 
    `svn diff                      {{View changes}} 
    `svn revert [file]             {{Revert changes made to file}} 
    `svn revert -R .               {{Revert all changes}} 
    `svn commit -m "[descriptive commit message]"
>                                  {{Send changes made in working copy to the repository}} 

$ Commit Log
    `svn log                       {{Display commit log messages}} 
    `svn log -l [number]           {{Display commit log messages, number parameter limiting how many are shown}} 
    `svn log -v                    {{Display commit log messages with all the paths affected by each commit}} 

$ Advanced Usage
    `svn update -r [revision]      {{Fetch specific revision to working copy}} 
    `svn merge -c -[revision] .    {{Remove changes made in specific revision}} 
    `svn patch [patch]             {{Apply changes from a patch file to the working copy}} 
    `svn info                      {{View repository information}} 
    `svn copy [source file] [destination file]
>                                  {{Copy file}} 
    `svn move [source file] [destination file]
>                                  {{Move file (same as running svn copy followed by svn delete)}} 
    `svn mkdir [directory name] [destination file]
>                                  {{Create directory (same as running mkdir followed by svn add)}} 

