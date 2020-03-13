# Salt Cloud

> Source: https://docs.saltstack.com/en/latest/ref/cli/

$ Options
    `salt --version                {{Print the version of Salt that is running}} 
    `salt --versions-report        {{Show program's dependencies and version number, and then exit}} 
    `salt -h                       {{Show the help message and exit}} 
    `salt -c                       {{The location of the Salt configuration directory. This directory contains the configuration files for Salt master and minions. The default location on most systems is /etc/salt}} 

$ Execution Options
    `salt-cloud -L                 {{Specify which region to connect to}} 
    `salt-cloud -a                 {{Perform an action that may be specific to this cloud provider. This argument requires one or more instance names to be specified}} 
    `salt-cloud -f <FUNC-NAME> <PROVIDER>
>                                  {{Perform a function that may be specific to this cloud provider, that does not apply to an instance. This argument requires a provider to be specified (i.e.: nova)}} 
    `salt-cloud-m MAP              {{Specify a map file to use. If used without any other options, this option will ensure that all of the mapped VMs are created. If the named VM already exists then it will be skipped}} 
    `salt-cloud -H                 {{When specifying a map file, the default behavior is to ensure that all of the VMs specified in the map file are created. If the --hard option is set, then any VMs that exist on configured cloud providers that are not specified in the map file will be destroyed. Be advised that this can be a destructive operation and should be used with care}} 
    `salt-cloud -d                 {{Pass in the name(s) of VMs to destroy, salt-cloud will search the configured cloud providers for the specified names and destroy the VMs. Be advised that this is a destructive operation and should be used with care. Can be used in conjunction with the -m option to specify a map of VMs to be deleted}} 
    `salt-cloud -P                 {{Normally when building many cloud VMs they are executed serially. The -P option will run each cloud vm build in a separate process allowing for large groups of VMs to be build at once.  Be advised that some cloud provider's systems don't seem to be well suited for this influx of vm creation. When creating large groups of VMs watch the cloud provider carefully}} 
    `salt-cloud -u                 {{Update salt-bootstrap to the latest develop version on GitHub}} 
    `salt-cloud -y                 {{Default yes in answer to all confirmation questions}} 
    `salt-cloud -k                 {{Do not remove files from /tmp/ after deploy.sh finishes}} 
    `salt-cloud --show-deploy-args {{Include the options used to deploy the minion in the data returned}} 
    `salt-cloud --script-args      {{Script arguments to be fed to the bootstrap script when deploying the VM}} 

$ Query Options
    `salt-cloud -Q                 {{Execute a query and return some information about the nodes running on configured cloud providers}} 
    `salt-cloud -F                 {{Execute a query and print out all available information about all cloud VMs. Can be used in conjunction with -m to display only information about the specified map}} 
    `salt-cloud -S                 {{Execute a query and print out selected information about all cloud VMs. Can be used in conjunction with -m to display only information about the specified map}} 
    `salt-cloud --list-providers   {{Display a list of configured providers}} 
    `salt-cloud --list-profiles    {{New in version 2014.7.0. | Display a list of configured profiles. Pass in a cloud provider to view the provider's associated profiles, such as digital_ocean, or pass in all to list all the configured profiles}} 

$ Cloud Providers Listings
    `salt-cloud --list-locations   {{Display a list of locations available in configured cloud providers. Pass the cloud provider that available locations are desired on, aka "linode", or pass "all" to list locations for all configured cloud providers}} 
    `salt-cloud --list-images      {{Display a list of images available in configured cloud providers. Pass the cloud provider that available images are desired on, aka "linode", or pass "all" to list images for all configured cloud providers}} 
    `salt-cloud --list-sizes       {{Display a list of sizes available in configured cloud providers. Pass the cloud provider that available sizes are desired on, aka "AWS", or pass "all" to list sizes for all configured cloud providers}} 

$ Output Options
    `salt-cloud --out              {{Pass in an alternative outputter to display the return of data. This outputter can be any of the available outputters}} 
    `salt-cloud --out-indent       {{Print the output indented by the provided value in spaces. Negative values disable indentation. Only applicable in outputters that support indentation}} 
    `salt-cloud --out-file         {{Write the output to the specified file}} 
    `salt-cloud --no-color         {{Disable all colored output}} 
    `salt-cloud --force-color      {{Force colored output}} 

