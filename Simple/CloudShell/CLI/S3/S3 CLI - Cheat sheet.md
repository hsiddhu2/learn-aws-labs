# AWS S3 CLI - Cheat Sheet

This cheat sheet provides a list of AWS CLI commands for Amazon S3, a highly-scalable object storage service offered by Amazon Web Services (AWS). If you're new to S3, we recommend going through the free AWS S3 crash course. To learn how to install AWS CLI, follow the steps on this [post](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html).

## Get Help

To get help with the AWS S3 CLI, use the following commands:

```bash
aws s3 help
```

or

```bash
aws s3api help
```

## Create a Bucket

To create an S3 bucket, use the following command:

```bash
aws s3 mb s3://bucket-name 
```

## Remove a Bucket

To remove an empty S3 bucket, use the following command:

```bash
aws s3 rb s3://bucket-name
```

**Note:** Be extremely careful while running this command as it will remove all contents in the bucket including subfolders and data in them.

To remove a non-empty bucket, use the `--force` option as shown below:

```bash
aws s3 rb s3://bucket-name --force
```

## Copy Objects

To copy an object to an S3 bucket, use the following command:

```bash
aws s3 cp mypic.png s3://mybucket/
```

## Copy Buckets

To copy a folder and its contents recursively to an S3 bucket, use the following command:

```bash
aws s3 cp myfolder s3://mybucket/myfolder --recursive
```

## Sync Buckets

To synchronize the contents of two S3 buckets, use the following command:

```bash
aws s3 sync <source> <target> [--options]
```

## List Buckets

To list all the S3 buckets in your account, use the following command:

```bash
aws s3 ls
```

## List Specific Bucket

To list the contents of a specific S3 bucket, use the following command:

```bash
aws s3 ls s3://mybucket
```

## Bucket Location

To get the location of an S3 bucket, use the following command:

```bash
aws s3api get-bucket-location --bucket <bucket-name>
```

## Logging Status

To get the logging status of an S3 bucket, use the following command:

```bash
aws s3api get-bucket-logging --bucket <bucket-name>
```

## ACL (Access Control List)

To set permissions on an S3 object, use the following command:

```bash
aws s3 cp file.txt s3://my-bucket/ --grants read=uri=http://acs.amazonaws.com/groups/global/AllUsers full=emailaddress=user@example.com
```

This example grants read permissions on the object to everyone and full permissions (read, readacl, and writeacl) to the account associated with `user@example.com`.

## Conclusion

This cheat sheet provides some of the most commonly used AWS S3 CLI commands. However, there are many other options and parameters available. For more information, refer to the [AWS S3 CLI documentation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/index.html).