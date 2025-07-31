from flask import Blueprint, request, jsonify
from services.auth_service import AuthService
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity,
    current_user as jwt_current_user,
)
from flask.views import MethodView

auth_bp = Blueprint("auth_bp", __name__)


class RegisterAPI(MethodView):
    def post(self):
        data = request.get_json()
        if not data:
            return jsonify({"message": "Invalid JSON"}), 400

        username = data.get("username")
        email = data.get("email")
        password = data.get("password")

        if not username or not email or not password:
            return (
                jsonify({"message": "Username, email, and password are required"}),
                400,
            )

        response, status_code = AuthService.register_user(username, email, password)
        return jsonify(response), status_code


class LoginAPI(MethodView):
    def post(self):
        data = request.get_json()
        if not data:
            return jsonify({"message": "Invalid JSON"}), 400

        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return jsonify({"message": "Username and password are required"}), 400

        response, status_code = AuthService.login_user(username, password)
        return jsonify(response), status_code


class LogoutAPI(MethodView):
    @jwt_required()
    def post(self):
        response, status_code = AuthService.logout_user()
        return jsonify(response), status_code


class ProtectedAPI(MethodView):
    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        return jsonify(logged_in_as=current_user), 200


auth_bp.add_url_rule("/register", view_func=RegisterAPI.as_view("register_api"))
auth_bp.add_url_rule("/login", view_func=LoginAPI.as_view("login_api"))
auth_bp.add_url_rule("/logout", view_func=LogoutAPI.as_view("logout_api"))
auth_bp.add_url_rule("/protected", view_func=ProtectedAPI.as_view("protected_api"))
