# Deploy Lmmbda Using CLI and S3


1. Create a file called lambda_function.py in CLI with the following code. 

[Function Code](lambda_function.py)

2. Zip lambda_function.py 

```bash
zip lambda_function.zip lambda_function.py
```

3. Create a role for the lambda function using below json and create lambda-role-trust-policy.json

```json
{
"Version": "2012-10-17",
"Statement": [
    {
    "Effect": "Allow",
    "Principal": {
        "Service": "lambda.amazonaws.com"
    },
    "Action": "sts:AssumeRole"
    }
]
}
```
AWS CLI command to create lambda role using the assume role policy document (trust policy)
```bash
aws iam create-role --role-name hp-lambda-role --assume-role-policy-document file://lambda-role-trust-policy.json

```

4. Attach Lambda Basic Role Execution Policy to the role (aws service role policy)

```bash
aws iam attach-policy --role hp-lambda-role --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
aws iam attach-policy --role hp-lambda-role --policy-arn arn:aws:iam::ACCOUNT-NO:policy/CreateS3Bucket
aws iam attach-policy --role hp-lambda-role --policy-arn arn:aws:iam::ACCOUNT-NO:policy/GetDeleteS3Object
```
5. Create a lambda function using CLI using the below command. 

```bash
aws lambda create-function --function-name hp-lambda-function --runtime python3.8 --role arn:aws:iam::ACCOUNT_ID:role/hp-lambda-role --handler lambda_function.event_handler --zip-file fileb://lambda_function.zip
```


6. Test lambda function by running Lambda Invoke command.
    
```bash
aws lambda invoke --function-name hp-lambda-function --payload '{"message":"Hello from lambda"}] output.txt --cli-binary-format raw-in-base64-out --log-type Tail --query 'LogResult' --output text | base64 -d

```

7. Check the content of output.txt file. 

```bash
cat output.txt
```

8. Update the code in lambda_function.py and zip the file again. 

```bash
zip lambda_function.zip lambda_function.py
```

```bash
aws lambda update-function-code --function-name hp-lambda-function --zip-file fileb://lambda_function.zip



# Lab 2 - Working with Environment Variables and Secrets in AWS Lambda

1. Create a secret json file and add your secrets. (secrets.json)

```json
{
    "username": "admin",
    "password": "admin123"
}
```

2. Create a secret in AWS Secrets Manager using CLI. 

```bash
aws secretsmanager create-secret --name hp-secret --description "HP Secret" --secret-string file://secrets.json
```

3, Create a lambda function using the below code. 

```python

import os
import boto3
import json

def lambda_handler(event, context):
    secret_name = os.environ['SECRET_NAME']
    region_name = os.environ['AWS_REGION']

    session = boto3.session.Session()
    client = session.client(service_name='secretsmanager', region_name=region_name)
    response = client.get_secret_value(SecretId=secret_name)

    secret_data = json.loads(response['SecretString'])
    api_key = secret_data['username']

    # Use the API key to make a request to the hypothetical API
    # (Replace with actual API request code)
    print(f"API key: {api_key}")

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

```