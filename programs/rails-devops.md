# Rails Devops

> Source: https://rubytune.com/cheat

$ Process Basics
    `ps auxww -H                   {{All processes, with params + hierarchy}} 
    `pgrep -fl ruby                {{Show all ruby-related PIDs and processes}} 
    `strace -f -p $PID             {{State of the process}} 
    `lsof -p $PID                  {{Show all open files}} 
    `pkill <name of process>       {{Kill process}} 
    `watch 'ps aux | grep ruby'    {{Monitor the process}} 

$ Memory
    `free -m                       {{Free memory}} 
    `vmstat                        {{Report virtual memory statistics}} 
    `ps aux --sort=-resident|head -11
>                                  {{List the top 10 memory hogs}} 
    `kern.log syslog               {{Detect Out of Memory(OOM) and other bad things}} 

$ Terminal and Screen
    `screen -x                     {{ Start a screen session as the current user}} 
    `screen -r                     {{ Join the screen session}} 
    `script filename.out 2> filename.timing
>                                  {{ Record a terminal session}} 
    `scriptreplay filename.timing filename.out
>                                  {{ Playback a recorded terminal session}} 

$ Tips and Tricks
    `sudo !!                       {{Run Previous command as root}} 
    `cd -                          {{Change to last working dir}} 
    `while true;do ruby ghetto.rb;done
>                                  {{Run something forever}} 

$ Network
    `lsof -nPi tcp                 {{TCP sockets in use}} 
    `ip addr/ifconfig              {{Get IP/Ethernet info}} 
    `host <ip-address>             {{Host to IP resolution}} 
    `mtr <url>                     {{Traceroute with stats over time}} 
    `tcptraceroute <url>           {{Traceroute using TCP to avoid ICMP blockage}} 
    `iptables -L                   {{List any IP blocks/rules}} 
    `iptables -I INPUT -s <ip-address> -j DROP
>                                  {{Drop any network requests from IP}} 
    `iftop                         {{Show traffic by port}} 
    `netstat -tlnp                 {{Show all ports listening with process PID}} 
    `wget cachefly.cachefly.net/100mb.test -O /dev/null
>                                  {{D/L speed test (Don't run in production!)}} 

$ Disk/Files
    `iostat -xnk 5                 {{Check reads/writes per disk}} 
    `lsof | grep delete            {{Files(often logs) marked for deletion but not yet deleted}} 
    `df -h                         {{Overview of all disks}} 
    `du -hs                        {{Usage of this dir and all subdirs}} 
    `find . -size +100M            {{Find files over 100MB}} 
    `ls -al /tmp                   {{Low hanging fruit for free space}} 
    `find . -mtime -7              {{Find files created within the last 7 days}} 
    `tail -f file.log | grep <ip-address>
>                                  {{Monitor a log file for an IP or anything else}} 
    `dd if=/dev/zero of=file.txt count=1024 bs=102
>                                  {{Generate a large file}} 

$ Databases
    `pt-query-digest --processlist h=localhost --print --no-report --user xxxx --password *****
>                                  {{"Tail" all queries hitting mysql}} 
    `ssh -L 3307:localhost:3306 user@hostname -N
>                                  {{Connect to production mysql locally on port 3307 via ssh}} 

