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

10. Make the object public using an object-level ACL

---
# Questions 

1. Which settings must be changed?
    - Need to enable bucket ACLs in the bucket ownership under permission tab. 
    - Uncheck the "block public access' setting in permission tab.
    - Open bucket and select the object and go to actions and click on "make public" 



2. Does the bucket policy need updating?
    - No, after enabling bucket ACLs bucket policy will not in effect and objects will be publicly accessible. 

4. After getting it working, what happens if you enable "block public access"?
    - The objects will become private again and will not be available publicly. 

---

# Lab 2 - MFA with Amazon S3

## 1. Enable versioning

aws s3api put-bucket-versioning --bucket bootcamp-s3-exercises --versioning-configuration Status=Enabled

## 2. Configure Access Keys 
Login as root and create access keys. Ensure you have an MFA device setup for root and make note of the ARN. Configure the access keys on the AWS CLI (not CloudShell)

## 3. Enable MFA delete
From the CLI, not from CloudShell (update the ARN and replace TOKEN_CODE with a valid code)

```
aws s3api put-bucket-versioning --bucket my-bucket --versioning-configuration Status=Enabled,MFADelete=Enabled --mfa "arn:aws:iam::<account-id>:mfa/root-account-mfa-device <TOKEN_CODE>"
```

## 4. Upload and and then attempt to delete an object

```
echo "Test MFA Delete" > test.txt
aws s3 cp test.txt s3://bootcamp-s3-exercises/test.txt

```
```
aws s3 rm s3://bootcamp-s3-exercises/test.txt
aws s3api delete-object --bucket bootcamp-s3-exercises --key test.txt --version-id <version-id-of-deleted-object>
```
## 5. Delete the object with MFA

```
aws s3api delete-object --bucket bootcamp-s3-exercises --key test.txt --version-id <version-id-of-deleted-object> --mfa "arn:aws:iam::ACCOUNT_ID:mfa/root-account-mfa-device TOKEN_CODE"
```

---

# Lab 3 -  MFA-Protected API Access

## 1. Create a bucket

```
aws s3api create-bucket --bucket bootcamp-s3-mfa-test --region us-east-1
```

## 2. Update bucket policy 
With the test use ARN and bucket ARNs and save as `mfa_bucket_policy.json`

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Deny",
            "Principal": {
                "AWS": "arn:aws:iam::ACCOUNT-ID:user/dva-test-user"
            },
            "Action": [
                "s3:ListBucket",
                "s3:PutObject",
                "s3:GetObject",
                "s3:DeleteObject"
            ],
            "Resource": [
                "arn:aws:s3:::dva-s3-mfa-test",
                "arn:aws:s3:::dva-s3-mfa-test/*"
            ],
            "Condition": {
                "Null": {
                    "aws:MultiFactorAuthAge": "true"
                }
            }
        }
    ]
}
```

## 3. Apply the bucket policy

```
aws s3api put-bucket-policy --bucket bootcamp-s3-mfa-test --policy file://mfa_bucket_policy.json
```

## 4. Attempt to upload 
Upload a file from the AWS CLI (not CloudShell) using the same account specified in the principal element (should fail)

## 5. Get temporary session credentials with MFA

```
aws sts get-session-token --serial-number arn:aws:iam::ACCOUNT_ID:mfa/DEVICE_NAME --token-code <token>
```
## 6. Then create the environment variables

```
export AWS_ACCESS_KEY_ID=TEMP_ACCESS_KEY_ID
export AWS_SECRET_ACCESS_KEY=TEMP_SECRET_ACCESS_KEY
export AWS_SESSION_TOKEN=TEMP_SESSION_TOKEN
```
## 7. Attempt to upload
Upload a file from the AWS CLI again, without specifying your profile (should work)

---

# Lab 4 - Enforce Encryption with AWS KMS

## 1. Update the bucket policy json file to enforce encryption with AWS KMS

```json
{
    "Version": "2012-10-17",
    "Id": "PutObjectPolicy",
    "Statement": [
        {
            "Sid": "DenyUnEncryptedObjectUploads",
            "Effect": "Deny",
            "Principal": "*",
            "Action": "s3:PutObject",
            "Resource": "arn:aws:s3:::dva-s3-mfa-test/*",
            "Condition": {
                "StringNotEquals": {
                    "s3:x-amz-server-side-encryption": "aws:kms"
                }
            }
        }
    ]
}
```

## 2. Update the bucket policy

```
aws s3api put-bucket-policy --bucket bootcamp-s3-mfa-test --policy file://mfa_bucket_policy.json
```
## 3. Test uploading 
Upload a file with default encryption settings (should fail)

## 4. Specify SSE using aws-kms
Try again specifying server-side encryption with AWS KMS (should work)

