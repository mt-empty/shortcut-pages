# Iptables

> Source: http://ipset.netfilter.org/iptables.man.html

> Aliases: ip6tables, linux-firewall, iptable

$ Basic Commands
    `sudo iptables -L -v -n        {{List all rules with verbose and numeric output}} 
    `sudo iptables -S              {{Print all rules in iptables-save format}} 
    `sudo iptables -A <chain> <rule>
>                                  {{Append one or more rules to the end of the selected chain}} 
    `sudo iptables -I <chain> <rulenum> <rule>
>                                  {{Insert one or more rules in the selected chain as the given rule number}} 
    `sudo iptables -D <chain> <rulenum>
>                                  {{Delete one or more rules at the given position from the selected chain}} 
    `sudo iptables -P <chain> <target>
>                                  {{Set the policy for the chain to the given target}} 
    `sudo iptables -N <chain>      {{Create a new user-defined chain by the given name}} 
    `sudo iptables -F <chain>      {{Flush the selected chain}} 
    `sudo iptables -X <chain>      {{Delete the optional user-defined chain specified}} 
    `sudo iptables-save > /path/to/file
>                                  {{Save current rules}} 
    `sudo iptables-restore < /path/to/file
>                                  {{Load rules from a file}} 
    `sudo iptables-persistent save {{Save current rules for Debian/Ubuntu}} 

$ Tables
    `filter                        {{Default table containing three built-in chains: "INPUT", "FORWARD", and "OUTPUT"}} 
    `nat                           {{Table for NAT containing three built-in chains: "PREROUTING", "OUTPUT", and "POSTROUTING"}} 

$ Targets
    `ACCEPT                        {{Let the packet through}} 
    `DROP                          {{Silently ignore the packet}} 
    `REJECT                        {{Reject the packet and notify the sender}} 
    `LOG                           {{Turn on kernel logging of matching packets and continue traversing the current chain}} 

$ Parameters
    `-t <table>                    {{Specify the packet matching table}} 
    `-j <target>                   {{Specify the target of the rule}} 
    `-p <protocol>                 {{Specify the protocol of the rule or of the packet to check}} 
    `-i <interface>                {{Specify an interface via which a packet was received}} 
    `-m <matchname> [<per-match-options>]
>                                  {{Specify extended packet matching modules}} 
    `-s x.x.x.x[/<mask>]           {{Specify a source IP address}} 
    `-d x.x.x.x[/<mask>]           {{Specify a destination IP address}} 

$ Matches
    `-m iprange --src-range x.x.x.x-x.x.x.x
>                                  {{Match source IP in the specified range}} 
    `-m iprange --dst-range x.x.x.x-x.x.x.x
>                                  {{Match destination IP in the specified range}} 
    `-p tcp --sport <port>[:<port>]
>                                  {{Match source port or port range}} 
    `-p tcp --dport <port>[:<port>]
>                                  {{Match destination port or port range}} 
    `-m multiport --sports <port>[,<port>|,<port>:<port>]...
>                                  {{Match if the source port is one of the given ports}} 
    `-m multiport --dports <port>[,<port>|,<port>:<port>]...
>                                  {{Match if the destination port is one of the given ports}} 
    `-m mac --mac-source XX:XX:XX:XX:XX:XX
>                                  {{Match source MAC address}} 
    `-m conntrack --ctstate <state>[,<state>]...
>                                  {{Match the state of a packet}} 
    `-m connlimit --connlimit-upto n
>                                  {{Restrict the number of parallel connections to a server per client IP address (or client address block)}} 

