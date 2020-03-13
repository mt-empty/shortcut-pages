# Portage

> Source: https://wiki.gentoo.org/wiki/Gentoo_Cheat_Sheet#Portage_package_management

> Aliases: portage, gentoo, emerge, gentoo-package-management

$ Package Installation/Removal
    `emerge www-client/firefox     {{Install a package and its dependencies}} 
    `emerge =www-client/firefox-24.8.0
>                                  {{Install a specific version of a package}} 
    `emerge -cav www-client/firefox
>                                  {{Remove a package and its dependencies}} 
    `emerge -C www-client/firefox  {{Remove a package but not its dependencies}} 
    `emerge -av --depclean         {{Remove no longer needed packages}} 

$ Package Upgrades
    `emerge -u @world              {{Upgrade installed packages}} 
    `emerge -avuDU --with-bdeps=y --keep-going=y @world
>                                  {{Upgrade installed packages and dependencies}} 

$ Updating the Repositories
    `emerge --sync                 {{Update repositories}} 
    `emerge-webrsync               {{Update repositories by fetching snapshots}} 

$ Miscellaneous Operations
    `revdep-rebuild -v             {{Check for and rebuild missing libraries}} 
    `perl-cleaner --all            {{After updating perl-core packages}} 
    `python-updater                {{After updating python core packages}} 

