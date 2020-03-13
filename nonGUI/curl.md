# Curl

> Source: http://linux.about.com/od/commands/l/blcmdl1_curl.htm

> Aliases: curl-options

$ Basic Usage
    `curl [options...] <url>       {{Makes a request to the url given}} 

$ Follow Redirects
    `-L                            {{Follow all the redirects if there in the request}} 

$ Cookies
    `-b cookiejar                  {{Sends Cookies using cookiejar}} 
    `-c cookiejar                  {{Stores Cookies using cookiejar}} 
    `-b 'n1=v1;n2=v2'              {{Sends raw cookies using -b}} 

$ Send Data
    `--data-binary @<filename>     {{Sends file in binary format}} 
    `-d <@filename>                {{Sends file in ASCII format}} 
    `-d <data>                     {{Sends the raw data}} 

$ Headers
    `-H <header>                   {{Specify the header to be sent}} 
    `-i                            {{Prints response header along with response content}} 
    `-l                            {{Sends a HEAD request and prints only response header}} 
    `-A 'User-Agent-Name'          {{Specifies the user agent}} 

$ Exit Codes
    `6                             {{The request can't be resolved}} 
    `7                             {{Couldn't connect to host}} 
    `28                            {{The operation has timed out}} 
    `55                            {{The request could not send data}} 
    `56                            {{The request could not receive data}} 

$ Miscellaneous
    `-v / --verbose                {{Displays data sent and received}} 
    `-m / --max-time               {{Maximum time in seconds the command should execute}} 
    `-k / --insecure               {{Allows insecure requests}} 
    `-s                            {{Hides the progress}} 
    `-S                            {{Displays error when the request fails(when used with -s)}} 

