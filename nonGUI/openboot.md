# OpenBoot

> Source: http://irtfweb.ifa.hawaii.edu/~spex/computers/spex1/techdocs/1201-hilodog/SunOBP_Quick_Ref.pdf

> Aliases: sun-openboot, sun-boot-prompt, sun-open-boot-prom

$ Basic Commands
    `banner                        {{Shows up the startup banner}} 
    `boot                          {{Boots the system from its default device}} 
    `boot disk                     {{Boots from hard drive #1}} 
    `boot floppy                   {{Boots from floppy}} 
    `boot net                      {{Quickboots from network}} 
    `boot cdrom                    {{Boots from CD drive}} 
    `power-off                     {{Switches off the machine}} 

$ Other Helpful Commands
    `eject floppy                  {{Ejects the floppy}} 
    `eject cdrom                   {{Ejects the CD drive}} 
    `Stop N                        {{Re-sets all NVRAM contents}} 
    `set-defaults                  {{Sets the entire PROM to default values}} 
    `reset                         {{Restarts the system}} 
    `devalias                      {{Shows all device aliases}} 
    `printenv                      {{Shows all NVRAM envs}} 
    `probe-scsi-all                {{Re-Scans devices on all SCSI buses}} 

