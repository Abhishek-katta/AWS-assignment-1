import boto3

s3 = boto3.client('s3')
s3.download_file('your bucket name', 'your object name', 'the object path', ExtraArgs={'VersionId': the 2nd version id})
