# OpenStack

> Source: http://docs.openstack.org/user-guide/cli_cheat_sheet.html

> Aliases: open-stack, open-stack-cli

$ Identity (keystone)
    `keystone user-list            {{List all users}} 
    `keystone catalog              {{List Identity service catalog}} 

$ Images (glance)
    `glance image-list             {{List images you can access}} 
    `glance image-delete IMAGE     {{Delete specified image}} 
    `glance image-show IMAGE       {{Describe a specific image}} 
    `glance image-update IMAGE     {{Update image}} 
    `glance image-create --name "<NAME>" --disk-format <FORMAT> --container-format <FORMAT> --is-public <True/False> --copy-from <URI>
>                                  {{Upload kernel image}} 
    `glance image-create --name "<NAME>" --disk-format <DISK_FORMAT> --container-format <FORMAT> --is-public <True/False> --copy-from <URI>
>                                  {{Upload RAM image}} 
    `glance image-create --name "<NAME>" --disk-format <FORMAT> --container-format <FORMAT> --is-public <True/False> --copy-from <URI>
>                                  {{Register raw image}} 

$ Compute (nova)
    `nova list                     {{List instances, check status of instance}} 
    `nova image-list               {{List images}} 
    `nova flavor-list              {{List flavors}} 
    `nova boot --image <IMAGE-NAME> --flavor FLAVOR INSTANCE-NAME
>                                  {{Boot an instance using flavor}} 
    `nova boot --image <IMAGE-NAME> --flavor m1.tiny \ MyFirstInstance
>                                  {{Boot an instance using image names}} 
    `ip netns exec <IMAGE-TAG> \ ssh cirros@10.0.0.2
>                                  {{Login to instance}} 
    `nova show MyFirstInstance     {{Show details of instance}} 
    `nova console-log MyFirstInstance
>                                  {{View console log of instance}} 
    `nova meta volumeTwoImage set newmeta='my meta data'
>                                  {{Set metadata on an instance}} 
    `nova image-create volumeTwoImage snapshotOfVolumeImage
>                                  {{Create an instance snapshot}} 
    `nova (pause/unpause/suspend/resume) NAME
>                                  {{Pause/Unpause/Suspend/Unsuspend}} 
    `nova (start/stop/reboot) NAME {{Start/Stop/Reboot}} 
    `nova rescue NAME              {{Rescue}} 
    `nova resize NAME FLAVOR       {{Resize}} 
    `nova rebuild NAME IMAGE       {{Rebuild}} 
    `nova boot --user-data FILE INSTANCE
>                                  {{Inject user data and files into an instance}} 
    `nova keypair-add test > test.pem
>                                  {{Create keypair}} 
    `nova boot --image <IMAGE-NAME> --flavor m1.small \ --key_name test MyFirstServer
>                                  {{Start an instance (boot)}} 
    `ip netns exec <IMAGE-TAG> \ ssh -i test.pem cirros@10.0.0.4
>                                  {{Use ssh to connect to the instance}} 
    `nova secgroup-add-group-rule default default icmp -1 -1
>                                  {{Add rules to default security group allowing ping and SSH b/w instances}} 

$ Networking (neutron)
    `neutron net-create NAME       {{Create network}} 
    `neutron subnet-create NETWORK_NAME CIDR
>                                  {{Create a subnet}} 

$ Block Storage (cinder)
    `cinder create SIZE_IN_GB --display-name NAME
>                                  {{Create a new volume}} 
    `nova boot --image cirros-qcow2 --flavor m1.tiny MyVolumeInstance
>                                  {{Boot an instance and attach to volume}} 
    `cinder list                   {{List volumes, notice status of volume}} 
    `nova volume-attach INSTANCE_ID VOLUME_ID auto
>                                  {{Attach volume to instance after instance is active, and volume is available}} 

$ Volume Management inside Instance
    `fdisk -l                      {{List storage devices}} 
    `mkfs.ext3 /dev/vdb            {{Make filesystem on volume}} 
    `mkdir /myspace                {{Create a mountpoint}} 
    `mount /dev/vdb /myspace       {{Mount the volume at the mountpoint}} 
    `touch /myspace/helloworld.txt {{Create a file on the volume}} 
    `umount /myspace               {{Unmount the volume}} 

$ Object Storage (swift)
    `swift stat (ACCOUNT/CONTAINER/OBJECT)
>                                  {{Display information for the account, container, or object}} 
    `swift list                    {{List containers}} 

