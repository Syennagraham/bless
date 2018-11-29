import boto3
import base64
import os


def lambda_handler(event, context):
    region = os.environ['AWS_REGION']
    client = boto3.client('kms', region_name=region)
    response = client.encrypt(
    KeyId= event,
    Plaintext= context
    )

    ciphertext = response['CiphertextBlob']
    return base64.b64encode(ciphertext)


print(lambda_handler("980e7261-e9e5-44ee-a0fd-a8a3195d3fa7","abc123"))
