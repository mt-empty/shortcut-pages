# SSH

> Source: http://linuxcommand.org/man_pages/ssh1.html

> Aliases: scp

$ Transferring  files  and  Backups
    `ssh user@remotehost           {{Connect to a remote system}} 
    `scp file.txt user1@remotehost:~/
>                                  {{Copy the local file.txt to the remote server}} 
    `scp user@remotehost:~/file.txt  .
>                                  {{Copy a file from a remote server to the local computer}} 
    `cat /home/mynitor/testfile | ssh user@remotehost "cat > /home/mynitor/testfile"
>                                  {{Transfer a local file to remote server}} 
    `ssh user@remotehost "tar cvzf – /home" | tar xvzf – /home
>                                  {{Transfer directory from remote host to local server using ssh and tar:}} 
    `scp -r user@remotehost:/home /home
>                                  {{Recursively copy /home from remote host to local server}} 
    `ssh user@remotehost.com "cat /tmp/remotefile" | diff – /tmp/localfile
>                                  {{Compare a file on remote server with local host}} 

$ Miscellaneous  Tricks
    `cat ~/.ssh/id_rsa.pub | ssh user@remotehost "cat – >> ~/.ssh/authorized_keys"
>                                  {{Setup passwordless SSH access to another server}} 
    `ssh-copy-id    -i  ~/.ssh/id_rsa.pub   user@remotehost
>                                  {{Like the previous example transfer your public key to the remote server}} 
    `ssh user1@remotehost "play /home/user1/2pac.wav"
>                                  {{Play a wav file on remote server}} 
    `dd if=/dev/dsp | ssh -c arcfour -C username@host dd of=/dev/dsp
>                                  {{Outputting your microphone to a remote computer’s speaker}} 

$ Proxy  and  Port  Forwarding  Tricks
    `ssh -D 9999 user@remotehost.com
>                                  {{Tunnel all your browser traffic through your SSH server}} 
    `ssh -X user1@remote_server "xeyes"
>                                  {{Execute one single command}} 
    `ssh -f -N -L 1521:destinationhost.com:80 servertoproxyfrom.com
>                                  {{Use a local server through a proxy server}} 
    `ssh -X user@remotehost.com "xterm"
>                                  {{Launch a local x11 session for a given application}} 
    `ssh -L 5900:localhost:5900 user@yourserver.com
>                                  {{Tunneling VNC over ssh}} 
    `ssh  -t  gatewayhost.com  ssh  destinationhost.com
>                                  {{Jump off one box into another}} 
    `ssh -L 3306:serverB.com:3306 user@serverA.com
>                                  {{Forward connections using server A to get to server B}} 
    ` ssh -R 3333:localhost:22 user@mynitor.com
>                                  {{Reverse SSH Tunneling}} 
    `ssh -T user@hostname.com      {{Log in without appearing in lastlog/w and who output}} 

