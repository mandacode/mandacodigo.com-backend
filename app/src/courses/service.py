from .model import enroll_course

from . import model


class CreateCourseService:

    def __init__(self, db):
        self.db = db

    def execute(
        self, title: str, description: str, teacher_id: int, price: int
    ) -> model.Course:

        course = model.Course(
            title=title,
            description=description,
            teacher_id=teacher_id,
            price=price
        )

        self.db.add(course)
        self.db.commit()

        return course


class CreateVideoService:

    def __init__(self, db):
        self.db = db

    def execute(self, url: str, duration: float):
        video = model.Video(url=url, duration=duration)

        self.db.add(video)
        self.db.commit()


class CreateLessonService:

    def __init__(self, db):
        self.db = db

    def execute(
            self, title: str, description: str, video_id: int, module_id: int
    ):
        lesson = model.Lesson(
            title=title,
            description=description,
            video_id=video_id,
            module_id=module_id
        )

        self.db.add(lesson)
        self.db.commit()


class CreateModuleService:

    def __init__(self, db):
        self.db = db

    def execute(self, title: str, course_id: int) -> model.Module:
        module = model.Module(title=title, course_id=course_id)

        self.db.add(module)
        self.db.commit()

        return module


class EnrollService:

    def __init__(self, db):
        self.db = db

    def execute(self, student_id: int, course_id: int):
        student = self.db.query(model.User).filter_by(id=student_id).one()
        course = self.db.query(model.Course).filter_by(id=course_id).one()

        enroll_course(student=student, course=course)

        self.db.commit()


# TODO business rules
# users can register and login
# only teachers can create courses, modules, lessons and upload videos
# students can enroll to courses, now for free
# students have to pay for courses so they have to add card to their profile
# meaning users have to have user profiles (profile picture, phone number, first name, last name, credit card (for payments))
# tracking course progress
# payments handled course_id | student_id | status | date |
