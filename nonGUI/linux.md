# Linux

> Source: http://www.cheatography.com/davechild/cheat-sheets/linux-command-line/

> Aliases: gnu-linux, unix, gnu/linux

$ Navigation
    `ls                            {{List directory contents}} 
    `ls -alh                       {{Formatted long listing with hidden files}} 
    `cd DIR                        {{Change the current directory to the DIR directory}} 
    `cd ~                          {{Change current directory to $HOME}} 
    `cd /                          {{Change the current directory to the root directory}} 
    `cd ..                         {{Change to the parent of the current directory}} 
    `pwd                           {{Show name of current working directory}} 

$ File Commands
    `mkdir -p DIR                  {{Create directory DIR}} 
    `rm FILE                       {{Remove FILE}} 
    `rm -r DIR                     {{Remove DIR and its contents recursively}} 
    `rm -f FILE                    {{Force remove FILE}} 
    `rm -rf DIR                    {{Recursively and forcefully remove a directory's contents}} 
    `cp FILE1 FILE2                {{Copy the contents of FILE1 to FILE2}} 
    `mv FILE1 FILE2                {{Rename or move FILE1 to FILE2}} 
    `ln -s FILE link               {{Create symbolic link 'link' to FILE}} 
    `touch FILE                    {{Create FILE or change FILE timestamps}} 
    `cmd > FILE                    {{Standard output (stdout) of cmd to file}} 
    `cmd >> file                   {{Append stdout to file}} 
    `cat FILE1 FILE2               {{Concatenate FILE1 and FILE2 and print to stdout}} 
    `less FILE                     {{Output the contents of the FILE. You can scroll up and down}} 
    `more FILE                     {{View contents of FILE one page at a time}} 
    `head FILE                     {{output first 10 lines of FILE}} 
    `tail FILE                     {{Output last 10 lines of FILE}} 
    `tail -f FILE                  {{Output contents of FILE as it grows}} 
    `sed -i 's,foo,bar,g' file.txt {{Replace instances of foo with bar}} 

$ SSH
    `ssh user@host                 {{Connect to host as user}} 
    `ssh -p port user@host         {{Connect using port p}} 
    `ssh -D port user@host         {{Connect and use bind port}} 

$ Installation
    `./configure                   {{Configure the source file}} 
    `make                          {{Compile the source code}} 
    `make install                  {{Install the compiled source code}} 

$ Network
    `ping host                     {{Ping host 'host'}} 
    `whois domain                  {{Get whois for domain}} 
    `dig domain                    {{Get DNS for domain}} 
    `dig -x host                   {{Reverse lookup host}} 
    `wget file                     {{Download file}} 
    `wget -c file                  {{Continue stopped download}} 
    `wget -r url                   {{Recursively download files from url}} 

$ System Info
    `date                          {{Print or set the system date and time}} 
    `cal                           {{Displays a calendar}} 
    `uptime                        {{Tell how long the system has been running}} 
    `w                             {{Show who is logged on and what they are doing}} 
    `whoami                        {{Print effective userid}} 
    `hostname                      {{Show host name}} 
    `uname -a                      {{Print system information}} 
    `cat /proc/cpuinfo             {{Print the cpu info}} 
    `cat /proc/meminfo             {{Print the memory information}} 

$ Process Management
    `top                           {{Show real time processes}} 
    `ps                            {{Report a snapshot of the current processes}} 
    `ps aux                        {{Show processes for all users}} 
    `kill [pid]                    {{Terminate a process}} 
    `bg                            {{Run jobs in the background}} 
    `fg                            {{Run jobs in the foreground}} 
    `fg n                          {{Bring job n to the foreground}} 
    `du                            {{Estimate file space usage}} 
    `du -sh                        {{Summarize file space usage and print sizes in human readable format}} 
    `free -h                       {{Display amount of free and used memory in the system}} 
    `whereis                       {{Locate the binary, source, and manual page files for a command}} 
    `which                         {{Locate a command}} 

$ Searching and Sorting
    `grep pattern FILE             {{Search for pattern in FILE}} 
    `grep -r pattern DIR           {{Search recursively for pattern in DIR}} 
    `command | grep pattern        {{Search for the pattern in in the output of command}} 
    `find /dir/ -name name*        {{Find files starting with name in dir}} 
    `find /dir/ -user name         {{Find files owned by name in dir}} 
    `locate FILE                   {{Find all instances of FILE}} 
    `sort FILE                     {{Sort the content of FILE alphabetically}} 
    `sort -r FILE                  {{Sort in reverse}} 
    `sort -R FILE                  {{Sort randomly}} 

$ File Permissions
    `chmod octal FILE              {{Change permission of FILE}} 
    `4                             {{read (r)}} 
    `2                             {{write (w)}} 
    `1                             {{execute (x)}} 

$ Compression
    `tar cf FILE.tar files         {{Tar files into FILE.tar}} 
    `tar xf FILE.tar               {{Untar into current directory}} 
    `tar tf FILE.tar               {{List the contents of an archive}} 
    `gzip FILE                     {{Compress FILE and rename to FILE.gz}} 
    `gzip -d FILE.gz               {{Decompress FILE.gz}} 

