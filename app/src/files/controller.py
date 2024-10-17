import pathlib

from fastapi import Depends, APIRouter, UploadFile

from .service import UploadFileService
from .dto import FileDTO
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
    service = UploadFileService(db=session)
    extension = file.filename.split('.')[-1]
    file = service.execute(file=file.file, extension=extension)
    return file
