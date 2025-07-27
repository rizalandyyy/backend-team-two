import pytest
from services.auth_service import AuthService

@pytest.fixture
def dummy_user():
    class DummyUser:
        id = 1
        username = "testuser"
        email = "test@example.com"
        password_hash = "$2b$12$dummyhash"
    return DummyUser()

def test_register_user_success(mocker, app, dummy_user):
    mocker.patch("repo.user_repository.UserRepository.get_user_by_username", return_value=None)
    mocker.patch("repo.user_repository.UserRepository.get_user_by_email", return_value=None)
    mocker.patch("repo.user_repository.UserRepository.create_user", return_value=dummy_user)
    mocker.patch("flask_jwt_extended.create_access_token", return_value="fake_token")

    with app.app_context():
        response, code = AuthService.register_user("newuser", "new@example.com", "password123")

    assert code == 201
    assert response["message"] == "User registered successfully"
    assert "access_token" in response

def test_register_user_username_taken(mocker, dummy_user):
    mocker.patch("repo.user_repository.UserRepository.get_user_by_username", return_value=dummy_user)

    response, code = AuthService.register_user("testuser", "other@example.com", "password")
    assert code == 409
    assert response["message"] == "Username already taken"

def test_register_user_email_taken(mocker, dummy_user):
    mocker.patch("repo.user_repository.UserRepository.get_user_by_username", return_value=None)
    mocker.patch("repo.user_repository.UserRepository.get_user_by_email", return_value=dummy_user)

    response, code = AuthService.register_user("otheruser", "test@example.com", "password")
    assert code == 409
    assert response["message"] == "Email already registered"

def test_login_user_success(mocker, dummy_user, app):
    mocker.patch("repo.user_repository.UserRepository.get_user_by_username", return_value=dummy_user)
    mocker.patch("flask_jwt_extended.create_access_token", return_value="test_token")

    with app.app_context():
        mocker.patch.object(app.extensions['bcrypt'], 'check_password_hash', return_value=True)
        response, code = AuthService.login_user("testuser", "password")

    assert code == 200
    assert "access_token" in response
    assert response["message"] == "Login successful"

def test_login_user_invalid_user(mocker):
    mocker.patch("repo.user_repository.UserRepository.get_user_by_username", return_value=None)

    response, code = AuthService.login_user("wronguser", "password")
    assert code == 401
    assert response["message"] == "Invalid credentials"

def test_login_user_wrong_password(mocker, dummy_user, app):
    mocker.patch("repo.user_repository.UserRepository.get_user_by_username", return_value=dummy_user)

    with app.app_context():
        mocker.patch.object(app.extensions['bcrypt'], 'check_password_hash', return_value=False)
        response, code = AuthService.login_user("testuser", "wrongpass")

    assert code == 401
    assert response["message"] == "Invalid credentials"
