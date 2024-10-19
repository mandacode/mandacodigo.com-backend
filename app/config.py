import os

from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
JWT_ALGORITH = "HS256"
SECRET_KEY = os.getenv("SECRET_KEY")
JWT_ACCESS_TOKEN_LIFESPAN = 10
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
AWS_DEFAULT_REGION = os.getenv("AWS_DEFAULT_REGION")
AWS_UPLOAD_DIR = 'uploads'
