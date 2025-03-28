from unittest.mock import MagicMock, patch
import pytest
from user_management.auth import get_current_user,create_access_token
from fastapi import HTTPException
import uuid

@pytest.fixture
def mock_db():
    """Fixture to mock database session."""
    return MagicMock()

@pytest.fixture
def mock_user():
    """Fixture to return a fake user."""
    return {"id": str(uuid.uuid4()), "username": "testuser"}

@patch("user_management.auth.get_user")  # Mock get_user function
@pytest.mark.asyncio
async def test_get_current_user(mock_get_user, mock_db, mock_user):
    """Test get_current_user with a valid JWT."""
    mock_get_user.return_value = mock_user  # Mock user retrieval

    valid_token = create_access_token({"sub": mock_user["id"]})
    
    user = await get_current_user(valid_token, db=mock_db)
    
    assert user["username"] == "testuser"

@patch("user_management.auth.get_user")
@pytest.mark.asyncio
async def test_get_current_user_invalid_token(mock_get_user, mock_db):
    """Test get_current_user with an invalid token."""
    mock_get_user.return_value = None  # Simulate user not found

    invalid_token = "invalid.token.value"

    with pytest.raises(HTTPException) as exc:
        await get_current_user(invalid_token, db=mock_db)

    assert exc.value.status_code == 401
