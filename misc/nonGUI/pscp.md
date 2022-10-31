# Pscp

> Source: http://the.earth.li/~sgtatham/putty/0.53b/htmldoc/Contents.html

> Aliases: pscp-arguments, putty-scp-arguments, putty-scp, pscp-options, putty-scp-options

$ Basics
    `pscp [options] [[user@]host:]source target
>                                  {{Copy file(s) from source as to target}} 
    `pscp [[user@]host:]source/&#42;.c target/
>                                  {{Copy files matching wildcard. SSH 1 server might produce warnings. See -unsafe.}} 

$ Behavior
    `-p                            {{Preserver original file timestamps}} 
    `-r                            {{Copy directories recursively}} 
    `-batch                        {{Avoid interactive promts by negative answers. This will allow unattended PSCP to fail instead of hanging indefinitely.}} 
    `-C                            {{Enable compression}} 
    `-v                            {{show verbose messages}} 
    `-q                            {{Quiet, don't show statistics}} 
    `-unsafe                       {{Allow server-side wildcards (DANGEROUS). This allows SSH 1 servers to return files that do not strictly match request (e.g. source.c for *.c wildcard)}} 

$ Connection
    `-load sessname                {{Load settings from saved session}} 
    `-P port                       {{Connect to specified port}} 
    `-l user                       {{Connect with specified username. PSCP will try to authenticate using Pageant if Pageant is running.}} 
    `-pw passw                     {{Login with specified password}} 
    `-i key                        {{Private key for authentication}} 
    `-load sessname                {{Load settings from saved session}} 
    `-1 -2                         {{Force use of particular SSH protocol version}} 

$ Return value
    `pscp file*.* user@hostname:
if errorlevel 1 echo There was an error
>                                  {{PSCP returns an ERRORLEVEL of zero (success) only if the files were correctly transferred. You can test for this in a batch file, using code such as above.}} 

