# Perforce Workshop

> Source: https://swarm.workshop.perforce.com

> Aliases: p4workshop

$ Setup
    `export P4USER=<user_name>     {{Sets the user name}} 
    `export P4PORT=workshop.perforce.com:1666
>                                  {{Sets the Workshop's server and port}} 
    `p4 login                      {{Log into the Perforce Workshop}} 

$ Create Repositories
    `p4 init                       {{Initialize a personal server}} 
    `p4 clone -p workshop.perforce.com:1666 -f //guest/depot/path/to/project/...
>                                  {{Clone a project using depot path syntax}} 

$ Making Changes
    `p4 status                     {{Show status of added, deleted, or modified files to be submitted}} 
    `p4 reconcile                  {{Stage changes to be submitted}} 
    `p4 submit -d "Description"    {{Submits changes to local repository}} 

$ Synchronize with the Workshop
    `$ p4 push                     {{Push changes to the Workshop}} 
    `$ p4 fetch                    {{Fetch changes from the Workshop}} 

