import pytest
import requests


def test_create_user(users_url, valid_user_payload):
    """Test that POST /users creates a user and returns the expected user payload."""
    response = requests.post(users_url, json=valid_user_payload)
    data = response.json()

    assert response.status_code == 200
    assert data["message"] == "User created successfully"
    assert data["user"]["name"] == "Sujeevana"
    assert data["user"]["email"] == "sujeevana@example.com"


@pytest.mark.parametrize(
    "payload",
    [
        {"name": "Sujeevana"},
        {"email": "sujeevana@example.com"},
    ],
)
def test_create_user_missing_required_field(users_url, payload):
    """Test that POST /users missing a required field returns HTTP 422 Unprocessable Entity."""
    response = requests.post(users_url, json=payload)

    assert response.status_code == 422


@pytest.mark.parametrize(
    "payload",
    [
        {"name": 123, "email": "sujeevana@example.com"},
        {"name": "Sujeevana", "email": 123},
    ],
)
def test_create_user_invalid_field_types(users_url, payload):
    """Test that POST /users with invalid field types returns HTTP 422 Unprocessable Entity."""
    response = requests.post(users_url, json=payload)

    assert response.status_code == 422
