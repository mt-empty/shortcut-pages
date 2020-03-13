# Netcat

> Source: http://man.openbsd.org/OpenBSD-current/man1/nc.1

> Aliases: nc, ncat

$ General Options
    `nc [options] [host] [port number]
>                                  {{Normal Syntax:}} 
    `nc -4 [host] [port number]    {{Use IPv4 addressing only}} 
    `nc -6 [host] [port number]    {{Use IPv6 addressing only}} 
    `nc -u [host] [port number]    {{UDP instead of TCP}} 
    `nc -r [host]                  {{Use random port number}} 
    `nc -l [host] [port number]    {{Listen for an incoming connection rather than initiate connection}} 
    `nc -k -l [host] [port number] {{Continue listening for connections after first client has disconnected}} 
    `nc -n [host] [port number]    {{No DNS lookups on addresses, hostnames or ports}} 
    `nc -p [source port number] [host] [port number]
>                                  {{Use given source port number when initiating connection}} 
    `nc -s [ip address] [host] [port number]
>                                  {{Use given source ip address}} 
    `nc -w [n] [host] [port number]
>                                  {{Apply "n" second timeout}} 
    `nc -z [host] [port number]    {{Scan for port listeners without transmitting any data}} 
    `nc -v [host] [port number]    {{Verbose output}} 

$ Server Examples
    `netcat -l 5050                {{Listen for TCP connections (port 5050). Data received is directed to STDOUT. Data is captured and transmitted from STDOUT}} 
    `netcat -l 5051 > filename.out {{Data received directed to "filename.out"}} 
    `( echo -ne "HTTP/1.1 200 OK
Content-Length: $(wc -c <index.html)\r\n\r\n" ; cat index.html ) | nc -l 8080
>                                  {{Single use web server listening on port 8080}} 
    `while : ; do ( echo -ne "HTTP/1.1 200 OK\r\nContent-Length: $(wc -c <index.html)\r\n\r\n" ; cat index.html; ) | nc -l -p 8080 ; done
>                                  {{Bash while loop restarts web server after each request}} 

$ Client Examples
    `netcat 192.168.0.1 5050       {{Connect to listening server. Data is captured and transmitted from STDIN. Responses directed to STDOUT}} 
    `netcat 192.168.0.1 5051 < filename.in
>                                  {{Transmit contents of file "filename.in"}} 
    `echo -e "GET / HTTP/1.0\r\n\r\n" | netcat somewebserver.sometld 80
>                                  {{Retrieve web page}} 

$ Simple Proxy Example
    `mknod backpipe p ; nc -l [proxy port] < backpipe | nc [destination host] [destination port] > pipe
>                                  {{Created a named pipe. Setup an a listener on proxy port. Forward requests from listener to a client which in-turn sends them onto the destination host. The client redirects the response from the destination host into the named pipe. The listener picks up the response from the named pipe and returns it. The named pipe thus allows the proxy to transmit data bi-directionally.}} 

$ Port Scanning Examples
    `nc -zv somehost.sometld 80    {{Scan a single TCP port}} 
    `nc -zvu somehost.sometld 53   {{Scan a UDP port}} 
    `nc -zv somehost.sometld 22-58 {{Scan a range of TCP ports}} 
    `nc -zv somehost.sometld 22 23 {{Scan multiple TCP ports}} 

