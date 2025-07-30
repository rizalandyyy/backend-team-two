from flask import Blueprint, jsonify
from flask.views import MethodView
from services.review_service import ReviewService

review_router = Blueprint("review_router", __name__, url_prefix="/api/reviews")
review_service = ReviewService()


class ReviewAPI(MethodView):
    def get(self):
        """GET /api/reviews - Get all reviews"""
        try:
            reviews = review_service.get_all_reviews()
            return jsonify({"success": True, "data": reviews}), 200
        except Exception:
            return (
                jsonify(
                    {"success": False, "error": "An internal server error occurred."}
                ),
                500,
            )


class ReviewByUserAPI(MethodView):
    def get(self, user_id):
        """GET /api/reviews/user/<user_id> - Get reviews by user"""
        try:
            reviews = review_service.get_reviews_by_user(user_id)
            return jsonify({"success": True, "data": reviews}), 200
        except ValueError as e:
            return jsonify({"success": False, "error": str(e)}), 404
        except Exception:
            return (
                jsonify(
                    {"success": False, "error": "An internal server error occurred."}
                ),
                500,
            )


class ReviewByProductAPI(MethodView):
    def get(self, product_id):
        """GET /api/reviews/product/<product_id> - Get reviews by product"""
        try:
            reviews = review_service.get_reviews_by_product(product_id)
            return jsonify({"success": True, "data": reviews}), 200
        except ValueError as e:
            return jsonify({"success": False, "error": str(e)}), 404
        except Exception:
            return (
                jsonify(
                    {"success": False, "error": "An internal server error occurred."}
                ),
                500,
            )


class ReviewByUserAndProductAPI(MethodView):
    def get(self, user_id, product_id):
        """GET /api/reviews/<user_id>/<product_id> - Get review by user and product"""
        try:
            review = review_service.get_review(user_id, product_id)
            return jsonify({"success": True, "data": review}), 200
        except ValueError as e:
            return jsonify({"success": False, "error": str(e)}), 404
        except Exception:
            return (
                jsonify(
                    {"success": False, "error": "An internal server error occurred."}
                ),
                500,
            )


# Register routes
review_router.add_url_rule("/", view_func=ReviewAPI.as_view("review_all"))
review_router.add_url_rule(
    "/user/<int:user_id>", view_func=ReviewByUserAPI.as_view("review_by_user")
)
review_router.add_url_rule(
    "/product/<int:product_id>",
    view_func=ReviewByProductAPI.as_view("review_by_product"),
)
review_router.add_url_rule(
    "/<int:user_id>/<int:product_id>",
    view_func=ReviewByUserAndProductAPI.as_view("review_by_user_and_product"),
)
