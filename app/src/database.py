from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import sessionmaker, registry
from . import config

metadata = MetaData()
mapper_registry = registry()
engine = create_engine(url=config.DATABASE_URL)
Session = sessionmaker(bind=engine, expire_on_commit=False, autocommit=False)


def create_all():
    metadata.create_all(bind=engine)


def get_session():
    db = Session()
    try:
        yield db
    finally:
        db.close()
