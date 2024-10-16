from fastapi import Depends, APIRouter, UploadFile

from ..database import get_session, Session

router = APIRouter(prefix="/files")

# TODO add alembic and s3


@router.post(
    path="/"
)
def upload_file_controller(
        file: UploadFile,
        session: Session = Depends(get_session)
):
    print(file)
