from __future__ import annotations
import time

from .repository import UserRepositoryInterface
from . import model
from .auth.jwt import JwtService, PyJwtService
from .auth.password import PasswordService, BcryptPasswordService
from .error import PasswordNotMatch, InvalidPassword
from .. import config


class RegistrationService:

    def __init__(
            self,
            repo: UserRepositoryInterface,
            password_service: PasswordService = BcryptPasswordService()
    ):
        self.repo = repo
        self.password_service = password_service

    def execute(
            self,
            username: str,
            password: str,
            repeat_password: str,
            role: model.UserRole
    ) -> model.User:

        if password != repeat_password:
            raise PasswordNotMatch

        password = self.password_service.hash_password(password)

        user = model.User(username=username, password=password, role=role)
        self.repo.add(user)

        return user


class AuthenticationService:

    def __init__(
            self,
            repo: UserRepositoryInterface,
            password_service: PasswordService = BcryptPasswordService(),
            jwt_service: JwtService = PyJwtService()
    ):
        self.repo = repo
        self.password_service = password_service
        self.jwt_service = jwt_service

    def execute(self, username: str, password: str) -> dict:
        user = self.repo.get_by_username(username=username)

        if not self.password_service.check_password(password, user.password):
            raise InvalidPassword

        payload = {
            "sub": username,
            "exp": time.time() + (config.JWT_ACCESS_TOKEN_LIFESPAN * 60)
        }

        token = self.jwt_service.encode(
            payload=payload,
            secret_key=config.SECRET_KEY,
            algorithm=config.JWT_ALGORITH
        )

        return {"access": token, "token_type": "bearer"}
