from flask import request, jsonify
from flask.views import MethodView
from flask import Blueprint
from services.product_detail_services import ProductDetailService

product_detail_bp = Blueprint("product_detail", __name__, url_prefix="/product-details")


class ProductDetailAPI(MethodView):
    def get(self, detail_id=None):
        if detail_id is None:
            details = ProductDetailService.list_product_details()
            return jsonify(
                [
                    {
                        "id": d.id,
                        "product_id": d.product_id,
                        "description": d.description,
                        "image1_url": d.image1_url,
                        "image2_url": d.image2_url,
                        "image3_url": d.image3_url,
                        "created_at": d.created_at.isoformat(),
                        "updated_at": d.updated_at.isoformat(),
                    }
                    for d in details
                ]
            )
        else:
            detail = ProductDetailService.get_product_detail(detail_id)
            if not detail:
                return jsonify({"error": "Not found"}), 404
            return jsonify(
                {
                    "id": detail.id,
                    "product_id": detail.product_id,
                    "description": detail.description,
                    "image1_url": detail.image1_url,
                    "image2_url": detail.image2_url,
                    "image3_url": detail.image3_url,
                    "created_at": detail.created_at.isoformat(),
                    "updated_at": detail.updated_at.isoformat(),
                }
            )

    def post(self):
        data = request.get_json()
        new_detail = ProductDetailService.create_product_detail(data)
        return jsonify({"message": "Created", "id": new_detail.id}), 201

    def put(self, detail_id):
        data = request.get_json()
        updated = ProductDetailService.update_product_detail(detail_id, data)
        if not updated:
            return jsonify({"error": "Not found"}), 404
        return jsonify({"message": "Updated"})

    def delete(self, detail_id):
        deleted = ProductDetailService.delete_product_detail(detail_id)
        if not deleted:
            return jsonify({"error": "Not found"}), 404
        return jsonify({"message": "Deleted"})


# 📌 Daftarkan route
product_detail_view = ProductDetailAPI.as_view("product_detail_api")
product_detail_bp.add_url_rule(
    "/", defaults={"detail_id": None}, view_func=product_detail_view, methods=["GET"]
)
product_detail_bp.add_url_rule("/", view_func=product_detail_view, methods=["POST"])
product_detail_bp.add_url_rule(
    "/<int:detail_id>", view_func=product_detail_view, methods=["GET", "PUT", "DELETE"]
)
