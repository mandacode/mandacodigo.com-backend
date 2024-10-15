import pydantic


class CreateCourseDTO(pydantic.BaseModel):
    title: str
    description: str
    teacher_id: int
    price: int


class CourseDTO(pydantic.BaseModel):
    id: int
    title: str
    teacher_id: int
    price: int
