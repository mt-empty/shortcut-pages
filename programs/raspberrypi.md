# Raspberry Pi

> Source: https://gist.github.com/hofmannsven/9132419

> Aliases: raspberry-functions, raspi, raspberry-toolkit, raspberry, raspberry-pi

$ Setup
    `arp -a                        {{Find all available devices}} 
    `Pi Finder                     {{Locate Raspberry (b8:27:eb) in Network}} 

$ SSH
    `ssh pi@rasperrypi             {{Connect to device via SSH + Name}} 
    `ssh pi@192.168.64.xxx         {{Connect to device via SSH + IP}} 

$ System
    `ifconfig                      {{Get system info (e.g. IP)}} 
    `iwconfig                      {{Get network info}} 
    `hostname                      {{Get hostname}} 
    `hostname -I                   {{Get hostname IP}} 
    `lsusb                         {{Check for all connected USB devices}} 
    `sudo raspi-config             {{Switch to config}} 
    `startx                        {{Switch to GUI}} 
    `reboot / sudo reboot          {{Reboot system}} 
    `sudo shutdown -h now          {{Shutdown}} 
    `sudo update-rc.d ssh defaults {{Start SSH while booting}} 

$ Web Server
    `sudo apt-get update & sudo apt-get upgrade
>                                  {{Update system}} 
    `sudo apt-get install apache2 php5
>                                  {{Install Web Server}} 
    `Laravel                       {{Need for mcrypt and GD extension}} 
    `sudo apt-get install mysql-server mysql-client php5-mysql
>                                  {{Install MySQL}} 
    `sudo service apache2 restart  {{Restart}} 
    `sudo apt-get install avahi-daemon
>                                  {{Install Avahi for .local domain}} 

$ Audio
    `omxplayer audio.mp3           {{Play}} 
    `+ & -                         {{Volume}} 

$ Remote Control
    `apt-get install xrdp          {{Install XRDP}} 
    `sudo apt-get install tightvncserver
>                                  {{Install VNC}} 
    `tightvncserver                {{Start VNC}} 
    `5900                          {{Ethernet Port}} 
    `5901                          {{WLAN Port}} 

$ File Sharing
    `sudo apt-get install netatalk {{Install file sharing}} 
    `afp://192.168.64.xxx          {{Connect to Server}} 

$ Disable Power Management
    `cat /sys/module/8192cu/parameters/rtw_power_mgnt
>                                  {{Check the power management flag}} 
    `sudo touch /etc/modprobe.d/8192cu.conf
>                                  {{Create power management file}} 
    `options 8192cu rtw_power_mgnt = 0 rtw_enusbss = 0
>                                  {{Set power management flag to zero in 8192cu.conf file}} 
    `sudo reboot                   {{Reboot}} 

$ Midnight Commander
    `sudo apt-get install mc       {{Install}} 
    `sudo mc                       {{Start}} 

