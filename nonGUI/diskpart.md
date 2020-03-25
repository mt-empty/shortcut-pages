# Diskpart

> Source: https://technet.microsoft.com/en-us/library/cc766465(v=ws.10).aspx

> Aliases: windows-diskpart-command, cmd-diskpart

$ Create a new partition and format a partition
    `SELECT DISK                   {{Selects the specified disk and shifts the focus to it.}} 
    `CREATE PARTITION PRIMARY      {{Creates a primary partition on the current basic disk.}} 
    `ASSIGN                        {{Assigns a drive letter or mount point to the volume with focus.}} 
    `SELECT PARTITION              {{Selects the specified partition and gives it focus.}} 
    `FORMAT                        {{Formats the volume or partition.}} 

$ Commands you may then issue at the DISKPART prompt
    `LIST DISK                     {{Displays a list of disks and information about them.}} 
    `LIST PARTITION                {{Displays the partitions listed in the partition table of the current disk.}} 
    `LIST VOLUME                   {{Displays a list of basic and dynamic volumes on all disks.}} 
    `SELECT VOLUME                 {{Selects the specified volume and shifts the focus to it.}} 
    `SELECT PARTITION              {{Selects the specified partition and gives it focus.}} 
    `DETAIL DISK                   {{Displays the properties of the selected disk and the volumes on that disk.}} 
    `DETAIL PARTITION              {{Displays the properties of the selected partition.}} 
    `DETAIL VOLUME                 {{Displays the disks on which the current volume resides.}} 
    `REM                           {{Provides a way to add comments to a script.}} 
    `EXIT                          {{Exits the DiskPart command interpreter.}} 

$ Commands to Manage Basic Disks
    `ASSIGN                        {{Assigns a drive letter or mount point to the volume with focus.}} 
    `CREATE PARTITION Extended     {{Creates an extended partition on the current drive.}} 
    `CREATE PARTITION Logical      {{Creates a logical drive in the extended partition.}} 
    `DELETE PARTITION              {{Deletes the partition with focus.}} 
    `REMOVE                        {{Removes a drive letter or mount point from the volume with focus.}} 

$ Commands to Manage Dynamic Disks
    `ADD disk                      {{Mirrors the simple volume with focus to the specified disk.}} 
    `BREAK disk                    {{Breaks the mirrored volume with focus into two simple volumes.}} 
    `CREATE VOLUME Simple          {{Creates a simple volume.}} 
    `CREATE VOLUME Stripe          {{Creates a striped volume by using two or more specified dynamic disks.}} 
    `CREATE VOLUME Raid            {{Creates a RAID-5 volume on three or more specified dynamic disks.}} 
    `DELETE DISK                   {{Deletes a missing dynamic disk from the disk list.}} 
    `DELETE VOLUME                 {{Deletes the selected volume.}} 
    `EXTEND                        {{Extends the volume with focus into the next contiguous unallocated space.}} 
    `IMPORT                        {{Imports a foreign disk group into the local computer's disk group.}} 
    `ONLINE                        {{Brings an offline disk or volume with focus online.}} 
    `RETAIN                        {{Prepares an existing dynamic simple volume to use as a boot or system volume.}} 

$ Commands to Convert Disks
    `CONVERT mbr                   {{Converts an empty basic disk with the GUID Partition Table (GPT) partition style to a basic disk with the master boot record (MBR) partition style.}} 
    `CONVERT gpt                   {{Converts an empty basic disk with the master boot record (MBR) partition style into a basic disk with the GUID partition table (GPT) partition style.}} 
    `CONVERT dynamic               {{Converts a basic disk into a dynamic disk. Any existing partitions on the disk become simple volumes.}} 
    `CONVERT basic                 {{Converts an empty dynamic disk into a basic disk.}} 
    `CLEAN                         {{Removes any and all partition or volume formatting from the disk with focus.}} 

