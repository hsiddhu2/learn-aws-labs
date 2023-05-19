# Automating AWS Resource Deployment using CloudFormation

## Objective: 

*The goal of this AWS lab is to create a CloudFormation stack template to automates the deployment of a web application on AWS.*


## Instructions:

### 1. Create a CloudFormation template that accomplishes the following tasks:

    - Creates a Virtual Private Cloud (VPC) with a two public subnet and and two private subnet.

    - Creates an Internet Gateway and attaches it to the VPC.

    - Configures the routing tables for the public and private subnets.

    - Creates a security group for an Amazon EC2 instance with rules allowing inbound HTTP and SSH traffic.

    - Launches an EC2 instance in the public subnet. 
  
    - The instance should run a web server and a python script to make a connection to the database (see the user data included below)

    - Creates a Multi AZ Amazon RDS database instance in the private subnet.

### 2. Use the following as the parameters for your CloudFormation template:

    - VPC CIDR block
    - Public subnet CIDR block
    - Private subnet CIDR block
    - EC2 instance type
    - RDS instance class
    - RDS database name, username, and password
    - Instance key pair name

### 3. The following user data can be included in the template (update values as necessary):

Link to [User Data](userdata.yml) 

This user data installs a web server and python dependencies and then runs a simple Flask application that connects to the RDS database, adds a record, and then retrieves the message from the database.


## Solution
   
**Complete Solution:**  [here](template.yml)

## References: 

1. [EC2 Instance](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html)
2. [AWS RDS Instance](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html)
3. [AWS RDS DB Security Group](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-security-group.html)
4. [AWS RDS DB Subnet Group](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbsubnetgroup.html)
5. [FreeCloudLabs.com](https://medium.com/@freecloudlabs)
