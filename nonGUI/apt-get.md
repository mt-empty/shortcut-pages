# AptGet

> Source: https://help.ubuntu.com/community/AptGet/Howto

> Aliases: aptget, apt-get

$ Installation commands
    `sudo apt-get install <package_name>
>                                  {{Install a new package}} 
    `sudo apt-get build-dep <package_name>
>                                  {{This command searches the repositories and installs the build dependencies for 'package_name'}} 
    `sudo apt-get install <package1_name> <package2_name> <package3_name>
>                                  {{Install multiple packages}} 

$ Maintenance commands
    `sudo apt-get update           {{Update source list}} 
    `sudo apt-get upgrade          {{Upgrade all installed packages}} 
    `sudo apt-get dist-upgrade     {{Upgrade all installed packages with a 'smart' conflict resolution system}} 
    `sudo apt-get check            {{Update package lists and check for broken dependencies}} 
    `sudo apt-get download <package_name>
>                                  {{Download the archive file for <package_name> into the current directory}} 
    `sudo apt-get -f install       {{Fix broken packages}} 
    `sudo apt-get autoclean        {{Remove all .deb files for packages that are no longer installed on the system}} 
    `sudo apt-get clean            {{Remove all packages from the package cache}} 

$ Removal commands
    `sudo apt-get remove <package_name>
>                                  {{Remove an installed package, leaving configuration files intact}} 
    `sudo apt-get purge <package_name>
>                                  {{Completely remove a package and the associated configuration files}} 
    `sudo apt-get remove <package1> <package2>+
>                                  {{Remove package1 and install package2 in one step (+operator)}} 
    `sudo apt-get autoremove       {{Remove packages that were installed by other packages and are no longer needed}} 
    `sudo apt-get autoremove <package_name>
>                                  {{Removes an installed package and dependencies}} 

$ Search commands
    `apt-cache search <search_term>
>                                  {{Find packages that include <search_item>}} 
    `apt-cache show <package_name> {{Shows the description of package <package_name> and other relevant information including version, size, dependencies and conflicts}} 
    `apt-cache pkgnames            {{Shows all the available packages}} 
    `apt-cache showpkg <package_name>
>                                  {{Shows the dependencies for <package_name>}} 

