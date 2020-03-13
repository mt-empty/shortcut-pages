# htaccess

> Source: http://thejackol.com/htaccess-cheatsheet/

> Aliases: htaccess-file, .htaccess, server-htaccess-file, htaccess-apache, server-htaccess, htaccess-files, apache-htaccess

$ Basic
    `Options +Indexes
## block a few types of files from showing
IndexIgnore *.wmv *.mp4 *.avi
>                                  {{Enable Directory Browsing}} 
    `Options All -Indexes          {{Disable Directory Browsing}} 
    `ErrorDocument 403 /forbidden.html
ErrorDocument 404 /notfound.html
ErrorDocument 500 /servererror.html
>                                  {{Customize Error Messages}} 
    `AddType text/html .html
AddType text/html .shtml
AddHandler server-parsed .html
AddHandler server-parsed .shtml
# AddHandler server-parsed .htm
>                                  {{Get SSI working with HTML/SHTML}} 
    `DirectoryIndex myhome.htm index.htm index.php
>                                  {{Change Default Page (order is followed!)}} 

$ Intermediate
    `<limit GET POST PUT>
order deny,allow
deny from 202.54.122.33
deny from 8.70.44.53
deny from .spammers.com
allow from all
</limit>
>                                  {{Block Users from accessing the site}} 
    `order deny,allow
deny from all
allow from 192.168.0.0/24
>                                  {{Allow only LAN users}} 
    `Redirect oldpage.html http://www.domainname.com/newpage.html
Redirect /olddir http://www.domainname.com/newdir/
>                                  {{Redirect Visitors to New Page/Directory}} 
    `<files file-name>
order allow,deny
deny from all
</files>
>                                  {{Stop .htaccess (or any other file) from being viewed}} 

$ Advanced
    `RewriteEngine on
RewriteCond %{HTTP_REFERER} site-to-block\.com [NC]
RewriteCond %{HTTP_REFERER} site-to-block-2\.com [NC]
RewriteRule .* - [F]
>                                  {{Block site from specific referrers}} 
    `RewriteEngine on
RewriteCond %{HTTP_REFERER} !^$
RewriteCond %{HTTP_REFERER} !^http://(www\.)?mydomain.com/.*$ [NC]
RewriteRule \.(gif|jpg)$ - [F]
>                                  {{Block Hot Linking/Bandwidth hogging}} 
    `# Avoid 500 error by passing chatset
AddDefaultChatset utf-8
>                                  {{Avoid the 500 Error}} 
    `Options +ExecCGI
AddHandler cgi-script cgi pl
# To enable all scripts in a directory use the following
# SetHandler cgi-script
>                                  {{Grant CGI Access in a directory}} 

