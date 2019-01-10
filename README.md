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

Cd to the bless repo:

    $ cd bless

## BLESS Deployment     
Run the main_script_deploy to deploy BLESS:

Create a virtualenv if you haven't already:
    $ ./main_script_deploy

    $ python3.6 -m venv venv

Activate the venv:
## Create Environment and BLESS Test
Change variable for AWS_REGION in ec2_deploy script

    $ source venv/bin/activate
Run the ec2_deploy script to create environment and create client

Install package and test dependencies:
    $ ./ec2_deploy

## Project resources
- Source code <https://github.com/netflix/bless>
- Issue tracker <https://github.com/netflix/bless/issues>
