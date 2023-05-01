**List IAM Users in Account**
- `aws iam list-users`
  
![Image](images/image1.jpeg)

**Create S3 Bucket**
- `aws s3api create-bucket --bucket hpcloudlabs --region us-east-1`
  
![Image](images/image2.jpeg)


**Put objects in Bucket**
- `aws s3api put-object --bucket hpcloudlabs --key scripts/script.sh`
- `aws s3api put-object --bucket hpcloudlabs --key scripts/pythonscript.py`
- `aws s3api put-object --bucket hpcloudlabs --key scripts/script.py`

![image](images/image3.jpeg) 

**List object**
- `aws s3api list-objects --bucket hpcloudlabs`
  
![image](images/image4.jpeg)  


**List object V2 From Bucket**
- `aws s3api list-objects-v2 --bucket hpcloudlabs`

![image](images/image5.jpeg)  


**Get Object From Bucket**
- `aws s3api get-object --bucket hpcloudlabs --key script/script.py scriptcopy.p`


**Delete Object From Bucket**
- `aws s3api delete-object --bucket hpcloudlabs --key scripts/script.py`

![image](images/image6.jpeg) 


**Delete Bucket**
- `aws s3api delete-bucket --bucket hpcloudlabs --region us-east-1`

![image](images/image7.jpeg)
