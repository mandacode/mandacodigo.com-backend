from fastapi import FastAPI

from .users.controller import router as auth_router
from .users.orm import start_mappers as start_auth_mappers
from .courses.orm import start_mappers as start_courses_mappers
from .database import create_all

app = FastAPI()
app.include_router(auth_router)


@app.on_event('startup')
def startup_event():
    create_all()
    start_auth_mappers()
    start_courses_mappers()


@app.on_event('shutdown')
def shutdown_event():
    ...


@app.get("/")
def root_endpoint() -> str:
    return "This is mandacodigo.com"
