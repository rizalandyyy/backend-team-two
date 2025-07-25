from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.product import Products
from models.product_detail import ProductDetails
from models.user import Users, UserRole
from instance.database import db

product_bp = Blueprint("product_bp", __name__)

# Utility: check if user is admin
def is_admin():
    current_user_id = get_jwt_identity()
    user = Users.query.get(current_user_id)
    return user and user.role == UserRole.ADMIN





# Endpoint: Get All Products (Public)
@product_bp.route("/products", methods=["GET"])
def get_all_products():
    products = Products.query.all()
    result = []
    for product in products:
        result.append({
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "condition": product.condition,
            "image_url": product.image_url,
            "description": product.details.description if product.details else None,
            # "image1_url": product.details.image1_url if product.details else None,
            # "image2_url": product.details.image2_url if product.details else None,
            # "image3_url": product.details.image3_url if product.details else None,
        })
    return jsonify(result), 200

# Endpoint: Get Product by ID (Public)
@product_bp.route("/products/<int:product_id>", methods=["GET"])
def get_product_by_id(product_id):
    product = Products.query.get(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    data = {
        "id": product.id,
        "name": product.name,
        "price": product.price,
        "condition": product.condition,
        "image_url": product.image_url,
        "description": product.details.description if product.details else None,
        "image1_url": product.details.image1_url if product.details else None,
        "image2_url": product.details.image2_url if product.details else None,
        "image3_url": product.details.image3_url if product.details else None,
    }
    return jsonify(data), 200