import boto3

iam_client = boto3.client('iam')
lambda_client = boto3.client('lambda')

with open('project.zip', 'rb') as f:
	zipped_code = f.read()
  
role = iam_client.get_role(RoleName='LambdaBasicExecution')

response = lambda_client.create_function(
    FunctionName='SEOO',
    Runtime='python3.9',
    Role=role['Role']['Arn'],
    Handler='handler.lambda_handler',
    Code=dict(ZipFile=zipped_code),
    Timeout=300, # Maximum allowable timeout
    # Set up Lambda function environment variables
    Environment={
        'Variables': {
            'Name': 'SEOO',
            'Environment': 'prod'
        }
    },
)