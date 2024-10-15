from fastapi import status, APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse

from .service import RegistrationService, AuthenticationService
from .error import PasswordNotMatch, UserNotExists, InvalidPassword
from .repository import SqlAlchemyUserRepository
from .dto import UserDTO, RegisterUserDTO, LoginDTO
from ..database import get_session

router = APIRouter(prefix="/users")


@router.post(
    "/register",
    response_model=UserDTO,
    status_code=status.HTTP_201_CREATED
)
def registration_controller(
        dto: RegisterUserDTO,
        session=Depends(get_session),
):
    repo = SqlAlchemyUserRepository(session=session)
    register_service = RegistrationService(repo=repo)

    try:
        user = register_service.execute(
            username=dto.username,
            password=dto.password,
            repeat_password=dto.repeat_password,
            role=dto.role,
        )

    except PasswordNotMatch as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=error.message
        )

    return user


@router.post("/login")
def login_controller(
        dto: LoginDTO,
        session=Depends(get_session),
) -> JSONResponse:
    repo = SqlAlchemyUserRepository(session=session)
    login_service = AuthenticationService(repo=repo)

    try:
        data = login_service.execute(
            username=dto.username,
            password=dto.password,
        )

    except (InvalidPassword, UserNotExists):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect username or password"
        )

    return JSONResponse(content=data, status_code=status.HTTP_200_OK)
