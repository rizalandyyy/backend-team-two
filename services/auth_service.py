from flask import current_app
from repo.user_repository import UserRepository
from flask_jwt_extended import create_access_token
from datetime import timedelta


class AuthService:
    @staticmethod
    def register_user(username, email, password):
        if UserRepository.get_user_by_username(username):
            return {"message": "Username already taken"}, 409
        if UserRepository.get_user_by_email(email):
            return {"message": "Email already registered"}, 409

        bcrypt = current_app.extensions["bcrypt"]
        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
        user = UserRepository.create_user(username, email, hashed_password)
        access_token = create_access_token(
            identity=str(user.id), additional_claims={"username": user.username}
        )

        return {
            "message": "User registered successfully",
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
            },
            "access_token": access_token,
        }, 201

    @staticmethod
    def login_user(username, password):
        user = UserRepository.get_user_by_username(username)
        if not user:
            return {"message": "Invalid credentials"}, 401

        bcrypt = current_app.extensions["bcrypt"]
        if not bcrypt.check_password_hash(user.password_hash, password):
            return {"message": "Invalid credentials"}, 401

        access_token = create_access_token(
            identity=str(user.id), additional_claims={"username": user.username}
        )

        return {
            "message": "Login successful",
            "access_token": access_token,
            "user": {"id": user.id, "username": user.username, "email": user.email},
        }, 200

    @staticmethod
    def logout_user():
        return {"message": "Logged out successfully"}, 200
