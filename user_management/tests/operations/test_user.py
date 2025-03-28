from unittest.mock import MagicMock, patch
import uuid
import pytest
from user_management.operations import user
from user_management.schemas.user import CreateUser
from user_management.models.user import User


@pytest.fixture
def mock_db():
    return MagicMock()


@pytest.fixture
def mock_user():
    usr = User()
    usr.id = uuid.uuid4()
    usr.email = "test@example.com"
    usr.username = "testuser"
    usr.password_hash = "hashedpassword"
    return usr


def test_create_user(mock_db):
    mock_db.add = MagicMock()
    mock_db.commit = MagicMock()
    mock_db.refresh = MagicMock()
    data = CreateUser(username="test",email="test@test.com",password="password")
    uid = user.create_user(data, mock_db)
    assert isinstance(uid,uuid.UUID)
    mock_db.add.assert_called_once()
    mock_db.commit.assert_called_once()
    mock_db.refresh.assert_called_once()


@patch("user_management.operations.user.get_user")
def test_get_user(mock_get_user, mock_db, mock_user):
    mock_get_user.return_value = mock_user
    usr = user.get_user(mock_user.id, mock_db)
    assert usr is not None
    assert usr.id == mock_user.id
