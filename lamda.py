import boto3
import json

iam = boto3.client('iam')

role_policy = {
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


response = iam.create_role(
  RoleName='LambdaBasicExecution',
  AssumeRolePolicyDocument=json.dumps(role_policy),
)

print(response)
