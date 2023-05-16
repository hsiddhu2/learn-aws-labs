# Welcome to S3 CLI Practice. 

## Lab 1: # S3 Access Control

1. Create S3 Bucket with name `dva-test-bucket` in region us-east-1

- `aws s3api create-bucket --bucket dva-test-bucket --region us-east-1` 

**Output**:
```
{
    "Location": "/dva-test-bucket"
}
```

2. Create a new "**IAM User**" name `**dva-test-user**" generate the access keys 

`aws iam create-user --user-name dva-test-user`

**Output**: 
```json
{
    "User": {
        "Path": "/",
        "UserName": "dva-test-user",
        "UserId": "AIDARDBOYPBP",
        "Arn": "arn:aws:iam::ACCOUNT-ID:user/dva-test-user",
        "CreateDate": "2023-05-16T01:54:42+00:00"
    }
}
```

`aws iam create-access-key --user-name dva-test-user`

**Output**: 
```json
{
    "AccessKey": {
        "UserName": "dva-test-user",
        "AccessKeyId": "AKIARDBOYP",
        "Status": "Active",
        "SecretAccessKey":"yxgs7UVUeI5VV1eAbUT",
        "CreateDate": "2023-05-16T01:56:40+00:00"
    }
}
```

3. Use 'aws-configure' to create a profile for the bootcamp test user. (for example - --profile dva-test-user) and use the access keys generated earlier. 


4. Use CloudShell and Nano to create an IAM policy for restriceted access name iam_policy.json. Run `sudo yum install nano` if nano is not installed on CloudShell. 

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::dva-test-bucket"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:DeleteObject"
      ],
      "Resource": [
        "arn:aws:s3:::dva-test-bucket/*"
      ]
    }
  ]
}
```

5. Attach the IAM policy to the dva=test-user


```code
aws iam put-user-policy --user-name dva-test-user --policy-name GetDeleteS3ObjectUserPolicy --policy-document iam_policy.json

aws iam list-user-policies --user-name dva-test-user

```
**Output**:
```json
{
    "PolicyNames": [
        "GetDeleteS3ObjectUserPolicy"
    ]
}
```

6. Create a bucket policy that allows the PutObject API action named bucket_policy.json

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::ACCOUNT_ID:user/dva-test-user"
      },
      "Action": [
        "s3:PutObject"
      ],
      "Resource": [
        "arn:aws:s3:::dva-test-bucket",
        "arn:aws:s3:::dva-test-bucket/*"
      ]
    }
  ]
}
```

7. Upload, download and delete objects using dva-test-profile. Since bucket policy is still not attached to the user, you should see <span style="color:red"> an error occurred (AccessDenied) when calling the PutObject operation: Access Denied

```
aws s3api put-object --bucket dva-test-bucket --key item1.json --profile dva-test-user 

```

8. Attach the bucket policy that we have created above to dva-test-user using below command. 

```
aws s3api put-bucket-policy --bucket dva-test-bucket --policy file://bucket_policy.json

```

9. Verify Bucket Policy Added Correctly

```
aws s3api get-bucket-policy --bucket dva-test-bucket

```
**Output:**

```json
{
    "Policy": "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Principal\":{\"AWS\":\"arn:aws:iam::ACCOUNT-ID:user/dva-test-user\"},\"Action\":\"s3:PutObject\",\"Resource\":[\"arn:aws:s3:::dva-test-bucket\",\"arn:aws:s3:::dva-test-bucket/*\"]}]}"
}
```

10. Upload the object again

```
aws s3api put-object --bucket dva-test-bucket --key item1.json --profile dva-test-user
```
**Output:**
```json

{
    "ETag": "\"d41d8cd98f00b204e9800998ecf8427e\"",
    "ServerSideEncryption": "AES256"
}
```

