import dataclasses
import enum


class UserRole(enum.Enum):
    STUDENT = "student"
    TEACHER = "teacher"
    ADMIN = "admin"


@dataclasses.dataclass
class User:
    username: str
    password: str
    role: UserRole
