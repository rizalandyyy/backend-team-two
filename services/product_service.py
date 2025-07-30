from repo.product_repo import ProductRepository
from repo.product_detail_repo import ProductDetailRepository


class ProductService:
    @staticmethod
    def list_products():
        return ProductRepository.get_all()

    @staticmethod
    def get_product(product_id):
        return ProductRepository.get_by_id(product_id)

    @staticmethod
    def create_product(data):
        # Create a shallow copy to avoid mutating the input
        product_data = data.copy()

        # Extract detail-related fields
        details_data = {
            "description": product_data.pop("description", None),
            "image1_url": product_data.pop("image1_url", None),
            "image2_url": product_data.pop("image2_url", None),
            "image3_url": product_data.pop("image3_url", None),
        }

        # Create the product
        product = ProductRepository.create(product_data)

        # Optionally create product details
        if any(details_data.values()):
            details_data["product_id"] = product.id
            ProductDetailRepository.create(details_data)

        return product

    @staticmethod
    def update_product(product_id, data):
        product = ProductRepository.get_by_id(product_id)
        if not product:
            return None

        ProductRepository.update(product_id, data)

        if product.details:
            ProductDetailRepository.update(
                product.details.id,
                {
                    "description": data.get("description", product.details.description),
                    "image1_url": data.get("image1_url", product.details.image1_url),
                    "image2_url": data.get("image2_url", product.details.image2_url),
                    "image3_url": data.get("image3_url", product.details.image3_url),
                },
            )

        return product

    @staticmethod
    def delete_product(product_id):
        product = ProductRepository.get_by_id(product_id)
        if not product:
            return False

        if product.details:
            ProductDetailRepository.delete(product.details.id)

        return ProductRepository.delete(product_id)
