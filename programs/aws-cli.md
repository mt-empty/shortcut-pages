# Amazon Web Services (AWS) CLI

> Source: https://github.com/toddm92/aws/wiki/AWS-CLI-Cheat-Sheet

> Aliases: aws-cmd, aws-services, aws-basics

$ Amazon S3
    `aws s3 ls                     {{List buckets}} 
    `aws s3api get-bucket-location --bucket <bucket-name>
>                                  {{Bucket location}} 
    `aws s3api get-bucket-logging --bucket <bucket-name>
>                                  {{Logging status}} 
    `aws help                      {{Get help on the command line to see the supported services}} 

$ Autoscaling
    `aws autoscaling describe-auto-scaling-groups --auto-scaling-group-names <as-group-name>
>                                  {{Describe autoscale group details and member instances}} 
    `aws autoscaling help          {{Get the operations for a service}} 
    `aws autoscaling create-auto-scaling-group help
>                                  {{Get the parameters for a service operation}} 

$ CloudFormation
    `aws cloudformation validate-template --template-body file://myCFN.template.json
>                                  {{Template validation (with file)}} 
    `aws cloudformation validate-template --template-url https://s3.amazonaws.com/cfn/myCFN.template.json
>                                  {{Template validation (with URL)}} 
    `aws cloudformation list-stacks --stack-status-filter [ CREATE_COMPLETE | UPDATE_COMPLETE | etc.. ]
>                                  {{Listing stacks}} 
    `aws cloudformation describe-stack-events --stack-name <stack-name>
>                                  {{View stack events}} 
    `aws cloudformation list-stack-resources --stack-name <stack-name>
>                                  {{View stack resources}} 

$ CloudTrail
    `aws cloudtrail create-subscription --name cloudtrail-logs-ue1 --s3-use-bucket cloudtrail-logs --s3-prefix stage --sns-new-topic cloudtrail-stage-notify-ue1
>                                  {{Create a subscription}} 
    `aws cloudtrail describe-trails
>                                  {{Describ status}} 
    `aws cloudtrail get-trail-status --name cloudtrail-logs-ue1
>                                  {{Retrieve status}} 

$ Elastic Compute Cloud (EC2)
    `aws ec2 describe-instances --instance-ids <instance-id>
>                                  {{Describe instance}} 
    `aws ec2 start-instances --instance-ids <instance-id>
>                                  {{Start instance}} 
    `aws ec2 stop-instances --instance-ids <instance-id>
>                                  {{Stop instance}} 
    `aws ec2 reboot-instances --instance-ids <instance-id>
>                                  {{Reboot instance}} 
    `aws ec2 terminate-instances --instance-ids <instance-id>
>                                  {{Kill instance}} 
    `aws ec2 get-console-output --instance-id <instance-id>
>                                  {{Show console output}} 
    `aws ec2 describe-images --image-ids <ami-id>
>                                  {{List images}} 
    `aws ec2 create-image --instance-id <instance-id> --name myAMI --description 'Test AMI'
>                                  {{Create an AMI}} 
    `aws ec2 describe-security-groups --group-names <group-name>
>                                  {{View a security group}} 
    `aws ec2 describe-instance-attribute --instance-id <instance-id> --attribute sriovNetSupport
>                                  {{Check the enhanced networking attribute}} 

$ Virtual Private Cloud (VPC)
    `aws ec2 describe-vpcs         {{Describe VPCs}} 
    `aws ec2 describe-subnets --filters Name=vpc-id,Values=<vpc-id>
>                                  {{Describe VPC subnets}} 
    `aws ec2 describe-route-tables --filters Name=vpc-id,Values=<vpc-id>
>                                  {{Describe VPC routing tables}} 
    `aws ec2 describe-network-acls --filters Name=vpc-id,Values=<vpc-id>
>                                  {{Describe VPC network ACLs}} 
    `aws ec2 describe-vpc-peering-connections
>                                  {{Describe VPC peering connection}} 

$ Elastic Load Balancer (ELB)
    `aws elb describe-load-balancers --load-balancer-names <lb-name>
>                                  {{Describe load balancers}} 
    `aws elb describe-load-balancer-attributes --load-balancer-name <lb-name>
>                                  {{Describe load balancer attributes}} 
    `aws elb describe-load-balancer-policies --policy-names [ <policy-name> | ELBSecurityPolicy-2014-10 ]
>                                  {{Describe load balancer policy}} 
    `aws elb register-instances-with-load-balancer --load-balancer-name <lb-name> --instances <instance-id>
>                                  {{Register instance}} 
    `aws elb deregister-instances-from-load-balancer --load-balancer-name <lb-name> --instances <instance-id>
>                                  {{Remove instance}} 
    `aws elb describe-instance-health --load-balancer-name <lb-name>
>                                  {{View health of ELB instance}} 

$ Identity and Access Management (IAM)
    `aws iam upload-server-certificate --server-certificate-name my.cert.com --certificate-body file://my.cert.com.crt --private-key file://my.cert.com.key --certificate-chain file://Verisign_Chain_CA.crt
>                                  {{Upload a server certificate}} 
    `aws iam list-server-certificates
>                                  {{List your certificates}} 

