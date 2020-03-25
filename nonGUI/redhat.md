# Red Hat Yum Commands

> Source: https://access.redhat.com/articles/yum-cheat-sheet

> Aliases: red-hat, redhat-yum, redhat-enterprise-yum, red-hat-yum, red-hat-enterprise-yum

$ Yum Queries
    `help                          {{Displays yum commands and options}} 
    `list                          {{List package name form repositories}} 
    `info                          {{Display information about a package}} 
    `deplist                       {{Displays dependencies for a package}} 
    `provides                      {{Find packages that provide the queried file}} 
    `search                        {{Search package name and description for a term}} 
    `updateinfo                    {{Get information about available package updates}} 

$ Troubleshoot
    `check                         {{Check local RPM for problems}} 
    `history                       {{View yum transactions}} 
    `clean                         {{Clear out cached package data}} 
    `fssnapshot                    {{List LVM snapshot}} 
    `fs                            {{Act on file system}} 

$ Package Maintenance
    `install                       {{Install a package from a repository to your system}} 
    `update                        {{Update one or all packages on your system}} 
    `update-to                     {{Update one or all packages to a particular version}} 
    `upgrade                       {{Update packages taking obsoletes into account}} 
    `localinstall                  {{Install a package from a local file, http or ftp}} 
    `downgrade                     {{Downgrade a package to an earlier version}} 
    `reinstall                     {{Reinstall the current version of a package}} 
    `swap                          {{Remove one package and install another}} 
    `erase                         {{Erase a package (and possibly dependencies) from}} 
    `groupinstall                  {{Install all packages in the selected group}} 

$ Repositories
    `repolist                      {{Display enabled software repositories}} 
    `repoinfo                      {{Display information about enabled yum repositories}} 
    `repo-pkgs                     {{Work with packages in a particular repository}} 
    `makecache                     {{Download yum repository data to cache}} 

$ Options for the Yum Command
    `-y                            {{Assume yes if prompted}} 
    `--assumeno                    {{Assume no if prompted}} 
    `-q                            {{Produce no output}} 
    `-v                            {{Produce extra debugging output}} 
    `--noplugins                   {{Run command without loading any yum plugins}} 
    `--disableplugin=              {{Disable a particular plugin for single command}} 
    `--changelog                   {{Display changelog information of package}} 
    `--downloadonly                {{Download to /var/cache/yum/arch/prod/repo/packages/, but don’t install}} 

$ Miscellaneous
    `find-repos-of-install         {{Find which repository a package comes from}} 
    `reposync                      {{Synchronize yum repositories to a local directory}} 
    `repotrack                     {{Download a package and all its dependencies}} 
    `show-installed                {{List installed RPM packages and statistics}} 
    `yumdb                         {{Check or change the yum database}} 
    `yumdownloader                 {{Download a package from a repo to current directory}} 
    `repoclosure                   {{Get unmet dependency list from repositories}} 

