import pathlib

from fastapi import Depends, APIRouter, UploadFile

from .aws import Boto3AWSClient
from .service import UploadFileService
from .dto import FileDTO
from .. import config
from ..database import get_session, Session

router = APIRouter(prefix="/files")

# TODO add alembic and configure logging


@router.post(
    path="/upload",
    response_model=FileDTO
)
def upload_file_controller(
        file: UploadFile,
        session: Session = Depends(get_session)
):
    aws_client = Boto3AWSClient(
        aws_access_key=config.AWS_ACCESS_KEY,
        aws_secret_key=config.AWS_SECRET_KEY,
        region=config.AWS_DEFAULT_REGION
    )
    service = UploadFileService(db=session, aws_client=aws_client)
    extension = file.filename.split('.')[-1]
    file = service.execute(file=file.file, extension=extension)
    return file
