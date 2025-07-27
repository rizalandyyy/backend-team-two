from flask import Blueprint, request, jsonify
from instance.database import db
from models.product import Products

product_bp = Blueprint('product_bp', __name__)

@product_bp.route('/products', methods=['POST'])
def add_product():
    data = request.json
    try:
        new_product = Products(
            name=data['name'],
            price=data['price'],
            condition=data['condition'],
            image_url=data.get('image_url')
        )
        db.session.add(new_product)
        db.session.commit()
        return jsonify({"message": "Product added successfully", "product": new_product.id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@product_bp.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Products.query.get(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": "Product deleted successfully"}), 200