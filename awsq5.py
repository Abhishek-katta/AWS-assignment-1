import boto3
import json

def lambda_handler(event, context):
    src_bucket_name ='frombucket01'  #enter the name of the source bucket
    src_object_name = 'New text document.txt' #enter the name of the source object u wish to move
    dest_object_name = None
    dest_bucket_name = 'tobucket01' #enter the name of the detination bucket
    copy_source = {'Bucket': src_bucket_name, 'Key': src_object_name}
    if dest_object_name is None:
        dest_object_name = src_object_name

    # Copy the object
    s3 = boto3.client('s3')

    s3.copy_object(CopySource=copy_source, Bucket=dest_bucket_name, Key=dest_object_name)

    return True
