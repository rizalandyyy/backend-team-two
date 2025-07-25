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


# Endpoint: Update Product (Admin Only)
@product_bp.route("/products/<int:product_id>", methods=["PUT"])
@jwt_required()
def update_product(product_id):
    user_id = get_jwt_identity()
    if not is_admin(user_id):
        return jsonify({"error": "Admin access required"}), 403

    product = Products.query.get(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    data = request.get_json()
    try:
        product.name = data.get("name", product.name)
        product.price = data.get("price", product.price)
        product.condition = data.get("condition", product.condition)
        product.image_url = data.get("image_url", product.image_url)

        if product.details:
            product.details.description = data.get("description", product.details.description)
            product.details.image1_url = data.get("image1_url", product.details.image1_url)
            product.details.image2_url = data.get("image2_url", product.details.image2_url)
            product.details.image3_url = data.get("image3_url", product.details.image3_url)

        db.session.commit()
        return jsonify({"message": "Product updated successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400


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