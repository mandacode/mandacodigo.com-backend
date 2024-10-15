from typing import Protocol

from . import model
from .error import UserNotExists


class UserRepositoryInterface(Protocol):

    def add(self, user: model.User):
        pass

    def get_by_username(self, username: str) -> model.User:
        pass


class MockUserRepository:

    def __init__(self, users: list[model.User] = None):
        if users is None:
            users = []
        self.users = users

    def add(self, user: model.User):
        self.users.append(user)

    def get_by_username(self, username: str) -> model.User:
        for user in self.users:
            if user.username == username:
                return user
        raise UserNotExists(username)


class SqlAlchemyUserRepository:

    def __init__(self, session):
        self.session = session

    def add(self, user: model.User):
        self.session.add(user)
        self.session.commit()

    def get_by_username(self, username: str) -> model.User:
        user = (
            self.session
            .query(model.User)
            .filter_by(username=username)
            .one_or_none()
        )
        if user is None:
            raise UserNotExists(username)
        return user
