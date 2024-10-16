from fastapi import status, APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse

from .service import RegistrationService, AuthenticationService
from .error import PasswordNotMatch, UserNotExists, InvalidPassword
from .repository import SqlAlchemyUserRepository
from .dto import UserDTO, CreateUserDTO, LoginDTO, TokenDTO
from ..database import get_session

router = APIRouter(prefix="/users")


@router.post(
    "/",
    response_model=UserDTO,
    status_code=status.HTTP_201_CREATED
)
def create_user_controller(
        dto: CreateUserDTO,
        session=Depends(get_session),
) -> UserDTO:
    repo = SqlAlchemyUserRepository(session=session)
    service = RegistrationService(repo=repo)

    try:
        user = service.execute(
            username=dto.username,
            password=dto.password,
            repeat_password=dto.repeat_password,
            role=dto.role,
        )

    except PasswordNotMatch as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=error.message
        )

    return UserDTO.from_orm(user)


@router.post("/login", response_model=TokenDTO, status_code=status.HTTP_200_OK)
def login_controller(
        dto: LoginDTO,
        session=Depends(get_session),
) -> TokenDTO:
    repo = SqlAlchemyUserRepository(session=session)
    service = AuthenticationService(repo=repo)

    try:
        token = service.execute(
            username=dto.username,
            password=dto.password,
        )

    except (InvalidPassword, UserNotExists):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect username or password"
        )

    return TokenDTO.from_orm(token)
