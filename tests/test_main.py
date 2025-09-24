import pytest
from app.main import app as flask_app

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_status_code(client):
    """Test that the home page returns a 200 status code."""
    response = client.get("/")
    assert response.status_code == 200

def test_hello_world(client):
    """Test that the home page returns 'Hello, World!'."""
    response = client.get("/")
    assert b"Hello, World!" in response.data