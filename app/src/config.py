import os

from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
JWT_ALGORITH = "HS256"
SECRET_KEY = os.getenv("SECRET_KEY")
JWT_ACCESS_TOKEN_LIFESPAN = 10
