import boto3
import json
import base64
from botocore.exceptions import ClientError

def get_db_credentials(secret_name="db-creds", region_name="ap-south-1"):
    session = boto3.session.Session()
    client = session.client(service_name='secretsmanager', region_name=region_name)

    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
        secret = get_secret_value_response['SecretString']
        return json.loads(secret)
    except ClientError as e:
        raise Exception("Error fetching secret: " + str(e))
