from flask import Blueprint, request, jsonify
from flask.views import MethodView
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.product import Products
from models.product_detail import ProductDetails
from models.user import Users, UserRole
from instance.database import db

product_bp = Blueprint("product_bp", __name__)

# Helper: Check if current user is admin
def is_admin(user_id):
    user = Users.query.get(user_id)
    return user and user.role == UserRole.ADMIN

# Get All Products
class ProductListAPI(MethodView):
    def get(self):
        products = Products.query.all()
        product_list = []

        for product in products:
            product_list.append({
                "id": product.id,
                "name": product.name,
                "price": product.price,
                "condition": product.condition,
                "image_url": product.image_url,
                "details": {
                    "description": product.details.description if product.details else None,
                    "image1_url": product.details.image1_url if product.details else None,
                    "image2_url": product.details.image2_url if product.details else None,
                    "image3_url": product.details.image3_url if product.details else None,
                } if product.details else None
            })

        return jsonify({"products": product_list}), 200

# Update Product (Admin Only)
class ProductUpdateAPI(MethodView):
    @jwt_required()
    def put(self, product_id):
        user_id = get_jwt_identity()
        if not is_admin(user_id):
            return jsonify({"message": "Admin access required"}), 403

        data = request.get_json()
        product = Products.query.get(product_id)

        if not product:
            return jsonify({"message": "Product not found"}), 404

        product.name = data.get("name", product.name)
        product.price = data.get("price", product.price)
        product.condition = data.get("condition", product.condition)
        product.image_url = data.get("image_url", product.image_url)

        # Optional: update details too
        details = product.details
        if details:
            details.description = data.get("description", details.description)
            details.image1_url = data.get("image1_url", details.image1_url)
            details.image2_url = data.get("image2_url", details.image2_url)
            details.image3_url = data.get("image3_url", details.image3_url)

        db.session.commit()
        return jsonify({"message": "Product updated successfully"}), 200

# Register routes
product_bp.add_url_rule("/products", view_func=ProductListAPI.as_view("product_list_api"))
product_bp.add_url_rule("/products/<int:product_id>", view_func=ProductUpdateAPI.as_view("product_update_api"))
