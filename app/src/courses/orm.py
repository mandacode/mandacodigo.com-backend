from sqlalchemy import (
    Table,
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime,
    func
)
from sqlalchemy.orm import relationship

from . import model
from ..database import metadata, mapper_registry
from ..files.model import File

lessons = Table(
    "lessons",
    metadata,
    Column("id", Integer, autoincrement=True, primary_key=True),
    Column("title", String(120)),
    Column("description", String(500)),
    Column("video_id", Integer, ForeignKey("files.id")),
    Column("module_id", Integer, ForeignKey("modules.id")),
)

modules = Table(
    "modules",
    metadata,
    Column("id", Integer, autoincrement=True, primary_key=True),
    Column("title", String(120)),
    Column("course_id", Integer, ForeignKey("courses.id")),
)

courses = Table(
    "courses",
    metadata,
    Column("id", Integer, autoincrement=True, primary_key=True),
    Column("title", String(120)),
    Column("description", String(1000)),
    Column("price", Integer),
    Column("teacher_id", Integer, ForeignKey("users.id")),
)

enrollments = Table(
    "enrollments",
    metadata,
    Column("id", Integer, autoincrement=True, primary_key=True),
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("course_id", Integer, ForeignKey("courses.id")),
    Column("enrolled_at", DateTime, default=func.now()),
)


def start_mappers():
    mapper_registry.map_imperatively(
        model.Lesson, lessons, properties={
            'video': relationship(
                File, backref='lesson', uselist=False
            )
        }
    )
    mapper_registry.map_imperatively(
        model.Module, modules, properties={
            'lessons': relationship(
                model.Lesson, backref='module'
            )
        }
    )
    mapper_registry.map_imperatively(
        model.Course, courses, properties={
            'modules': relationship(
                model.Module, backref='course'
            )
        }
    )
