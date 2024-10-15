from typing import Protocol

import bcrypt


class PasswordService(Protocol):

    def hash_password(self, password: str) -> str:
        ...

    def check_password(self, password: str, hashed_password: str) -> bool:
        ...


class BcryptPasswordService:

    def __init__(self):
        self._bcrypt = bcrypt

    def hash_password(self, password: str) -> str:
        password = password.encode()
        salt = self._bcrypt .gensalt()
        hashed_password = self._bcrypt .hashpw(password=password, salt=salt)
        password = hashed_password.decode()
        return password

    def check_password(self, password: str, hashed_password: str) -> bool:
        return self._bcrypt.checkpw(
            password=password.encode(),
            hashed_password=hashed_password.encode()
        )
