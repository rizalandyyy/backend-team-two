import pytest
from config.settings import create_app


@pytest.fixture
def app():
    """Create a Flask application instance for testing."""
    app = create_app("config.testing")
    yield app


@pytest.fixture
def client(app):
    """Create a test client for the Flask application."""
    return app.test_client()
