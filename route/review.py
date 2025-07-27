from flask import Blueprint, request, jsonify
from services.review_service import ReviewService
from functools import wraps

review_router = Blueprint('review_router', __name__, url_prefix='/api/reviews')
review_service = ReviewService()

@review_router.route('/user/<int:user_id>', methods=['GET'])
def get_review_by_user_route(user_id):
    try:
        reviews = review_service.get_review_by_user(user_id)
        return jsonify({
            "success": True,
            "data": reviews
        }), 200
    except Exception as e:
        return jsonify({"success": False, "error": "Terjadi kesalahan pada server."}), 500

@review_router.route('/product/<int:product_id>', methods=['GET'])
def get_review_by_product_route(product_id):
    try:
        reviews = review_service.get_review_by_product(product_id)
        return jsonify({
            "success": True,
            "data": reviews
        }), 200
    except Exception as e:
        return jsonify({"success": False, "error": "Terjadi kesalahan pada server."}), 500

@review_router.route('/<int:user_id>/<int:product_id>', methods=['GET'])
def get_review_route(user_id, product_id):
    try:
        review = review_service.get_review(user_id, product_id)
        return jsonify({
            "success": True,
            "data": review
        }), 200
    except ValueError as e:
        return jsonify({"success": False, "error": str(e)}), 404
    except Exception as e:
        return jsonify({"success": False, "error": "Terjadi kesalahan pada server."}), 500

@review_router.route('/', methods=['GET'])
def get_all_review_route():
    try:
        reviews = review_service.get_all_reviews()
        return jsonify({
            "success": True,
            "data": reviews
        }), 200
    except Exception as e:
        return jsonify({"success": False, "error": "Terjadi kesalahan pada server."}), 500