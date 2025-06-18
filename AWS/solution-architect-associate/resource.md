
==================================
Architecture and Tools
---------------------------
In this course:

- cover how regions and availability zones (AZ) affect resource placement and high availability
- cover how shared responsibility applies to AWS services
- Describe the AWS well-architected Framework
- Match AWS services to specific business needs
- Get the CLI and PowerShell tools running on the windows and linux platforms to enable AWS management
- Use Cloud Shell for command line management
- Cover how AWS Outposts allow the use of AWS services on-premises

----------------------------
AWS global Infrastructure
- 200+ it services available
- Accessible
- scalable (scalein/ scaledown)
- reliable
- Network Latency
- Network Security (HTTPs, VPN)
- encryption of data at rest or in transit
- data centers
- curretly 37 regions and 117 AZ
- 

----------------------------
Shared responsibility
  Cloud Service Categories

- Infrastructure as a service (IaaS)
    Customer manually deploys services such as S3 Buckets, EC2 instances
    They configure and control those items
    For VMs, customer is responsible for the OS, its configuration, apps, patching.
    For VMs, Amazaon is responsible for the underlying hardware and hypervisors

- Platform as a services (PaaS)
    Customer deploys managed platform such as Relational Database Servies (RDS)
    Custome is responsible for limited configuratoin settings and all data
    Amazon manages underlying infrastructure and underlying servies such as EC2 instances.

- Software as a service
    Customer deploys or develops high level software
    Customer is responsible for limited configuration settings and all data
    Amazon manages the underlying infrastructure and VMs and the software

- Amazon S3 Service Level Agreement (SLA)


-------------------------------------------------
AWS Well-Architected Framework
- its a six pilar design principles for cloud-based IT systems
    1- operational excellence
    2- security
    3- reliability
    4- performance efficiency
    5- cost optimization
    6- Sustainability

    Operational Excelence:
    it is all about monitoring your deployed aws sercices to ensure peak efficiency and utilization.
    Can be monitore using performance matrics in cloud watch

    security:
    data confidentiality (both at rest and transit (over the network))
    data integrity (authenticity of data, can be done using cloudtrail auditing)
    IAM users, roles, policies, threat detection

    Reliability:
    distributed system design - Regions, AZs, replication
    Disaster Recovery Planning (DRP)
    Ability to change as needs evolve

    Performance Efficiency : 
    Match service sizing to workload requirements
    Monitor performance metrics and adjust sizing accordingly

    Cost Optimization:
    removing unused resources
    use spot and reserved instances where possible
    Cost budget alerts
    Monitoring usage and performance metrics

    Sustainability:
    AWS: use renewable water and power
    Customer: Optimizes services to meet workload requirements and no more


--------------------------------------
Matching AWS services to Business Needs:
- Business needs assessments
- Familiarity with AWS service offerings
- Network requirements
- Compute requirements
- storage requirements
- Monitoring and security requirements
- AWS service sprawl reduction

Newwork Requirements:
- VPCs, subnets required we need
- VPC peering ( allow you to link VPCs together)
- VPN
- HTTPs 
- Network/threat monitoring : GuardDuty, Cloudwatch network metrics

Compute Requirements:
- EC2 instances
    full configuration control
- Managed Services
    limited indirect VM
    configuration control 

- Application containers 
    Elastic Container Services
    Elastic Container Registry

- Container Clusters
    Elastic kubernetes services

Storage Requirements:
- S3 bucket storage
- Database - NoSQL or SQL based
- Security - Amazon Macie data classification,server side encryption with amazon or customer managed keys


Monitoring and Security:
- CloudWatch monitoring
- CloudTrail Auditing
- Amazon Detective
- Network ACLs
- Security Groups
- Web Application Firewall (WAF)
- Security Standards compliances -- PCI DSS, GDPR


========================================================
Data Storage Services
----------------------------------

Overview:
- Cover how AWS Transfer and Snow Familiy services supports importing data to the aws cloud over the internet as well as 
    through shipping storage devices to AWS data centers

- plan database usage in accordance with anticipated workloads
- Deploy and manage various database solutions such MySQL, Microsoft SQL Server, DynamoDB and DocumentDB
- Create and attach and EBS volume and configure and Elastic File System


-----------------------------------
Using AWS transfer:
- configure aws transfer family
    ssh + FTP = SFTP  (to transfer file from linux host to the S3 bucket)
    - create a s3 bucket 
    - create an IAM role to enable trust relationship between services ( create role for aws service)(AmazonS3FullAccess)
    
    - 