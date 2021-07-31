import json
import boto3
import logging

logger = logging.getLogger(__name__)
s3 = boto3.client('s3')

def s3_read(bucket: str, key: str) -> str:
    s3_object = s3.get_object(Bucket=bucket, Key=key)
    body = s3_object['Body']
    return body.read()

def s3_write(bucket: str, key: str, body: any):
    return s3.put_object(
        Body=body,
        Bucket=bucket,
        Key=key
    )