Sure, here's a cheatsheet for AWS IAM CLI commands:

# AWS IAM CLI Cheatsheet

AWS Identity and Access Management (IAM) is a web service that allows you to manage users and user permissions in AWS. You can also manage permissions for AWS resources and integrate IAM with other AWS services. 

The AWS CLI provides a set of commands for interacting with IAM. Here are some of the most commonly used IAM CLI commands:

## 1. Create User

```bash
aws iam create-user --user-name <user-name>
```

## 2. List Users

```bash
aws iam list-users
```

## 3. Add User to Group

```bash
aws iam add-user-to-group --user-name <user-name> --group-name <group-name>
```

## 4. Remove User from Group

```bash
aws iam remove-user-from-group --user-name <user-name> --group-name <group-name>
```

## 5. Create Group

```bash
aws iam create-group --group-name <group-name>
```

## 6. List Groups

```bash
aws iam list-groups
```

## 7. Attach Policy to Group

```bash
aws iam attach-group-policy --policy-arn <policy-arn> --group-name <group-name>
```

## 8. Detach Policy from Group

```bash
aws iam detach-group-policy --policy-arn <policy-arn> --group-name <group-name>
```

## 9. Create Policy

```bash
aws iam create-policy --policy-name <policy-name> --policy-document file://<policy-document.json>
```

## 10. List Policies

```bash
aws iam list-policies
```

## 11. Delete Policy

```bash
aws iam delete-policy --policy-arn <policy-arn>
```

## 12. Get User Policy

```bash
aws iam get-user-policy --user-name <user-name> --policy-name <policy-name>
```

## 13. Put User Policy

```bash
aws iam put-user-policy --user-name <user-name> --policy-name <policy-name> --policy-document file://<policy-document.json>
```

## 14. Delete User Policy

```bash
aws iam delete-user-policy --user-name <user-name> --policy-name <policy-name>
```

## 15. Get Group Policy

```bash
aws iam get-group-policy --group-name <group-name> --policy-name <policy-name>
```

## 16. Put Group Policy

```bash
aws iam put-group-policy --group-name <group-name> --policy-name <policy-name> --policy-document file://<policy-document.json>
```

## 17. Delete Group Policy

```bash
aws iam delete-group-policy --group-name <group-name> --policy-name <policy-name>
```

These are some of the most commonly used IAM CLI commands. For more information on IAM CLI commands, check out the [AWS CLI IAM documentation](https://docs.aws.amazon.com/cli/latest/reference/iam/index.html).