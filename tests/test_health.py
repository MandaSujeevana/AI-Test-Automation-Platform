import requests
from tests.config import BASE_URL


def test_health_check():
    """Test that the /health endpoint returns HTTP 200 OK and status healthy."""
    url = f"{BASE_URL}/health"
    response = requests.get(url)

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
