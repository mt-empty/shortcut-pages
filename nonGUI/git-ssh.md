# Git SSH

> Source: https://help.github.com/articles/generating-an-ssh-key/

> Aliases: 

$ List Keys
    `ls -al ~/.ssh                 {{Check for existing keys.}} 

$ Generate Private Keys
    `ssh-keygen -t rsa -b 4096 -C your_email@example.com
>                                  {{Create a new ssh key, using your email as a label}} 

$ Use SSH Agent to Connect
    `eval $(ssh-agent -s)          {{Start ssh-agent}} 
    `ssh-add ~/.ssh/id_rsa         {{Add your private key and password to ssh-agent. (Make sure you have added your public key to your git account.)}} 

$ Test the Connection
    `ssh -T git@github.com         {{ssh to github}} 

