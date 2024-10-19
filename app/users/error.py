class PasswordNotMatch(Exception):
    message: str = "Passwords do not match!"


class InvalidPassword(Exception):
    message: str = "Invalid password!"


class UserNotExists(Exception):

    def __init__(self, username: str):
        super().__init__(f"User with username '{username}' does not exist.")
