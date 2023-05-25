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


arn:aws:iam::075260000351:policy/CreateS3Bucket
arn:aws:iam::075260000351:policy/GetDeleteS3Object
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
