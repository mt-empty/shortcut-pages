# ZFS

> Source: https://www.freebsd.org/doc/handbook/zfs.html

> Aliases: zpool, z-file-system

$ Pools
    `zpool list                    {{Lists the given pools.}} 
    `zpool status [$POOLNAME]      {{Displays the detailed health status.}} 
    `zpool get all $POOLNAME       {{Retrieves the all properties for the pool.}} 
    `zpool set $PROPERTY=$VALUE $POOLNAME
>                                  {{Sets the given property on the pool.}} 
    `zpool create [$POOLTYPE] $POOLNAME $DEVICE1
>                                  {{Create a pool (Pool types: _ | spare | mirror | raidz).}} 
    `zpool replace $POOLNAME $DEV_OLD [$DEV_NEW]
>                                  {{Replaces the old device with new one.}} 
    `zpool destroy $POOLNAME       {{Destroys the given pool.}} 
    `zpool remove $POOLNAME $DEVICE
>                                  {{Remove a physical device from the pool.}} 
    `zpool online $POOLNAME $DEVICE
>                                  {{Device is online and functioning.}} 
    `zpool offline $POOLNAME $DEVICE
>                                  {{Take device explicitly offline.}} 
    `zpool scrub $POOLNAME         {{Begin to examines all data in the pool to verify that checksums are correctly.}} 
    `zpool [attach|detach] $POOLNAME $DEVICE
>                                  {{Attach or Detaches device from a pool.}} 
    `zpool iostat [$POOLNAME]      {{Displays I/O statistics for the given pool.}} 

$ Datasets
    `zfs list                      {{Lists the properties for the given datasets.}} 
    `zfs list -t snapshot /[$DATASET]
>                                  {{Display a list of snapshots from /[] directory.}} 
    `zfs snaphot [-r] $POOLNAME/$DATASET@$SNAPSHOTNAME
>                                  {{Takes a [recursiv] snaphot of dataset.}} 
    `zfs set $OPTION=$VALUE $POOLNAME/$DATASET
>                                  {{Set the property to the given value for a dataset.}} 
    `zfs clone $POOLNAME/$DATASET@$SNAPSHOTNAME $POOLNAME/$CLONE
>                                  {{Creates a clone of the given snapshot.}} 
    `zfs rollback [-rR] $POOLNAME/$DATASET@$SNAPSHOTNAME
>                                  {{Roll back the given dataset to a previous snapshot.}} 
    `zfs destroy $POOLNAME/$DATASET@$SNAPSHOTNAME
>                                  {{Destroys the given dataset.}} 
    `zfs mount $POOLNAME           {{Mounts of the ZFS file systems.}} 
    `zfs umount $POOLNAME[/$MOUNTPOINT]
>                                  {{Unmounts currently mounted ZFS file systems.}} 

