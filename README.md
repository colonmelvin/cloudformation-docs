# AWS CloudFormation Markdown Generator

This Python script generates documentation for AWS CloudFormation templates in Markdown format. It reads a CloudFormation YAML template file and outputs a table with parameters, outputs, and resources, including hyperlinks to AWS documentation for each resource.

## Requirements

- Python 3.6 or higher

## Usage

Run the script with the following command:

```sh
python cfn_docs.py my_template.yaml
```

Output to a file:

```sh
python cfn_docs.py my_template.yaml > my_template.md
```

# Example Table

## AWS CloudFormation Documentation

## Parameters

| Name | Description | Type | Default |
|------|-------------|------|---------|
| CreateDirectoryConsoleDelegatedAccessRoles | Create sample IAM ROLES that can be used to delegate users/groups access to certain areas of the AWS Management Console. User/Group assignment to these IAM roles has to be done manually via Directory Services -> Directory -> Application Management Tab. | String | No |
| CreateDirectoryAlias | Create an alias for the directory. The alias is used to construct the access URL for the directory, such as http://<alias>.awsapps.com. NOTE, after an alias has been created, it cannot be deleted or reused. Hence if a different alias already exists, then you must use the existing alias (also shown in CloudFormation error). | String | No |
| DirectoryAlias | (Optional) Specifies an alias to be assigned to the directory, such as http://<alias>.awsapps.com. Note, after alias is created it cannot be deleted or reused. Note, will only be set, if `CreateDirectoryAlias` parameter, has a value of `Yes`. | String |  |
| DirectoryID | Directory ID that will have settings updated | String |  |
| DirectoryMonitoringEmail | Email for SNS Topic to monitor directory changes. | String |  |
| DirectoryMonitoringSNSTopicKMSKey | (Optional) KMS Key ID to use for encrypting the directory monitoring SNS topic messages. If empty, encryption is enabled with SNS managing the server-side encryption keys. | String |  |
| EnableDirectorySSO | Enable single sign-on for a directory. Single sign-on allows users in your directory to access certain AWS services from a computer joined to the directory without having to enter their credentials separately. If true, "DirectoryAlias" must also be true, & "DirectoryAlias" parameter input required. | String | No |
| LambdaFunctionName | Lambda Function Name for Custom Resource | String | CR-DirectorySettings |
| LambdaLogLevel | Lambda logging level | String | INFO |
| LambdaLogsLogGroupRetention | Specifies the number of days you want to retain Lambda log events in the CloudWatch Logs | String | 14 |
| LambdaLogsCloudWatchKMSKey | (Optional) KMS Key ARN to use for encrypting the Lambda logs data. If empty, encryption is enabled with CloudWatch Logs managing the server-side encryption keys. | String |  |
| LambdaS3BucketName | Lambda S3 bucket name for the Lambda deployment package. Lambda bucket name can include numbers, lowercase letters, uppercase letters, and hyphens (-). It cannot start or end with a hyphen (-). | String |  |
| LambdaZipFileName | Amazon S3 key of the deployment package. | String | directory_settings_custom_resource.zip |

## Outputs

| Name | Description |
|------|-------------|
| DirectoryAliasUrl | Directory Alias |

## Resources

| Name | Type |
|------|------|
| [DirectoryConsoleDelegatedAccessEC2ReadOnlyRole](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html) | AWS::IAM::Role |
| [DirectoryConsoleDelegatedAccessSecurityAuditRole](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html) | AWS::IAM::Role |
| [DirectoryMonitoringTopic](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topic.html) | AWS::SNS::Topic |
| [DirectorySettingsLambdaFunction](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html) | AWS::Lambda::Function |
| [DirectorySettingsLambdaLogsLogGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loggroup.html) | AWS::Logs::LogGroup |
| [DirectorySettingsLambdaRole](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html) | AWS::IAM::Role |
| [DirectorySettingsResource](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-custom-directorysettingsresource.html) | Custom::DirectorySettingsResource |
