from flask import Blueprint, request, jsonify
from services import product_detail_services

product_detail_bp = Blueprint(
    "product_detail_bp", __name__, url_prefix="/product-details"
)


@product_detail_bp.route("/product/<int:product_id>", methods=["GET"])
def get_detail_by_product(product_id):
    try:
        detail = product_detail_services.get_details_by_product_id(product_id)
        return (
            jsonify(
                {
                    "id": detail.id,
                    "product_id": detail.product_id,
                    "description": detail.description,
                    "image1_url": detail.image1_url,
                    "image2_url": detail.image2_url,
                    "image3_url": detail.image3_url,
                    "created_at": detail.created_at,
                }
            ),
            200,
        )
    except ValueError as e:
        return jsonify({"error": str(e)}), 404


@product_detail_bp.route("/<int:detail_id>", methods=["GET"])
def get_detail(detail_id):
    try:
        detail = product_detail_services.get_detail_by_id(detail_id)
        return (
            jsonify(
                {
                    "id": detail.id,
                    "product_id": detail.product_id,
                    "description": detail.description,
                    "image1_url": detail.image1_url,
                    "image2_url": detail.image2_url,
                    "image3_url": detail.image3_url,
                    "created_at": detail.created_at,
                }
            ),
            200,
        )
    except ValueError as e:
        return jsonify({"error": str(e)}), 404


@product_detail_bp.route("/", methods=["POST"])
def create_detail():
    data = request.get_json()
    try:
        detail = product_detail_services.create_product_detail(data)
        return (
            jsonify({"message": "Product detail created", "detail_id": detail.id}),
            201,
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@product_detail_bp.route("/<int:detail_id>", methods=["PUT"])
def update_detail(detail_id):
    data = request.get_json()
    try:
        detail = product_detail_services.update_product_detail(detail_id, data)
        return (
            jsonify({"message": "Product detail updated", "detail_id": detail.id}),
            200,
        )
    except ValueError as e:
        return jsonify({"error": str(e)}), 404


@product_detail_bp.route("/<int:detail_id>", methods=["DELETE"])
def delete_detail(detail_id):
    try:
        product_detail_services.delete_product_detail(detail_id)
        return jsonify({"message": "Product detail deleted"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
