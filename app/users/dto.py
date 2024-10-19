import pydantic

from . import model


class CreateUserDTO(pydantic.BaseModel):
    username: pydantic.EmailStr
    password: str
    repeat_password: str
    role: model.UserRole


class LoginDTO(pydantic.BaseModel):
    username: pydantic.EmailStr
    password: str


class UserDTO(pydantic.BaseModel):
    id: int
    username: str
    role: model.UserRole

    class Config:
        from_attributes = True


class TokenDTO(pydantic.BaseModel):
    access: str

    class Config:
        from_attributes = True
