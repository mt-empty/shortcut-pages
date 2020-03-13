# NPM

> Source: https://docs.npmjs.com/#cli

$ Getting Started
    `npm init                      {{Interactively create a package.json file}} 
    `npm install                   {{Install packages based on package.json file in the current folder}} 
    `npm search <term>             {{Search the registry for packages matching the search terms}} 
    `npm update -g <package_name>  {{Updates all the packages to the latest version, respecting semver}} 
    `npm help <command>            {{Show help for the specific command}} 
    `npm search <package_name>     {{Search for the package}} 

$ Installing Packages
    `npm install <package_name>    {{Install the latest version of a package}} 
    `npm install <package_name>@<version>
>                                  {{Install specific version of a package}} 
    `npm install -g <package_name> {{Install a package globally, usually for command line use (On *nix requires sudo)}} 
    `npm install -S <package_name> {{Install a package and append it in the dependencies section of your package.json}} 
    `npm install -D <package_name> {{Install a package and append it in the devDependencies section of your package.json}} 
    `npm install -O <package_name> {{Install a package and append it in the optionalDependencies section of your package.json}} 

$ Uninstalling Packages
    `npm uninstall <package_name>  {{Uninstall the latest version of a package}} 
    `npm uninstall <package_name>@<version>
>                                  {{Uninstall specific version of a package}} 
    `npm uninstall -g <package_name>
>                                  {{Uninstall the package globally}} 
    `npm uninstall -S <package_name>
>                                  {{Uninstall the package and append it in the dependencies section of your package.json}} 
    `npm uninstall -D <package_name>
>                                  {{Uninstall the package and append it in the devDependencies section of your package.json}} 
    `npm uninstall -O <package_name>
>                                  {{Uninstall the package and append it in the optionalDependencies section of your package.json}} 

$ Package Details
    `npm docs <package_name>       {{Show the docs for a package in a web browser}} 
    `npm bugs <package_name>       {{Show the issues for a package in a web browser}} 
    `npm repo <package_name>       {{Open package repository page in the browser}} 
    `npm ls                        {{Print all the versions of packages that are installed, as well as their dependencies}} 

