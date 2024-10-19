import pydantic


class LightLessonDTO(pydantic.BaseModel):
    id: int
    title: str


class LessonDTO(pydantic.BaseModel):
    id: int
    title: str
    description: str

    video_url: str


class ModuleDTO(pydantic.BaseModel):
    id: int
    title: str

    lessons: list[LightLessonDTO]


class CreateCourseDTO(pydantic.BaseModel):
    title: str
    description: str
    teacher_id: int
    price: int


class CourseDTO(pydantic.BaseModel):
    id: int
    title: str
    description: str
    teacher_id: int
    price: int

    modules: list[ModuleDTO]


class CreateModuleDTO(pydantic.BaseModel):
    title: str


class CreateLessonDTO(pydantic.BaseModel):
    title: str
    description: str
    video_id: int
