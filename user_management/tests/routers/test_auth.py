from pydoc import cli
import pytest
from unittest.mock import MagicMock, patch
from fastapi.testclient import TestClient
from user_management.main import app  # Import FastAPI app
from user_management.operations import user as user_ops
from user_management.models.user import User
from user_management.schemas.user import CreateUser
from user_management.security import verify_password
from user_management.auth import create_access_token



client = TestClient(app)

@pytest.fixture
def mock_db():
    return MagicMock()


@pytest.fixture
def mock_user():
    user = User()
    user.id = "123e4567-e89b-12d3-a456-426614174000"
    user.email = "test@example.com"
    user.username = "testuser"
    user.password_hash = "$2b$12$hashedpassword"
    return user


@patch("user_management.routers.auth.create_access_token")  # PATCH 1 (Last argument)
@patch("user_management.security.verify_password")  # PATCH 2 (Middle argument)
@patch("user_management.operations.user.get_user_by_email")  # PATCH 3 (First argument)
def test_login(mock_get_user_by_email, mock_verify_password, mock_create_access_token, mock_db, mock_user):  # ✅ Match order
    mock_get_user_by_email.return_value = mock_user
    mock_verify_password.return_value = True
    mock_create_access_token.return_value = "mocked_token"

    response = client.post("/auth/login", data={"username": "test@example.com", "password": "correctpass"})

    assert response.status_code == 200
    assert response.json() == {"access_token": "mocked_token", "token_type": "bearer"}

    mock_get_user_by_email.assert_called_once()
    mock_verify_password.assert_called_once()
    mock_create_access_token.assert_called_once()