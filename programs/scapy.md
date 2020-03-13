# Scapy

> Source: http://www.secdev.org/projects/scapy/doc/usage.html

> Aliases: python-scapy

$ Data Import and Export Functions
    `rdpcap(file)                  {{Read a pcap file and return a packet list}} 
    `wrpcap(file, pktlist)         {{Write a list of packets to a pcap file}} 

$ Packet Creation and Manipulation Functions
    `Ether()                       {{Create an Ethernet Packet}} 
    `IP()                          {{Create an IP Packet}} 
    `TCP()                         {{Create a TCP Packet}} 
    `UDP()                         {{Create a UDP Packet}} 
    `fuzz()                        {{Transform a layer into a fuzzy layer by replacing some default values by random objects}} 
    `/                             {{Operator to stack packet layers}} 

$ Packet Methods
    `summary()                     {{Display an one-line summary}} 
    `show()                        {{Display a developed view of the packet}} 
    `show2()                       {{Display same as show but on the assembled packet (checksum is calculated, for instance)}} 
    `sprintf()                     {{Display a format string filled with fields values of the packet}} 
    `command()                     {{Return a Scapy command that can generate the packet}} 
    `psdump()                      {{Draws a PostScript diagram of the packet with explained dissection (needs PyX)}} 
    `pdfdump()                     {{Draws a PDF of the packet with explained dissection (needs PyX)}} 

$ Packet Send and Receive Functions
    `send()                        {{Send packets at layer 3}} 
    `sendp()                       {{Send packets at layer 2}} 
    `sniff()                       {{Sniff packets}} 
    `sendpfast()                   {{Send packets at layer 2 using tcpreplay for performance}} 
    `sr()                          {{Send and receive packets at layer 3}} 
    `sr1()                         {{Send packets at layer 3 and return only the first answer}} 
    `srflood()                     {{Flood and receive packets at layer 3}} 
    `srloop()                      {{Send a packet at layer 3 in loop and print the answer each time}} 
    `srp()                         {{Send and receive packets at layer 2}} 
    `srp1()                        {{Send packets at layer 2 and return only the first answer}} 
    `srpflood()                    {{Flood and receive packets at layer 2}} 
    `srploop()                     {{Send a packet at layer 2 in loop and print the answer each time}} 
    `srbt()                        {{Send and receive using a bluetooth socket}} 
    `srbt1()                       {{Send and receive 1 packet using a bluetooth socket}} 

$ Miscellaneous Functions
    `str()                         {{Convert a packet into a hex string}} 
    `ls()                          {{Display the list of fields values of a pkt}} 
    `hexdump()                     {{Display a hexadecimal dump of a pkt}} 
    `hexdiff()                     {{Show differences between 2 binary strings}} 
    `lsc()                         {{List scapy user commands}} 
    `arping()                      {{Send ARP who-has requests to determine which hosts are up}} 
    `traceroute()                  {{Instant TCP traceroute on a list of IP addresses}} 

