import datetime
import random
import string
from typing import BinaryIO

from .aws import Boto3AWSClient
from . import model
from .. import config
from ..database import DatabaseSession


def generate_unique_filename(extension: str, length: int = 16) -> str:
    letters_and_digits = string.ascii_letters + string.digits
    random_string = ''.join(random.choices(letters_and_digits, k=length))
    return f"{random_string}.{extension}"


class UploadFileService:

    def __init__(
            self,
            db: DatabaseSession,
            aws_client: Boto3AWSClient
    ):
        self.db = db
        self.aws_client = aws_client

    def execute(self, file: BinaryIO, extension: str) -> model.File:
        today = datetime.datetime.today()
        filename = generate_unique_filename(extension)

        s3_key = "{0}/{1}/{2}/{3}/{4}".format(
            config.AWS_UPLOAD_DIR,
            today.year,
            today.month,
            today.day,
            filename
        )

        self.aws_client.upload(
            file=file,
            bucket="manda-uploads",
            s3_key=s3_key
        )

        # add repository
        file = model.File(filename=filename, path=s3_key)
        self.db.add(file)
        self.db.commit()

        return file
