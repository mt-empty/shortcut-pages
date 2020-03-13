# Nmap

> Source: http://nmapcookbook.blogspot.com.br/2010/02/nmap-cheat-sheet.html

$ Basic Scanning Techniques
    `nmap [target]                 {{Scan a single target}} 
    `nmap [target1, target2, etc]  {{Scan multiple targets}} 
    `nmap -iL [list.txt]           {{Scan a list of targets}} 
    `nmap [range of IP addresses]  {{Scan a range of hosts}} 
    `nmap [ip address/cdir]        {{Scan an entire subnet}} 
    `nmap -iR [number]             {{Scan random hosts}} 
    `nmap [targets] --exclude [targets]
>                                  {{Excluding targets from a scan}} 
    `nmap [targets] --excludefile [list.txt]
>                                  {{Excluding targets using a list}} 
    `nmap -A [target]              {{Perform an agressive scan}} 
    `nmap -6 [target]              {{Scan an IPv6 target}} 

$ Discovery Options
    `nmap -sn [target]             {{Perform a ping-only scan}} 
    `nmap -Pn [target]             {{Don't ping}} 
    `nmap -PS [target]             {{TCP SYN ping}} 
    `nmap -PA [target]             {{TCP ACK ping}} 
    `nmap -PU [target]             {{UDP ping}} 
    `nmap -PY [target]             {{SCTP INIT ping}} 
    `nmap -PE [target]             {{ICMP echo ping}} 
    `nmap -PP [target]             {{ICMP timestamp ping}} 
    `nmap -PM [target]             {{ICMP address mask ping}} 
    `nmap -PO [target]             {{IP protocol ping}} 
    `nmap -PR [target]             {{ARP ping}} 
    `nmap --traceroute [target]    {{Traceroute}} 
    `nmap -R [target]              {{Force reverse DNS resolution}} 
    `nmap -n [target]              {{Disable reverse DNS resolution}} 
    `nmap --system-dns [target]    {{Alternative DNS lookup}} 
    `nmap --dns-servers [servers] [target]
>                                  {{Manually specify DNS server(s)}} 
    `nmap -sL [targets]            {{Create a host list}} 

$ Advanced Scanning Functions
    `nmap -sS [target]             {{TCP SYN scan}} 
    `nmap -sT [target]             {{TCP connect scan}} 
    `nmap -sU [target]             {{UDP scan}} 
    `nmap -sN [target]             {{TCP NULL scan}} 
    `nmap -sF [target]             {{TCP FIN scan}} 
    `nmap -sA [target]             {{Xmas scan}} 
    `nmap -sA [target]             {{TCP ACK scan}} 
    `nmap --scanflags [flags] [target]
>                                  {{Custom TCP scan}} 
    `nmap -sO [target]             {{IP protocol scan}} 
    `nmap --send-eth [target]      {{Send raw ethernet packets}} 
    `nmap --send-ip [target]       {{Send IP packets}} 

$ Port Scanning Options
    `nmap -F [target]              {{Perform a fast scan}} 
    `nmap -p [port(s)] [target]    {{Scan specific ports}} 
    `nmap -p [port name(s)] [target]
>                                  {{Scan ports by name}} 
    `nmap -sU -sT -p U:[ports],T:[ports] [target]
>                                  {{Scan ports by protocol}} 
    `nmap -p 1-65535 [target]      {{Scan all ports}} 
    `nmap --top-ports [number] [target]
>                                  {{Scan top ports}} 
    `nmap -r [target]              {{Perform a sequential port scan}} 
    `nmap -O --osscan-guess [target]
>                                  {{Attempt to guess an unknown OS}} 
    `nmap -sV [target]             {{Service version detection}} 
    `nmap -sV --version-trace [target]
>                                  {{Troubleshooting version scans}} 
    `nmap -sR [target]             {{Perform a RPC scan}} 

$ Timing Options
    `nmap -T[0-5] [target]         {{Timing templates}} 
    `nmap --ttl [time] [target]    {{Set the packet TTL}} 
    `nmap --min-parallelism [number] [target]
>                                  {{Minimum number of parallel operations}} 
    `nmap --max-parallelism [number] [target]
>                                  {{Maximum number of parallel operations}} 
    `nmap --min-hostgroup [number] [targets]
>                                  {{Minimum host group size}} 
    `nmap --max-hostgroup [number] [targets]
>                                  {{Maximum host group size}} 
    `nmap --initial-rtt-timeout [time] [target]
>                                  {{Maximum RTT timeout}} 
    `nmap --max-rtt-timeout [TTL] [target]
>                                  {{Initial RTT timeout}} 
    `nmap --max-retries [number] [target]
>                                  {{Maximum number of retries}} 
    `nmap --host-timeout [time] [target]
>                                  {{Host timeout}} 
    `nmap --scan-delay [time] [target]
>                                  {{Minimum scan delay}} 
    `nmap --max-scan-delay [time] [target]
>                                  {{Maximum scan delay}} 
    `nmap --min-rate [number] [target]
>                                  {{Minimum packet rate}} 
    `nmap --max-rate [number] [target]
>                                  {{Maximum packet rate}} 
    `nmap --defeat-rst-ratelimit [target
>                                  {{Defeat reset rate limits}} 

$ Firewall Evasion Techniques
    `nmap -f [target]              {{Fragment packets}} 
    `nmap --mtu [MTU] [target]     {{Specify a specific MTU}} 
    `nmap -D RND:[number] [target] {{Use a decoy}} 
    `nmap -sI [zombie] [target]    {{Idle zombie scan}} 
    `nmap --source-port [port] [target]
>                                  {{Manually specify a source port}} 
    `nmap --data-length [size] [target]
>                                  {{Append random data}} 
    `nmap --randomize-hosts [target]
>                                  {{Randomize target scan order}} 
    `nmap --spoof-mac [MAC|0|vendor] [target]
>                                  {{Spoof MAC address}} 
    `nmap --badsum [target]        {{Send bad checksums}} 

$ Output Options
    `nmap -oN [scan.txt] [target]  {{Save output to a text file}} 
    `nmap -oX [scan.xml] [target]  {{Save output to a XML file}} 
    `nmap -oG [scan.txt] [target]  {{Grepable output}} 
    `nmap -oA [path/filename] [target]
>                                  {{Output all supported file types}} 
    `nmap --stats-every [time] [target]
>                                  {{Periodically display statistics}} 
    `nmap -oS [scan.txt] [target]  {{1337 output}} 

$ Troubleshooting and Debugging
    `nmap -h                       {{Getting help}} 
    `nmap -V                       {{Display nmap version}} 
    `nmap -v [target]              {{Verbose output}} 
    `nmap -d [target]              {{Debugging}} 
    `nmap --reason [target]        {{Display port state reason}} 
    `nmap --open [target]          {{Only display open ports}} 
    `nmap --packet-trace [target]  {{Trace packets}} 
    `nmap --iflist                 {{Display host networking}} 
    `nmap -e [interface] [target]  {{Specify a network interface}} 

$ Nmap Scripting Engine
    `nmap --script [script.nse] [target]
>                                  {{Execute individual scripts}} 
    `nmap --script [expression] [target]
>                                  {{Execute multiple scripts}} 
    `nmap --script [category] [target]
>                                  {{Execute scripts by category}} 
    `nmap --script [category1,category2,etc]
>                                  {{Execute multiple script categories}} 
    `nmap --script [script] --script-trace [target]
>                                  {{Troubleshoot scripts}} 
    `nmap --script-updatedb        {{Update the script database}} 

$ Ndiff
    `ndiff [scan1.xml] [scan2.xml] {{Comparison using Ndiff}} 
    `ndiff -v [scan1.xml] [scan2.xml]
>                                  {{Ndiff verbose mode}} 
    `ndiff --xml [scan1.xml] [scan2.xml]
>                                  {{XML output mode}} 

