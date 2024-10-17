from typing import Protocol, BinaryIO

import boto3


class AWSClient(Protocol):

    def upload(self, file: BinaryIO, bucket: str, s3_key: str) -> str:
        ...


class Boto3AWSClient:

    def __init__(
            self,
            aws_access_key: str,
            aws_secret_key: str,
            region: str
    ):
        self._client = boto3.client(
            "s3",
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_key,
            region_name=region
        )

    def upload(self, file: BinaryIO, bucket: str, s3_key: str):
        self._client.upload_fileobj(file, bucket, s3_key)
