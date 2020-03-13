# Amazon Elastic Compute Cloud (EC2)

> Source: http://aws.amazon.com/documentation/ec2/

> Aliases: amazon-elastic-compute-cloud, amazon-ec2, ec2

$ Resource Glossary
    `Amazon Machine Image (AMI)    {{Provides information required to launch an instance. Contains a template for the root volume of an instance, launch permissions, and a block device mapping. (Tagable)}} 
    `Bundle Task                   {{Used to bundle an instance in order to create an instance store-backed AMI. Currently only for instance store-backed Window instances.}} 
    `Customer Gateway              {{A router or software application on your side of a VPN tunnel that is managed by Amazon VPC. (Tagable)}} 
    `Dedicated Host                {{A physical server with EC2 instance capacity dedicated for your use.}} 
    `Elastic Block Store (EBS) Volume
>                                  {{Used to share data between containers and persist the data on the container instance when the containers are no longer running. (Tagable)}} 
    `Instance Store Volume         {{The root device used when an instance is launched from an instance store-backed AMI.}} 
    `Elastic IP Address            {{A static IP address associated with an AWS Account that can be allocated or freed from accounts as needed, and attached/detached from instances as needed.}} 
    `Instance                      {{A copy of an Amazon Machine Image running as a virtual server in the AWS cloud. (Tagable)}} 
    `Key Pair                      {{A set of security credentials you use to prove your identity electronically. A key pair consists of a private key and a public key. Used in EC2 to encrypt and decrypt login information.}} 
    `NAT Gateway                   {{A managed instance that is configured to perform Network Address Translation (NAT) in a VPC. Used enable instances in a private subnet to connect to the Internet or other AWS services, but prevent the Internet from initiating a connection with those instances.}} 
    `Network ACL                   {{An optional layer of security that acts as a firewall for controlling traffic in and out of a subnet. (Tagable)}} 
    `Elsatic Network Interface     {{An elastic network interface (ENI) is a virtual network interface that you can attach to an instance in a VPC. (Tagable)}} 
    `Placement Group               {{A logical cluster compute instance grouping to provide lower latency and high-bandwidth connectivity between the instances.}} 
    `Reserved Instance             {{An option to guarantee that sufficient capacity will be available to launch Dedicated Instances into a VPC. Heavily discounted compared to on-demand instance prices. (Tagable)}} 
    `Reserved Instance Listing     {{A reference for reserved instances that have been put up for sale in the Reserved Instance Marketplace.}} 
    `Route Table                   {{A set of routing rules that controls the traffic leaving any subnet that is associated with the route table. You can associate multiple subnets with a single route table, but a subnet can be associated with only one route table at a time. (Tagable)}} 
    `Spot Instance Request         {{Request container for new spot instances, including the number of instances, the instance type, the Availability Zone, and the maximum price that you are willing to pay per instance hour (your bid). If your bid exceeds the current Spot price, Amazon EC2 fulfills your request immediately. Otherwise, Amazon EC2 waits until your request can be fulfilled or until you cancel the request. (Tagable)}} 
    `Security Group                {{A named set of allowed inbound network connections for an instance. (Security groups in Amazon VPC also include support for outbound connections.) Each security group consists of a list of protocols, ports, and IP address ranges. A security group can apply to multiple instances, and multiple groups can regulate a single instance. (Tagable)}} 
    `Snapshot                      {{A backup of an EBS volume, stored in Amazon S3. (Tagable)}} 
    `Subnet                        {{A segment of the IP address range of a VPC that EC2 instances can be attached to. (Tagable)}} 
    `Virtual Private Gateway (VPG) {{The Amazon side of a VPN connection that maintains connectivity. The internal interfaces of the virtual private gateway connect to a VPC via the VPN attachment and the external interfaces connect to the VPN connection, which leads to the customer gateway. (Tagable)}} 
    `Virtual Private Cloud (VPC)   {{An elastic network populated by infrastructure, platform, and application services that share common security and interconnection. (Tagable)}} 
    `VPC Endpoint                  {{Enables a private connection between a VPC and an another AWS service without requiring access over the Internet.}} 
    `VPC Flow Log                  {{Log of network traffic in a VPC. Logged to CloudWatch. Useful to troubleshoot connectivity and security issues, and to make sure that network access rules are working as expected.}} 
    `VPC Peering Connection        {{connection between two VPCs that enables you to route traffic between them using private IP addresses. Instances in either VPC can communicate with each other as if they are within the same network. A VPC peering connection can be created between a single account's VPCs, or with a VPC in another AWS account within a single region. (Tagable)}} 
    `VPN Connection                {{Connection between a VPC and some other network, such as a corporate data center, home network, or co-location facility. (Tagable)}} 

$ CloudWatch Metrics
    `CPU Credit Usage              {{(Only valid for T2 instances) The number of CPU credits consumed during the specified period. (Units: Count)}} 
    `CPU Credit Balance            {{(Only valid for T2 instances) The number of CPU credits that an instance has accumulated. (Units: Count)}} 
    `CPU Utilization               {{The percentage of allocated EC2 compute units that are currently in use on the instance. (Units: Percent)}} 
    `Disk Read Ops                 {{Completed read operations from all ephemeral disks available to the instance in a specified period of time. (Units: Count)}} 
    `Disk Write Ops                {{Completed write operations to all ephemeral disks available to the instance in a specified period of time. (Units: Count)}} 
    `Disk Read Bytes               {{Bytes read from all ephemeral disks available to the instance. (Units: Bytes)}} 
    `Disk Write Bytes              {{Bytes written to all ephemeral disks available to the instance (Units: Bytes)}} 
    `Network In                    {{The number of bytes received on all network interfaces by the instance. (Units: Bytes)}} 
    `Network Out                   {{The number of bytes sent out on all network interfaces by the instance. (Units: Bytes)}} 
    `Status Check Failed           {{A combination of Status Check Failed 'Instance' and 'System' that reports if either of the status checks has failed. (Values: 0 (passed) or 1 (failed)) (Units: Count)}} 
    `Status Check Failed (Instance)
>                                  {{Reports whether the instance has passed the EC2 instance status check in the last minute. (Values: 0 (passed) or 1 (failed)) (Units: Count)}} 
    `Status Check Failed (System)  {{Reports whether the instance has passed the EC2 system status check in the last minute. (Values: 0 (passed) or 1 (failed)) (Units: Count)}} 

$ Instance Types
    `T2                            {{General purpose, burstable performance instances that provide a baseline level of CPU performance with the ability to burst above the baseline.}} 
    `M4                            {{General purpose instances that provide a balance of compute, memory, and network resources.}} 
    `M3                            {{Older generation general purpose instances that provide a balance of compute, memory, and network resources.}} 
    `C4                            {{Compute-optimized instances that provide high performing processors.}} 
    `C3                            {{Older generation compute-optimized instances that provide high performing processors.}} 
    `R3                            {{Memory-optimized instances that provide lowest cost per GiB of RAM on EC2.}} 
    `G2                            {{Optimized for graphical and general purpose GPU compute applications.}} 
    `I2                            {{High storage instances that provide very fast SSD-backed instance storage optimized for very high random I/O performance, and provide high IOPS.}} 
    `D2                            {{Dense storage instances that provide high disk throughput.}} 

$ Instance Metadata Categories
    `Instance Metadata Service Base URL
>                                  {{The following items can be derived within an EC2 instance by querying the instance metadata service at this url: http://169.254.169.254/latest/meta-data/}} 
    `ami-id                        {{The AMI ID used to launch the instance.}} 
    `ami-launch-index              {{Indicates the order in which the instance was launched. The value of the first instance launched is 0.}} 
    `ami-manifest-path             {{The path to the AMI's manifest file in Amazon S3.}} 
    `ancestor-ami-ids              {{The AMI IDs of any instances that were rebundled to create this AMI.}} 
    `block-device-mapping/ami      {{The virtual device that contains the root/boot file system.}} 
    `block-device-mapping/ebsN     {{The virtual devices associated with Amazon EBS volumes, if any are present. Replace N with index of the Amazon EBS volume.}} 
    `block-device-mapping/ephemeralN
>                                  {{The virtual devices associated with ephemeral devices, if any are present. Replace N with index of the ephemeral volume.}} 
    `block-device-mapping/root     {{The virtual devices or partitions associated with the root devices, or partitions on the virtual device, where the root (/ or C:) file system is associated with the given instance.}} 
    `block-device-mapping/swap     {{The virtual devices associated with swap. Not always present.}} 
    `hostname                      {{The private hostname of the instance. In cases where multiple network interfaces are present, this refers to the eth0 device (the device for which the device number is 0).}} 
    `iam/info                      {{If there is an IAM role associated with the instance at launch, contains information about the last time the instance profile was updated, including the instance's LastUpdated date, InstanceProfileArn, and InstanceProfileId.}} 
    `iam/security-credentials/role-name
>                                  {{If there is an IAM role associated with the instance at launch, role-name is the name of the role, and role-name contains the temporary security credentials associated with the role.}} 
    `instance-action               {{Notifies the instance that it should reboot in preparation for bundling. Valid values: none | shutdown | bundle-pending.}} 
    `instance-id                   {{The ID of this instance.}} 
    `instance-type                 {{The type of instance.}} 
    `kernel-id                     {{The ID of the kernel launched with this instance, if applicable.}} 
    `local-hostname                {{The private DNS hostname of the instance.}} 
    `local-ipv4                    {{The private IP address of the instance.}} 
    `mac                           {{The instance's media access control (MAC) address.}} 
    `network/interfaces/macs/mac/device-number
>                                  {{The unique device number associated with that interface. The device number corresponds to the device name.}} 
    `network/interfaces/macs/mac/ipv4-associations/public-ip
>                                  {{The private IPv4 addresses that are associated with each public-ip address and assigned to that interface.}} 
    `network/interfaces/macs/mac/local-hostname
>                                  {{The interface's local hostname.}} 
    `network/interfaces/macs/mac/local-ipv4s
>                                  {{The private IP addresses associated with the interface.}} 
    `network/interfaces/macs/mac/mac
>                                  {{The instance's MAC address.}} 
    `network/interfaces/macs/mac/owner-id
>                                  {{The ID of the owner of the network interface.}} 
    `network/interfaces/macs/mac/public-hostname
>                                  {{The interface's public DNS. If the instance is in a VPC, this category is only returned if the enableDnsHostnames attribute is set to true.}} 
    `network/interfaces/macs/mac/public-ipv4s
>                                  {{The Elastic IP addresses associated with the interface. There may be multiple IP addresses on an instance.}} 
    `network/interfaces/macs/mac/security-groups
>                                  {{Security groups to which the network interface belongs. (VPC only)}} 
    `network/interfaces/macs/mac/security-group-ids
>                                  {{IDs of the security groups to which the network interface belongs. (VPC only)}} 
    `network/interfaces/macs/mac/subnet-id
>                                  {{The ID of the subnet in which the interface resides. (VPC only)}} 
    `network/interfaces/macs/mac/subnet-ipv4-cidr-block
>                                  {{The CIDR block of the subnet in which the interface resides. (VPC only)}} 
    `network/interfaces/macs/mac/vpc-id
>                                  {{The ID of the VPC in which the interface resides. (VPC only)}} 
    `network/interfaces/macs/mac/vpc-ipv4-cidr-block
>                                  {{The CIDR block of the VPC in which the interface resides. (VPC only)}} 
    `placement/availability-zone   {{The Availability Zone in which the instance launched.}} 
    `product-codes                 {{Product codes associated with the instance.}} 
    `public-hostname               {{The instance's public DNS. If the instance is in a VPC, this category is only returned if the enableDnsHostnames attribute is set to true.}} 
    `public-ipv4                   {{The public IP address. If an Elastic IP address is associated with the instance, the value returned is the Elastic IP address.}} 
    `public-keys/0/openssh-key     {{Public key. Only available if supplied at instance launch time.}} 
    `ramdisk-id                    {{The ID of the RAM disk specified at launch time, if applicable.}} 
    `reservation-id                {{The ID of the reservation.}} 
    `security-groups               {{The names of the security groups applied to the instance.}} 
    `services/domain               {{The domain for AWS resources for the region; for example, amazonaws.com for us-east-1.}} 
    `spot/termination-time         {{The approximate time, in UTC, that the operating system for your Spot instance will receive the shutdown signal. This item is present and contains a time value (for example, 2015-01-05T18:02:00Z) only if the Spot instance has been marked for termination by Amazon EC2.}} 

$ Purchasing Options
    `On-Demand Instances           {{Instances that can be provisioned immediately and paid for by each hour used.}} 
    `Reserved Instances            {{Instances that are paid for upfront in a bulk, discounted sum.}} 
    `Spot Instances                {{Instances that are bid on and provisioned based on a fluctuating 'Spot Price'. If a spot instance request's bid price exceeds the current spot price for given availability zone, it will be provisioned. If a running instance's bid price falls under the current spot price for that same availability zone, it will be terminated.}} 

$ Instance Lifecycle States
    `Pending                       {{When an instance is launched, or restarted after being in the stopped state, it enters the pending state.}} 
    `Running                       {{After the instance is ready, it enters the running state. Billing starts when this state is entered.}} 
    `Rebooting                     {{An instance enters this state when a reboot has been triggered via Amazon EC2. The instance stays on the same host computer and maintains its public DNS name, private IP address, and any data on its instance store volumes.}} 
    `Stopping                      {{When you stop your instance, it enters the stopping state.}} 
    `Stopped                       {{After the instance has completed stopping, it enters the stopped state. Billing for instance usage stops in this state.  we move the instance to a new host computer. If the instance is started again, it will move to a new host computer and any data on the instance store volumes (ephemeral, not EBS-backed) on the previous host computer will be lost.}} 
    `Shutting Down                 {{When an instance begins the process of termination, it enters the shutting down state. Billing for instance usage stops in this state.}} 
    `Terminated                    {{When an instance has completed the process of termination, it enters this state. It cannot be connected to or recovered.}} 

$ Running Instance (Per-Region) Default Limits
    `m4.4xlarge                    {{On-Demand Limit: 10 | Reserved Limit: 20}} 
    `m4.10xlarge                   {{On-Demand Limit: 5 | Reserved Limit: 20}} 
    `c4.4xlarge                    {{On-Demand Limit: 10 | Reserved Limit: 20}} 
    `c4.8xlarge                    {{On-Demand Limit: 5 | Reserved Limit: 20}} 
    `cg1.4xlarge                   {{On-Demand Limit: 2 | Reserved Limit: 20}} 
    `hi1.4xlarge                   {{On-Demand Limit: 2 | Reserved Limit: 20}} 
    `cr1.8xlarge                   {{On-Demand Limit: 2 | Reserved Limit: 20}} 
    `g2.2xlarge                    {{On-Demand Limit: 5 | Reserved Limit: 20}} 
    `g2.8xlarge                    {{On-Demand Limit: 2 | Reserved Limit: 20}} 
    `r3.4xlarge                    {{On-Demand Limit: 10 | Reserved Limit: 20}} 
    `r3.8xlarge                    {{On-Demand Limit: 5 | Reserved Limit: 20}} 
    `i2.xlarge                     {{On-Demand Limit: 8 | Reserved Limit: 20}} 
    `i2.2xlarge                    {{On-Demand Limit: 8 | Reserved Limit: 20}} 
    `i2.4xlarge                    {{On-Demand Limit: 4 | Reserved Limit: 20}} 
    `i2.8xlarge                    {{On-Demand Limit: 2 | Reserved Limit: 20}} 
    `d2.4xlarge                    {{On-Demand Limit: 10 | Reserved Limit: 20}} 
    `d2.8xlarge                    {{On-Demand Limit: 5 | Reserved Limit: 20}} 
    `t2.nano                       {{On-Demand Limit: 20 | Reserved Limit: 20}} 
    `t2.micro                      {{On-Demand Limit: 20 | Reserved Limit: 20}} 
    `t2.small                      {{On-Demand Limit: 20 | Reserved Limit: 20}} 
    `t2.medium                     {{On-Demand Limit: 20 | Reserved Limit: 20}} 
    `t2.large                      {{On-Demand Limit: 20 | Reserved Limit: 20}} 
    `All Other Instance Types      {{On-Demand Limit: 20 | Reserved Limit: 20}} 

$ Resource Default Limits
    `Elastic IP Addresses (EC2-Classic)
>                                  {{5}} 
    `Security Groups Per Instance (EC2-Classic)
>                                  {{500}} 
    `Rules per security group (EC2-Classic)
>                                  {{100}} 
    `Key Pairs                     {{5000}} 
    `Reserved Instances            {{20 instance reservations per AZ, per month}} 
    `AMI copies                    {{50 concurrent copies; 25 from a single source region}} 

