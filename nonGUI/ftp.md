# FTP

> Source: http://www.smartfile.com/blog/the-ultimate-ftp-commands-list/

> Aliases: file-transfer-protocol

$ Establish Connection
    `open                          {{Connects to the specified FTP server}} 
    `status                        {{Displays the current status of FTP connections}} 
    `user                          {{Specifes a user to the remote computer}} 

$ Download
    `get                           {{Copies a single remote file to the local computer}} 
    `mget                          {{Copies one or more remote files to the local computer}} 
    `recv                          {{Copies a remote file to the local computer}} 

$ Upload
    `put                           {{Copies a single local file to the remote computer}} 
    `mput                          {{Copies one or more local files to the remote computer}} 
    `send                          {{Copies a local file to the remote computer (same as “put”)}} 
    `append                        {{Appends a local file to a file on the remote computer}} 

$ Toggle Transfer Type
    `ascii                         {{Sets the file transfer type to ASCII, the default}} 
    `binary                        {{Sets the file transfer type to binary}} 
    `type                          {{Sets or displays the file transfer type (default = ASCII)}} 

$ Navigate On Remote
    `ls                            {{Displays an abbreviated list of a remote directory’s files and subdirectories}} 
    `dir                           {{Displays a list of a remote directory’s files and subdirectories}} 
    `pwd                           {{Displays the current directory on the remote computer (literally, “print working directory”)}} 
    `cd                            {{Changes the working directory on the remote computer}} 
    `mkdir                         {{Creates a remote directory}} 
    `rename                        {{Renames remote files}} 
    `mdir                          {{Displays a list of a remote directory’s files and subdirectories}} 
    `mls                           {{Displays an abbreviated list of a remote directory’s files and subdirectories}} 

$ Delete On Remote
    `delete                        {{Deletes a single file on a remote computer}} 
    `mdelete                       {{Deletes one or more files on a remote computer}} 
    `rmdir                         {{Deletes a remote directory}} 

$ Local
    `!                             {{Runs the specified command on the local computer}} 
    `lcd                           {{Changes the working directory on the local computer}} 

$ Help
    `?                             {{Displays descriptions for ftp commands}} 
    `help                          {{Displays descriptions for ftp commands}} 
    `remotehelp                    {{Displays help for remote commands}} 

$ Misc Settings
    `hash                          {{Toggles hash sign (#) printing for each data block transferred (default = OFF)}} 
    `bell                          {{Toggles a bell to ring after each file transfer command is completed (default = OFF)}} 
    `verbose                       {{Toggles verbose mode (default = ON)}} 
    `prompt                        {{Toggles prompting (default = ON)}} 
    `trace                         {{Toggles packet tracing (default = OFF)}} 
    `glob                          {{Toggles filename globbing (wildcard characters) (default = ON)}} 
    `debug                         {{Toggles debugging (default = OFF)}} 

$ Close Connection
    `bye                           {{Ends the FTP session and exits ftp}} 
    `quit                          {{Ends the FTP session with the remote computer and exits ftp (same as “bye”)}} 
    `close                         {{Ends the FTP session and returns to the command interpreter}} 
    `disconnect                    {{Disconnects from the remote computer, retaining the ftp prompt}} 

$ Command Line Options
    `-v                            {{Suppresses verbose display of remote server responses}} 
    `-n                            {{Suppresses auto login}} 
    `-i                            {{Turns off interactive prompting during multiple file transfers}} 
    `-d                            {{Enables debugging, displaying all ftp commands passed between the client and server}} 
    `-g                            {{Disables filename globbing, which permits the use of wildcard chracters in local file and path names}} 
    `-s:filename                   {{Specifies a text file containing ftp commands; the commands will automatically run after ftp starts. No spaces are allowed in this parameter. Use this switch instead of redirection (>)}} 
    `-a                            {{Use any local interface when binding data connection}} 
    `-w:windowsize                 {{Overrides the default transfer buffer size of 4096}} 
    `-computer                     {{Specifies the computer name or IP address of the remote computer to connect to. The computer, if specified, must be the last parameter on the line}} 

