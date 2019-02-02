from botocore.exceptions import ClientError
import boto3
import sys
import json


POLICYNAME = "bless_iam_policy"
ROLENAME = "bless_iam_role"
KEY_ID = 'arn:aws:kms:us-east-1:497773990203:key/832a4bd4-d7a8-47a2-a4bb-e3a858871abb'

# Create a policy
BLESSPOLICY = \
    { "Version": "2012-10-17", "Statement": [ { "Action": [ "kms:GenerateRandom", "logs:CreateLogGroup", "logs:CreateLogStream", "logs:PutLogEvents" ], "Effect": "Allow", "Resource": "*" }, { "Sid": "AllowKMSDecryption", "Effect": "Allow", "Action": [ "kms:Decrypt", "kms:DescribeKey" ], "Resource": [ KEY_ID ] } ] }

# Create role
bless_role = \
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "",
      "Effect": "Allow",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}




iamclient = boto3.client('iam')


try:
  policy_res = iamclient.list_attached_role_policies( RoleName = ROLENAME )
  print('policy_res', policy_res)
  ROLE_ARN = iamclient.get_role( RoleName = ROLENAME)
except ClientError as e:
  if e.response['Error']['Code'] == 'NoSuchEntity':
      print("Policy not found, creating new policy, role and attachment")
      POLICY_ARN = iamclient.create_policy(PolicyName = POLICYNAME,
          PolicyDocument=json.dumps(BLESSPOLICY)
      )
      ROLE_ARN = iamclient.create_role(
          RoleName= ROLENAME,
          AssumeRolePolicyDocument=json.dumps(bless_role),
      )
      print('ROLE_ARN', ROLE_ARN) 
      print('POLICY_ARN', POLICY_ARN) 
      iamclient.attach_role_policy(
          PolicyArn= POLICY_ARN['Policy']['Arn'],
          RoleName= ROLE_ARN['Role']['RoleName']
      )
  else:
      print("Unexpected error: %s" % e)

print(ROLE_ARN)
ROLE_ID = ROLE_ARN['Role']['Arn']

lambdaclient = boto3.client('lambda')

# Create Lambda Function 
lambda_res = lambdaclient.create_function(
    FunctionName='bless_lambda',
    Runtime='python3.7',
    Role=ROLE_ID,
    Handler='bless_lambda.lambda_handler',
    Code={'ZipFile': open('./publish/bless_lambda.zip', 'rb').read()},
    Timeout=10
)

print('lambda arn', lambda_res)

