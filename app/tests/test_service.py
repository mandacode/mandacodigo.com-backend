import pytest

from auth import model, repository, service


def mock_hash_password(password: str) -> str:
    return password + "_hashed"


def test_service__passwords_not_match():
    repo = repository.MockUserRepository()
    register_service = service.RegisterService(repo=repo)
    username = "testuser"
    password = "testpass"
    repeat_password = "testpass1"

    with pytest.raises(service.PasswordNotMatch):
        register_service.execute(
            username=username,
            password=password,
            repeat_password=repeat_password
        )


def test_service__user_created():
    repo = repository.MockUserRepository()
    register_service = service.RegisterService(
        repo=repo,
        hash_password=mock_hash_password
    )
    username = "testuser"
    password = repeat_password = "testpass"

    register_service.execute(
        username=username,
        password=password,
        repeat_password=repeat_password
    )

    assert repo.items[0].username == username
    assert repo.items[0].password == mock_hash_password(password)
    assert isinstance(repo.items[0], model.User)
