import boto3
import json

s3Client = boto3.client('s3')
bucket_name = "aws.freecloudlabs.com"

def lambda_handler(event, context):
    print("Lambda function started")
    try:
        s3Client.head_bucket(Bucket=bucket_name)
        print("Bucket exists, writing event to bucket")
        s3Client.put_object(Bucket=bucket_name, Key="lambda-event.json", Body=json.dumps(event))
        bucket_created = False
    except:
        print("Bucket does not exist, creating bucket")
        s3Client.create_bucket(Bucket=bucket_name)
        S3Client.put(Bucket=bucket_name, Key="lambda-event.json", Body=json.dumps(event)) 
        bucket_created = True

    return {
        'statusCode': 200,
        'new_bucket_created': bucket_created,
        'body': json.dumps('Hello from Lambda!')
    }