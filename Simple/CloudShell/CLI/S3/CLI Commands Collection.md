**List IAM Users in Account**
- `aws iam list-users`
  
**Create S3 Bucket**
- `aws s3api create-bucket --bucket uniquebucketname --region us-east-1`


**Put objects in Bucket**
- `aws s3api put-object --bucket uniquebucketname --key scripts/script.sh`
- `aws s3api put-object --bucket uniquebucketname --key scripts/pythonscript.py`
- `aws s3api put-object --bucket uniquebucketname --key scripts/script.py`


**List object**
- `aws s3api list-objects --bucket uniquebucketname`
  

**List object V2 From Bucket**
- `aws s3api list-objects-v2 --bucket uniquebucketname`

**Get Object From Bucket**
- `aws s3api get-object --bucket uniquebucketname --key script/script.py scriptcopy.py`

**Delete Object From Bucket**
- `aws s3api delete-object --bucket uniquebucketname --key scripts/script.py`


**Delete Bucket**
- `aws s3api delete-bucket --bucket uniquebucketname --region us-east-1`

