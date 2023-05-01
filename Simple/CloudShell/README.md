**List IAM Users in Account**
- `aws iam list-users`
  
![alt text]([http://url/to/img.png](https://github.com/hsiddhu2/learn-aws-labs/blob/main/Simple/CloudShell/images/image1.jpeg)

**Create S3 Bucket**
- `aws s3api create-bucket --bucket hpcloudlabs --region us-east-1`

![picture 2](../../../images/bc3ca131738f551b6df4b2d06c7babda6fd447182f694008c707ae7d3bdcdd92.png)  


**Put objects in Bucket**
- `aws s3api put-object --bucket hpcloudlabs --key scripts/script.sh`
- `aws s3api put-object --bucket hpcloudlabs --key scripts/pythonscript.py`
- `aws s3api put-object --bucket hpcloudlabs --key scripts/script.py`

![picture 3](../../../images/44a449b7e85f725554ab08d168d645e71942926cf434e27bab61d29e1e11fc7d.png)  

**List object**
- `aws s3api list-objects --bucket hpcloudlabs`
  
![picture 4](../../../images/8bce75550a04badf687e62540acdc04b96e6bc96a1da53e83fdc7ddaf9f3bc7a.png)  


**List object V2 From Bucket**
- `aws s3api list-objects-v2 --bucket hpcloudlabs`

![picture 5](../../../images/4a09f26d7d54d3eb29bcc0e8eb954e4e1689a5ee6443546f46aff23e63a7e06f.png)  


**Get Object From Bucket**
- `aws s3api get-object --bucket hpcloudlabs --key script/script.py scriptcopy.py`

**Delete Object From Bucket**
- `aws s3api delete-object --bucket hpcloudlabs --key scripts/script.py`

![picture 6](../../../images/7900a43a54409f09ca1e386465720141129ef2546301055f6ffcc234a8ffe101.png)  


**Delete Bucket**
- `aws s3api delete-bucket --bucket hpcloudlabs --region us-east-1`

![picture 7](../../../images/678bafd7ee6fb2238b361c2d68d599898db7d137daa4a73ca2fa0bc33ede2731.png)  
