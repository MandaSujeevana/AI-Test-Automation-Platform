import pytest
from tests.config import BASE_URL


@pytest.fixture
def valid_user_payload():
    """Pytest fixture returning a valid user payload dictionary."""
    return {
        "name": "Sujeevana",
        "email": "sujeevana@example.com"
    }


@pytest.fixture
def users_url():
    """Pytest fixture returning the full endpoint URL for /users."""
    return f"{BASE_URL}/users"
