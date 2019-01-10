![alt text](bless_logo.png "BLESS")
# BLESS - Bastion's Lambda Ephemeral SSH Service
[![Build Status](https://travis-ci.org/Netflix/bless.svg?branch=master)](https://travis-ci.org/Netflix/bless) [![Test coverage](https://coveralls.io/repos/github/Netflix/bless/badge.svg?branch=master)](https://coveralls.io/github/Netflix/bless) [![Join the chat at https://gitter.im/Netflix/bless](https://badges.gitter.im/Netflix/bless.svg)](https://gitter.im/Netflix/bless?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge) [![NetflixOSS Lifecycle](https://img.shields.io/osslifecycle/Netflix/bless.svg)]()

BLESS is an SSH Certificate Authority that runs as an AWS Lambda function and is used to sign SSH
public keys.

SSH Certificates are an excellent way to authorize users to access a particular SSH host,
as they can be restricted for a single use case, and can be short lived.  Instead of managing the
authorized_keys of a host, or controlling who has access to SSH Private Keys, hosts just
need to be configured to trust an SSH CA.

BLESS should be run as an AWS Lambda in an isolated AWS account.  Because BLESS needs access to a
private key which is trusted by your hosts, an isolated AWS account helps restrict who can access
that private key, or modify the BLESS code you are running.

AWS Lambda functions can use an AWS IAM Policy to limit which IAM Roles can invoke the Lambda
Function.  If properly configured, you can restrict which IAM Roles can request SSH Certificates.
For example, your SSH Bastion (aka SSH Jump Host) can run with the only IAM Role with access to
invoke a BLESS Lambda Function configured with the SSH CA key trusted by the instances accessible
to that SSH Bastion.
## Prerequistes 
A configured AWS CLI, Python 3.6, Docker and SSH access to Github.

Deployment bash scripts are for Mac and Linux.

For Windows users, option to run on an AWS Linux EC2 instance or use a Linux subsystem.

## Getting Started
These instructions are to get BLESS up and running in your local development environment.

### Installation Instructions
Clone the repo:

    $ git clone git@github.com:Practical-Code/bless.git

Cd to the bless repo:

    $ cd bless
    
## BLESS Deployment     
Run script to deploy BLESS:

    $ bash ./main_script_deploy


## Create Environment and Test BLESS
Change variable for AWS_REGION at the tops of the ec2_deploy script if not in region us-east-1.

Run script to create environment and create client:

    $ bash ./ec2_deploy


## Project resources
- Source code <https://github.com/netflix/bless>
