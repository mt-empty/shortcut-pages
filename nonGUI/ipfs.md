# IPFS

> Source: https://ipfs.io/docs/commands/

> Aliases: ipns, ipld

$ Configuring
    `export IPFS_PATH=/path/to/ipfsrepo
>                                  {{Path to the repo custom location. By default, the repo is located at `~/.ipfs.`}} 
    `ipfs init                     {{Initialize ipfs local configuration.}} 

$ Options Keys
    `-c, --config [path:string]    {{Path to the configuration file to use.}} 
    `-D, --debug                   {{Operate in debug mode.}} 
    `-h                            {{Show a short version of the command help text.}} 
    `--help                        {{Show the full command help text.}} 
    `-L, --local                   {{Run the command locally, instead of using the daemon.}} 
    `--api [uri:string]            {{Use a specific API instance (defaults to /ip4/127.0.0.1/tcp/5001)}} 

$ Basic Commands
    `ipfs help                     {{Show a short version of the command help text.}} 
    `ipfs init                     {{Initialize ipfs local configuration.}} 
    `ipfs add <path>               {{Add an object to ipfs.}} 
    `ipfs cat <ref>                {{Show ipfs object data.}} 
    `ipfs get <ref>                {{Download ipfs objects.}} 
    `ipfs ls <ref>                 {{List links from an object.}} 
    `ipfs refs <ref>               {{List hashes of links from an object.}} 
    `ipfs add <path>               {{Add an object to ipfs.}} 
    `ipfs add <path>               {{Add an object to ipfs.}} 

$ Advanced Commands
    `ipfs daemon                   {{Start a long-running daemon process.}} 
    `ipfs daemon --mount           {{Start a long-running daemon process and mount and mount an ipfs read-only mountpoint.}} 
    `ipfs mount                    {{Mount an ipfs read-only mountpoint.}} 
    `ipfs resolve                  {{Resolve any type of name.}} 
    `ipfs name                     {{Publish or resolve IPNS names.}} 
    `ipfs dns                      {{Resolve DNS links.}} 
    `ipfs pin                      {{Pin objects to local storage.}} 
    `ipfs repo gc                  {{Garbage collect unpinned objects.}} 

$ Network Commands
    `ipfs id                       {{Show info about ipfs peers.}} 
    `ipfs bootstrap                {{Add or remove bootstrap peers.}} 
    `ipfs swarm                    {{Manage connections to the p2p network.}} 
    `ipfs dht                      {{Query the dht for values or peers.}} 
    `ipfs ping                     {{Measure the latency of a connection.}} 
    `ipfs diag                     {{Print diagnostics.}} 

$ Tool Commands
    `ipfs config                   {{Manage configuration.}} 
    `ipfs version                  {{Show ipfs version information.}} 
    `ipfs update                   {{Download and apply go-ipfs updates.}} 
    `ipfs commands                 {{List all available commands.}} 

