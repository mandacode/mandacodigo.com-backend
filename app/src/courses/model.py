import dataclasses

from ..users.model import User


@dataclasses.dataclass
class Lesson:
    title: str
    description: str
    video_id: int
    module_id: int


@dataclasses.dataclass
class Module:
    title: str
    course_id: int


@dataclasses.dataclass
class Course:
    title: str
    description: str
    teacher_id: int
    price: int  # in cents

    def __post_init__(self):
        self.students: list[User] = []


def enroll_course(student: User, course: Course):
    course.students.append(student)
