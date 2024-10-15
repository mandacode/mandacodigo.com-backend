from sqlalchemy import Table, Column, Integer, String, Enum

from ..database import metadata, mapper_registry
from . import model

users = Table(
    "users",
    metadata,
    Column("id", Integer, autoincrement=True, primary_key=True),
    Column("username", String(50), unique=True, index=True),
    Column("password", String(80)),
    Column("role", Enum(model.UserRole))
)


def start_mappers():
    mapper_registry.map_imperatively(model.User, users)
