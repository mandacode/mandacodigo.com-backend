from auth import model, repository


class MockSession:

    def __init__(self):
        self.items = []
        self.committed = False

    def commit(self):
        self.committed = True

    def add(self, item: object):
        self.items.append(item)


def test_repository__user_added():
    session = MockSession()
    repo = repository.SqlAlchemyUserRepository(session=session)
    user = model.User(username="testuser", password="testpass")

    repo.add(user)

    assert session.committed
    assert user in session.items
