# Pacman Package Manager

> Source: https://wiki.archlinux.org/index.php/Pacman

> Aliases: linux-arch, pacman, yaourt, antergos-linux, arch-distro, manjaro-linux, chakra-linux, antergos, arch, manjaro

$ Pacman - Package manager utility
    `pacman -S xyz                 {{Install package xyz}} 
    `pacman -Syy                   {{Force synchronization of repository databases}} 
    `pacman -Ss xyz                {{Search repository database for packages for xyz}} 
    `pacman -Sy xyz                {{Really synchronize repo and install xyz}} 
    `pacman -R xyz                 {{Remove package xyz but keep its dependencies installed}} 
    `pacman -Rs xyz                {{Remove package xyz and all its dependencies (if they are not required by any other package)}} 
    `pacman -Rsc xyz               {{Remove package xyz, all its dependencies and packages that depend on the target package}} 
    `pacman -Ql xyz                {{Show all files installed by the package xyz}} 
    `pacman -Qo /path              {{Find the package which installed the file at /path}} 
    `pacman -Syu                   {{Sync and Upgrade}} 
    `pacman -Sc                    {{Remove all cached packages that are not currently installed}} 
    `pacman -U /path/to/package/package_name-version.pkg.tar.xz
>                                  {{Install a 'local' package that is not from a remote repository (e.g. the package is from the AUR)}} 
    `pacman -Sw xyz                {{Download package xyz without installing it}} 

$ Yaourt - Yaourt is a pacman frontend with added features
    `yaourt -Syu --devel --aur     {{Sync database, upgrade packages, search aur and devel (all packages based on dev version) upgrades}} 
    `yaourt -Sb                    {{Build package from source}} 
    `yaourt -C                     {{Check, edit, merge or remove *.pac* files}} 
    `yaourt -G                     {{Get a PKGBUILD (support splitted package)}} 
    `yaourt -Sb --export           {{Build and export package, its sources to a directory}} 
    `yaourt -B                     {{Backup database}} 
    `yaourt -Q --backupfile        {{Query backup file}} 

$ Removing Packages
    `pacman -R xyz                 {{Remove package 'xyz', leaving all of its dependencies installed}} 
    `pacman -Rs xyz                {{ Remove package 'xyz' and its dependencies which are not required by any other installed package}} 
    `pacman -Rsc xyz               {{Remove package 'xyz', its dependencies and all the packages that depend on the target package}} 
    `pacman -Rdd xyz               {{Remove package 'xyz', which is required by another package, without removing the dependent package}} 
    `pacman -Rn xyz                {{Prevent the creation of the backup configuration files use the -n option}} 

