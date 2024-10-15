from typing import Protocol

import jwt


class JwtService(Protocol):

    def encode(self, payload: dict, secret_key: str, algorithm: str) -> str:
        ...

    def decode(
            self, token: str, secret_key: str, algorithms: list[str]
    ) -> dict:
        ...


class PyJwtService:

    def __init__(self):
        self._jwt = jwt

    def encode(self, payload: dict, secret_key: str, algorithm: str) -> str:
        return self._jwt.encode(
            payload=payload,
            key=secret_key,
            algorithm=algorithm
        )

    def decode(
            self, token: str, secret_key: str, algorithms: list[str]
    ) -> dict:
        return self._jwt.decode(
            jwt=token, key=secret_key, algorithms=algorithms
        )
