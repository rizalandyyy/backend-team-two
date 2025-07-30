from flask import Blueprint, request, jsonify
from flask.views import MethodView
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.product_service import ProductService
from models.user import Users, UserRole

product_bp = Blueprint("product", __name__, url_prefix="/products")


# Helper
def is_admin(user_id):
    user = Users.query.get(user_id)
    return user and user.role == UserRole.ADMIN


class ProductAPI(MethodView):
    def get(self, product_id=None):
        if product_id is None:
            products = ProductService.list_products()
            return jsonify(
                [
                    {
                        "id": p.id,
                        "name": p.name,
                        "price": p.price,
                        "condition": p.condition,
                        "image_url": p.image_url,
                        "details": (
                            {
                                "description": p.details.description,
                                "image1_url": p.details.image1_url,
                                "image2_url": p.details.image2_url,
                                "image3_url": p.details.image3_url,
                            }
                            if p.details
                            else None
                        ),
                    }
                    for p in products
                ]
            )
        else:
            product = ProductService.get_product(product_id)
            if not product:
                return jsonify({"error": "Product not found"}), 404
            return jsonify(
                {
                    "id": product.id,
                    "name": product.name,
                    "price": product.price,
                    "condition": product.condition,
                    "image_url": product.image_url,
                    "details": (
                        {
                            "description": product.details.description,
                            "image1_url": product.details.image1_url,
                            "image2_url": product.details.image2_url,
                            "image3_url": product.details.image3_url,
                        }
                        if product.details
                        else None
                    ),
                }
            )

    @jwt_required()
    def post(self):
        user_id = get_jwt_identity()
        if not is_admin(user_id):
            return jsonify({"message": "Admin access required"}), 403

        data = request.get_json()
        product = ProductService.create_product(data)
        return jsonify({"message": "Product created", "id": product.id}), 201

    @jwt_required()
    def put(self, product_id):
        user_id = get_jwt_identity()
        if not is_admin(user_id):
            return jsonify({"message": "Admin access required"}), 403

        data = request.get_json()
        updated = ProductService.update_product(product_id, data)
        if not updated:
            return jsonify({"message": "Product not found"}), 404
        return jsonify({"message": "Product updated"})

    @jwt_required()
    def delete(self, product_id):
        user_id = get_jwt_identity()
        if not is_admin(user_id):
            return jsonify({"message": "Admin access required"}), 403

        deleted = ProductService.delete_product(product_id)
        if not deleted:
            return jsonify({"error": "Product not found"}), 404
        return jsonify({"message": "Product deleted"})


# 📌 Register routes
product_view = ProductAPI.as_view("product_api")
product_bp.add_url_rule(
    "/", defaults={"product_id": None}, view_func=product_view, methods=["GET"]
)
product_bp.add_url_rule("/", view_func=product_view, methods=["POST"])
product_bp.add_url_rule(
    "/<int:product_id>", view_func=product_view, methods=["GET", "PUT", "DELETE"]
)
