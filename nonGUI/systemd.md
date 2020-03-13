# Systemd

> Source: https://www.cheatography.com/tme520/cheat-sheets/systemd/

> Aliases: system-services, system-manager, system-service, systemctl

$ Services Management
    `systemctl start <SERVICE>     {{Start a SERVICE (not reboot persistent) Ex: systemctl start httpd.service}} 
    `systemctl stop <SERVICE>      {{Stop a SERVICE (not reboot persistent) Ex: systemctl stop httpd.service}} 
    `systemctl restart <SERVICE>   {{Restart a SERVICE Ex: systemctl restart httpd.service}} 
    `systemctl reload <SERVICE>    {{Reloads the configuration files without interrupting pending operations Ex: systemctl reload httpd.service}} 
    `systemctl condrestart <SERVICE>
>                                  {{Restarts if the SERVICE is already running Ex: systemctl condrestart httpd.service}} 
    `systemctl status <SERVICE>    {{Shows the status of a SERVICE Ex: systemctl status httpd.service}} 
    `systemctl list-units --type=service
>                                  {{Displays the status of all services}} 
    `systemctl list-unit-files --type=service
>                                  {{List the services that can be started or stopped}} 
    `ls /etc/systemd/system/*.wants/
>                                  {{Print a list of services (alternative)}} 
    `systemctl enable <SERVICE>    {{Start SERVICE at next boot Ex: systemctl enable httpd.service}} 
    `systemctl disable <SERVICE>   {{SERVICE won't be started on next boot Ex: systemctl disable httpd.service}} 
    `systemctl is-enabled <SERVICE>
>                                  {{Check if a SERVICE is configured to start in the current environment Ex: systemctl is-enabled httpd.service}} 
    `systemctl daemon-reload       {{Run this command after a change in any configuration file (old or new)}} 
    `systemctl -H <HOST> status network
>                                  {{Run any systemctl command remotely}} 

$ Investigate and Logs
    `systemctl get-default         {{Determine which target unit is used by default.}} 
    `systemctl set-default multi-user.target
>                                  {{Change default boot target to multi-user.target}} 
    `journalctl -b                 {{Show all messages from last boot}} 
    `journalctl -b -p err          {{Show all messages of priority level ERROR and more from last boot}} 
    `journalctl -f                 {{Follow messages as they appear}} 
    `journalctl -k                 {{Show only kernal messages}} 
    `journalctl -u <SERVICE>       {{Show logs for SERVICE}} 
    `journalctl --full             {{Display all messages without truncating any}} 
    `systemctl --state=failed      {{Display the services that failed to start}} 
    `systemctl list-units --type=target
>                                  {{Show current runlevel}} 
    `systemctl isolate graphical.target
>                                  {{Change the current runlevel (target)}} 
    `systemctl emergency           {{Switch to Emergency mode (single user)}} 
    `systemctl kill <SERVICE>      {{Gently kill SERVICE (SIGTERM, 15)}} 
    `systemd-cgls                  {{Show the full systemd control group (cgroup) hierarchy as a tree}} 
    `systemctl list-jobs           {{Show jobs}} 
    `systemctl list-dependencies   {{Show units and its dependencies}} 

$ System State
    `systemctl halt                {{Halts the system}} 
    `systemctl poweroff            {{Powers off the system}} 
    `systemctl reboot              {{Restarts the system}} 
    `systemctl suspend             {{Suspends the system}} 
    `systemctl hibernate           {{Hibernates the system}} 
    `systemctl hybrid-sleep        {{Hibernates and suspend the system}} 

