from fastapi import APIRouter, Depends, HTTPException
from fastapi import status

from .dto import (
    CreateCourseDTO,
    CourseDTO,
    CreateModuleDTO,
    CreateLessonDTO,
    LessonDTO
)
from .service import (
    CreateCourseService,
    CreateModuleService,
    CreateLessonService,
    GetCourseService,
    GetLessonService
)
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
    # use course_id for validation if module belongs to the course
    service = CreateLessonService(db=session)
    lesson = service.execute(
        title=dto.title,
        description=dto.description,
        module_id=module_id,
        video_id=dto.video_id
    )
    return lesson


@router.get(
    path="/{course_id}",
    response_model=CourseDTO
)
def get_course_controller(
        course_id: int,
        session: Session = Depends(get_session)
):
    service = GetCourseService(db=session)
    course = service.execute(course_id=course_id)
    if course is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return course


@router.get(
    path="/{course_id}/modules/{module_id}/lessons/{lesson_id}",
    response_model=LessonDTO
)
def get_lesson_controller(
        course_id: int,
        module_id: int,
        lesson_id: int,
        session: Session = Depends(get_session)
):
    service = GetLessonService(db=session)
    lesson = service.execute(lesson_id=lesson_id)
    if lesson is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return lesson


# TODO add enrollment
# TODO add user profile
# TODO add security
# TODO add ability to delete file, lesson, module, course (delete course removes all modules, lessons etc)

