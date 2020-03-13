# Linux Ubuntu

> Source: http://www.cheat-sheets.org/saved-copy/ubunturef.pdf

$ Privileges
    `sudo command                  {{Run command as root}} 
    `sudo -s                       {{Open a root shell}} 
    `sudo -s -u user               {{Open a shell as user}} 
    `sudo -k                       {{Forget sudo passwords}} 
    `gksudo command                {{Visual sudo dialog (GNOME)}} 
    `kdesudo command               {{Visual sudo dialog (KDE)}} 
    `sudo visudo                   {{Edit /etc/sudoers}} 
    `gksudo nautilus               {{Root file manager (GNOME)}} 
    `kdesudo konqueror             {{Root file manager (KDE)}} 
    `passwd                        {{Change your password}} 

$ Display
    `sudo /etc/init.d/gdm restart  {{Restart X and return to login (GNOME)}} 
    `sudo /etc/init.d/kdm restart  {{Restart X and return to login (KDE)}} 
    `(file) /etc/X11/xorg.conf     {{Display configuration}} 
    `sudo dexconf                  {{Reset xorg.conf configuration}} 

$ System Services
    `start service                 {{Start job service (Upstart)}} 
    `stop service                  {{Stop job service (Upstart)}} 
    `status service                {{Check if service is running (Upstart)}} 
    `/etc/init.d/service start     {{Start service(SysV)}} 
    `/etc/init.d/service stop      {{Stop service (SysV)}} 
    `/etc/init.d/service status    {{Check service (SysV)}} 
    `/etc/init.d/service restart   {{Restart service (SysV)}} 
    `runlevel                      {{Get current runlevel}} 

$ Package Management
    `apt-get update                {{Refresh available updates}} 
    `apt-get upgrade               {{Upgrade all packages}} 
    `apt-get dist-upgrade          {{Upgrade with package replacements; upgrade Ubuntu version}} 
    `apt-get install pkg           {{Install pkg}} 
    `apt-get purge pkg             {{Uninstall pkg}} 
    `apt-get autoremove            {{Remove obsolete packages}} 
    `apt-get -f install            {{Try to fix broken packages}} 
    `dpkg --configure -a           {{Try to fix broken packages}} 
    `dpkg -i pkg.deb               {{Install file pkg.deb}} 
    `(file) /etc/apt/sources.list  {{APT repository list}} 

$ Network
    `ifconfig                      {{Show network information}} 
    `iwconfig                      {{Show wireless information}} 
    `sudo iwlist scan              {{Scan for wireless networks}} 
    `sudo /etc/init.d/networking restart
>                                  {{Reset network for manual configurations}} 
    `(file) /etc/network/interfaces
>                                  {{Manual configuration}} 
    `ifup interface                {{Bring interface online}} 
    `ifdown interface              {{Disable interface}} 

$ Special Packages
    `ubuntu-desktop                {{Standard Ubuntu environment}} 
    `kubuntu-desktop               {{KDE desktop}} 
    `xubuntu-desktop               {{XFCE desktop}} 
    `ubuntu-minimal                {{Core Ubuntu utilities}} 
    `ubuntu-standard               {{Standard Ubuntu utilities}} 
    `ubuntu-restricted-extras      {{Non-free, but useful}} 
    `kubuntu-restricted-extras     {{KDE of the above}} 
    `xubuntu-restricted-extras     {{Packages used to compile programs}} 
    `build-essential               {{packages used to compile programs}} 
    `linux-image-generic           {{Latest generic kernel image}} 
    `linux-headers-generic         {{Latest build headers}} 

$ Firewall
    `ufw enable                    {{Turn on the firewall}} 
    `ufw disable                   {{Turn off the firewall}} 
    `ufw default allow             {{Allow all connections by default}} 
    `ufw default deny              {{Drop all connections by default}} 
    `ufw status                    {{Current status and rules}} 
    `ufw allow port                {{Allow traffic on port}} 
    `ufw deny port                 {{Block port}} 
    `ufw deny from ip              {{Block ip address}} 

$ Application Names
    `nautilus                      {{File manager (GNOME)}} 
    `dolphin                       {{File manager (KDE)}} 
    `konqueror                     {{Web browser (KDE)}} 
    `kate                          {{Text editor (KDE)}} 
    `gedit                         {{Text editor (GNOME)}} 

$ System
    `Recovery                      {{Type the phrase REISUB while holding down Alt and SysRq (PrintScrn) with about 1 second between each letter. Your system will reboot}} 
    `lsb_release -a                {{Get Ubuntu version}} 
    `uname -r                      {{Get kernel version}} 
    `uname -a                      {{Get all kernel information}} 

