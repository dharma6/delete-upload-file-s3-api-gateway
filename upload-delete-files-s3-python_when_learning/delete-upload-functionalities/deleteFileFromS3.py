import boto3
from botocore.exceptions import NoCredentialsError
import config

ACCESS_KEY = config.credentials['access_key']
SECRET_KEY = config.credentials['secret_key']

def delete_from_s3(bucket, s3_file):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,aws_secret_access_key=SECRET_KEY)

    try:
        s3.delete_object(Bucket=bucket,Key=s3_file)
        print("Delete Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False
    



uploaded = delete_from_s3(config.credentials['s3bucket'], config.credentials['dest-file-name'])
