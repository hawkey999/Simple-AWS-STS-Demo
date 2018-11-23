import boto3
sts = boto3.client('sts',endpoint_url="https://sts.cn-northwest-1.amazonaws.com.cn")

assumed_role_object = sts.assume_role(
    RoleArn="arn:aws-cn:iam::<your account>:role/s3fullaccess_self_account",
    RoleSessionName="AssumeRoleSession000001"
)

des_aws_access_key_id = assumed_role_object['Credentials']['AccessKeyId']
des_aws_secret_access_key = assumed_role_object['Credentials']['SecretAccessKey']
aws_session_token = assumed_role_object['Credentials']['SessionToken']
s3client = boto3.client(
    's3',
    aws_access_key_id=des_aws_access_key_id,
    aws_secret_access_key=des_aws_secret_access_key,
    aws_session_token=aws_session_token,
    region_name='cn-north-1')

response = s3client.list_buckets()
print(response)
