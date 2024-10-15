import fastapi

from . import dto
from ..database import get_session

router = fastapi.APIRouter(prefix="/courses")


@router.post("/")
def create_course_controller(
        dto: dto.CreateCourseDTO,
        session=fastapi.Depends(get_session)
):
    pass
