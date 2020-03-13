# Vagrant

> Source: https://docs.vagrantup.com/v2/cli/index.html

> Aliases: vagrantup

$ Getting Started
    `vagrant init                  {{Initializes the current directory to be a Vagrant environment by creating an initial Vagrantfile if one doesn't already exist}} 
    `vagrant up                    {{Creates and configures guest machines according to your Vagrantfile}} 
    `vagrant ssh                   {{SSH into a running Vagrant machine and give you access to a shell}} 
    `vagrant ssh boxname           {{SSH into a running Vagrant machine by giving boxname and give you access to a shell}} 
    `vagrant push                  {{Vagrant can be configured to deploy code}} 
    `vagrant up --provision | tee provision.log
>                                  {{Runs vagrant up, forces provisioning and logs all output to a file}} 
    `vagrant destroy               {{Stops the running machine Vagrant is managing and destroys all resources that were created during the machine creation process}} 
    `vagrant destroy -f            {{Stops the running machine Vagrant is managing and destroys all resources that were created during the machine creation process without asking for confirmation}} 

$ Machines Management
    `vagrant -v                    {{Get the vagrant version}} 
    `vagrant provision             {{Runs any configured provisioners against the running Vagrant managed machine}} 
    `vagrant provision --debug     {{Use the debug flag to increase the verbosity of the output}} 
    `vagrant reload --provision    {{Restart the virtual machine and force provisioning}} 
    `vagrant status                {{Tells you the state of the machines Vagrant is managing}} 
    `vagrant global-status         {{Outputs status of all vagrant machines}} 
    `vagrant halt                  {{Shuts down the running machine Vagrant is managing}} 
    `vagrant reload                {{The equivalent of running a halt followed by an up}} 
    `vagrant suspend               {{Suspends the guest machine Vagrant is managing, rather than fully shutting it down or destroying it}} 
    `vagrant resume                {{resumes a Vagrant managed machine that was previously suspended, perhaps with the suspend command}} 
    `vagrant share                 {{Shares a Vagrant managed machine and provide you with public URL}} 

$ Boxes Management
    `vagrant box add ADDRESS       {{Adds a box with the given address to Vagrant}} 
    `vagrant box list              {{Lists all the boxes that are installed into Vagrant}} 
    `vagrant box outdated          {{Tells you whether or not the box you're using in your current Vagrant environment is outdated}} 
    `vagrant box remove NAME       {{Removes a box from Vagrant that matches the given name}} 
    `vagrant box update            {{Updates the box for the current Vagrant environment if there are updates available}} 

