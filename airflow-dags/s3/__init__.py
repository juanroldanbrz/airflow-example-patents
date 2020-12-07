import logging
import os

import boto3
from botocore.exceptions import NoCredentialsError

ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
SECRET_KEY = os.getenv('AWS_SECRET_KEY')
AWS_BUCKET_NAME = os.getenv('AWS_BUCKET_NAME')
AWS_BUCKET_REGION = os.getenv('AWS_S3_REGION')

s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                  aws_secret_access_key=SECRET_KEY, region_name=AWS_BUCKET_REGION)


def upload_to_aws(local_file, s3_file):
    """
    Uploads a file into a S3 bucket.
    :param local_file: local file to upload to S3.
    :param s3_file: file path in the s3 bucket.
    :return: True if upload was successful.
    """

    logging.info("Uploading file " + s3_file)
    try:
        s3.upload_file(local_file, AWS_BUCKET_NAME, s3_file)
        logging.info(s3_file + " uploaded successfully")
        return True
    except FileNotFoundError:
        logging.error(s3_file + " file was not found")
        return False
    except NoCredentialsError:
        logging.error("Credentials not available")
        return False
