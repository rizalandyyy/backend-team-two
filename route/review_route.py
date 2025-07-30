from flask import Blueprint, jsonify, request
from flask.views import MethodView
from services.review_service import ReviewService
from flask_jwt_extended import jwt_required, get_jwt_identity

review_router = Blueprint("review_router", __name__, url_prefix="/reviews")
review_service = ReviewService()


class ReviewAPI(MethodView):
    def get(self):
        """GET /reviews - Get all reviews"""
        try:
            reviews = review_service.get_all_reviews()
            return jsonify({"success": True, "data": reviews}), 200
        except Exception:
            return jsonify({"success": False, "error": "Internal server error"}), 500

    @jwt_required()
    def post(self):
        """POST /reviews - Create a new review"""
        try:
            current_user_id = int(get_jwt_identity())
            data = request.get_json() or {}

            # Enforce user_id from JWT, ignore client-provided user_id
            data["user_id"] = current_user_id

            created = review_service.create_review(data)
            return jsonify({"success": True, "data": created}), 201
        except ValueError as e:
            return jsonify({"success": False, "error": str(e)}), 409
        except Exception:
            return jsonify({"success": False, "error": "Internal server error"}), 500


class ReviewByUserAPI(MethodView):
    def get(self, user_id):
        try:
            reviews = review_service.get_reviews_by_user(user_id)
            return jsonify({"success": True, "data": reviews}), 200
        except ValueError as e:
            return jsonify({"success": False, "error": str(e)}), 404


class ReviewByProductAPI(MethodView):
    def get(self, product_id):
        try:
            reviews = review_service.get_reviews_by_product(product_id)
            return jsonify({"success": True, "data": reviews}), 200
        except ValueError as e:
            return jsonify({"success": False, "error": str(e)}), 404


class ReviewByUserAndProductAPI(MethodView):
    def get(self, user_id, product_id):
        try:
            review = review_service.get_review(user_id, product_id)
            return jsonify({"success": True, "data": review}), 200
        except ValueError as e:
            return jsonify({"success": False, "error": str(e)}), 404

    @jwt_required()
    def put(self, user_id, product_id):
        """PUT /reviews/<user_id>/<product_id> - Update review"""
        try:
            current_user_id = int(get_jwt_identity())
            if user_id != current_user_id:
                return jsonify({"success": False, "error": "Unauthorized"}), 403

            data = request.get_json() or {}

            # Enforce user_id in update data as well
            data["user_id"] = current_user_id

            updated = review_service.update_review(user_id, product_id, data)
            return jsonify({"success": True, "data": updated}), 200
        except ValueError as e:
            return jsonify({"success": False, "error": str(e)}), 404
        except Exception:
            return jsonify({"success": False, "error": "Internal server error"}), 500

    @jwt_required()
    def delete(self, user_id, product_id):
        """DELETE /reviews/<user_id>/<product_id> - Delete review"""
        try:
            current_user_id = int(get_jwt_identity())
            if user_id != current_user_id:
                return jsonify({"success": False, "error": "Unauthorized"}), 403

            review_service.delete_review(user_id, product_id)
            return jsonify({"success": True, "message": "Review deleted"}), 200
        except ValueError as e:
            return jsonify({"success": False, "error": str(e)}), 404
        except Exception:
            return jsonify({"success": False, "error": "Internal server error"}), 500


# Register routes
review_router.add_url_rule("/", view_func=ReviewAPI.as_view("review_api"))
review_router.add_url_rule(
    "/user/<int:user_id>", view_func=ReviewByUserAPI.as_view("review_by_user")
)
review_router.add_url_rule(
    "/product/<int:product_id>",
    view_func=ReviewByProductAPI.as_view("review_by_product"),
)
review_router.add_url_rule(
    "/<int:user_id>/<int:product_id>",
    view_func=ReviewByUserAndProductAPI.as_view("review_user_product"),
)
