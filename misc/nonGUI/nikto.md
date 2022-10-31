# Nikto

> Source: http://www.r00tsec.com/2014/06/cheatsheet-nikto-cheat-sheet.html

$ Installation
    `sudo apt-get install nikto    {{Install Nikto on Ubuntu}} 
    `C:\pentest\nikto-2.1.5>perl nikto.pl -h example.com
>                                  {{Install Nikto on windows (On windows first install the perl interpreter)}} 
    `nikto -host example.com -port 8080
>                                  {{Basic Usage}} 

$ Display Options
    `1                             {{Show redirects}} 
    `2                             {{Show cookies received}} 
    `3                             {{Show all 200/OK responses}} 
    `4                             {{Show URLs which require authentication}} 
    `D                             {{Debug Output}} 
    `E                             {{Display all HTTP errors}} 
    `P                             {{Print progress to STDOUT}} 
    `S                             {{Scrub output of IPs and hostnames}} 
    `V                             {{Verbose Output}} 

$ Evasion Options
    `1                             {{Random URI encoding (non-UTF8)}} 
    `2                             {{Directory self-reference (/./)}} 
    `3                             {{Premature URL ending}} 
    `4                             {{Prepend long random string}} 
    `5                             {{Fake parameter}} 
    `6                             {{TAB as request spacer}} 
    `7                             {{Change the case of the URL}} 
    `8                             {{Use Windows directory separator}} 
    `A                             {{Use a carriage return (0x0d) as a request spacer}} 
    `B                             {{Use binary value 0x0b as a request spacer}} 

$ Tuning
    `0                             {{File Upload}} 
    `1                             {{Interesting File / Seen in logs}} 
    `2                             {{Misconfiguration / Default File}} 
    `3                             {{Information Disclosure}} 
    `4                             {{Injection (XSS/Script/HTML)}} 
    `5                             {{Remote File Retrieval - Inside Web Root}} 
    `6                             {{Denial of Service}} 
    `7                             {{Remote File Retrieval - Server Wide}} 
    `8                             {{Command Execution / Remote Shell}} 
    `9                             {{SQL Injection}} 
    `a                             {{Authentication Bypass}} 
    `b                             {{Software Identification}} 
    `c                             {{Remote Source Inclusion}} 
    `x                             {{Reverse Tuning Options (i.e., include all except specified)}} 

$ Mutate Options
    `1                             {{Test all files with all root directories}} 
    `2                             {{Guess for password file names}} 
    `3                             {{Enumerate user names via Apache (/~user type requests)}} 
    `4                             {{Enumerate user names via cgiwrap (/cgi-bin/cgiwrap/~user type requests)}} 
    `5                             {{Attempt to brute force sub-domain names, assume that the host name is the parent domain}} 
    `6                             {{Attempt to guess directory names from the supplied dictionary file}} 

$ Output File Format
    `Use –o (-output) option       {{To save file with file extension}} 
    `csv                           {{Comma-separated-value}} 
    `htm                           {{HTML Format}} 
    `msf                           {{Log to Metasploit}} 
    `nbe                           {{Nessus NBE format}} 
    `txt                           {{Plain text}} 
    `xml                           {{XML Format}} 

$ Basic Options
    `-host                         {{Host(s) to target (Can be an IP address, hostname or text file of hosts)}} 
    `-vhost                        {{Specify the Host header to be sent to the target}} 
    `-port                         {{Specify Port Number}} 
    `-ssl                          {{Only test SSL on the ports specified}} 
    `-save                         {{Save Request & Response Headers}} 
    `replay.pl                     {{Can be replayed with}} 
    `-useproxy                     {{Use the HTTP proxy defined in the configuration file}} 
    `-maxtime                      {{Maximum testing time per host secs}} 
    `-H or –h                      {{Display extended help information}} 
    `-until                        {{Run for specified time or duration}} 
    `-update                       {{Update the plugins and databases directly from cirt.net}} 
    `-dbcheck                      {{Check the scan databases for syntax errors}} 
    `-config                       {{Specify an alternative config file to use instead of the Nikto.conf file located in the install directory}} 
    `-Version                      {{Display the Nikto software, plugin and database versions}} 

$ Advanced Options
    `-nossl                        {{Disables SSL}} 
    `-ssl                          {{Force SSL}} 
    `-no404                        {{Disables 404 Guessing}} 
    `-id (Format is 'id:password') {{Host authentication}} 
    `-key                          {{Client certificate key file}} 
    `-ask                          {{Whether to ask about submitting updates}} 
    `-Cgidirs                      {{Scan these CGI directories}} 
    `–findonly                     {{Only discover the HTTP(S) ports, do not perform a security scan}} 
    `–IgnoreCode(Format is '302,301')
>                                  {{Ignore these HTTP codes as negative responses (always)}} 
    `-list-plugins                 {{All plugins that Nikto can run against targets and then will exit without performing a scan}} 
    `-nolookup                     {{Do not perform name lookups on IP addresses}} 
    `-nocache                      {{Disable response cache}} 
    `–nointeractive                {{Disable interactive features}} 
    `-Pause                        {{Seconds (integer or floating point) to delay between each test}} 
    `-root                         {{Prepend the value specified to the beginning of every request}} 
    `-timeout                      {{Seconds to wait before timing out a request}} 
    `-userdbs                      {{Load user defined databases instead of standard databases}} 

