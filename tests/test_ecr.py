import os

import boto3
from botocore.exceptions import EndpointConnectionError

os.environ["AWS_ACCESS_KEY_ID"] = 'testing'
os.environ["AWS_SECRET_ACCESS_KEY"] = 'testing'
os.environ["AWS_DEFAULT_REGION"] = 'us-east-1'


def test_create_repository():
    # given
    client = boto3.client("ecr", endpoint_url="http://localhost:5000")

    try:
        client.create_repository(repositoryName="myrepo")
    except EndpointConnectionError as e:
        # Expected, as nothing is running on localhost
        pass

