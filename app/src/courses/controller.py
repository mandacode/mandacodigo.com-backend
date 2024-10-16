from fastapi import APIRouter, Depends
from fastapi import status

from .dto import CreateCourseDTO, CourseDTO, CreateModuleDTO, CreateLessonDTO
from .service import CreateCourseService, CreateModuleService, \
    CreateLessonService
from ..database import get_session, Session

router = APIRouter(prefix="/courses")


@router.post(
    path="/",
    response_model=CourseDTO,
    status_code=status.HTTP_201_CREATED
)
def create_course_controller(
        dto: CreateCourseDTO,
        session: Session = Depends(get_session)
):
    # TODO check competition how it works there
    service = CreateCourseService(db=session)
    course = service.execute(
        title=dto.title,
        description=dto.description,
        teacher_id=dto.teacher_id,
        price=dto.price
    )
    return course


@router.post(
    path="/{course_id}/modules",
)
def create_module_controller(
        course_id: int,
        dto: CreateModuleDTO,
        session: Session = Depends(get_session)
):
    # module can be added only by teacher who created course or by head admin
    service = CreateModuleService(db=session)
    module = service.execute(
        title=dto.title,
        course_id=course_id
    )
    return module


@router.post(
    path="/{course_id}/modules/{module_id}/lessons",
)
def create_lesson_controller(
        course_id: int,
        module_id: int,
        dto: CreateLessonDTO,
        session: Session = Depends(get_session)
):
    # use course_id for validation if module belongs to the course'
    service = CreateLessonService(db=session)
    lesson = service.execute(
        title=dto.title,
        description=dto.description,
        module_id=module_id,
        video_id=dto.video_id
    )
    return lesson


# TODO Uploading files to S3 or just videos
# Add introduction