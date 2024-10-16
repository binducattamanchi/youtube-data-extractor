import json
import boto3
import logging

logger = logging.getLogger(__name__)

def create_s3_client(endpoint_url):
    return boto3.client('s3', endpoint_url=endpoint_url)

def ensure_bucket_exists(s3_client, bucket_name):
    try:
        s3_client.create_bucket(Bucket=bucket_name)
        logger.info(f"Created S3 bucket: {bucket_name}")
    except s3_client.exceptions.BucketAlreadyExists:
        logger.info(f"S3 bucket already exists: {bucket_name}")

def upload_to_s3(s3_client, data, bucket, object_name):
    try:
        s3_client.put_object(Bucket=bucket, Key=object_name, Body=json.dumps(data))
        logger.info(f"Uploaded data to S3 bucket {bucket}/{object_name}")
    except Exception as e:
        logger.error(f"Error uploading data to S3: {e}")