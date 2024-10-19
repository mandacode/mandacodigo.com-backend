from sqlalchemy import Table, Column, String, Integer, DateTime

from . import model
from ..database import metadata, mapper_registry

files = Table(
    "files",
    metadata,
    Column("id", Integer, autoincrement=True, primary_key=True),
    Column("filename", String(100)),
    Column("path", String(500)),
    Column("uploaded_at", DateTime)
)


def start_mappers():
    mapper_registry.map_imperatively(model.File, files)
