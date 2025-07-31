from repo.product_detail_repo import ProductDetailRepository


class ProductDetailService:
    @staticmethod
    def list_product_details():
        return ProductDetailRepository.get_all()

    @staticmethod
    def get_product_detail(detail_id):
        return ProductDetailRepository.get_by_id(detail_id)

    @staticmethod
    def create_product_detail(data):
        return ProductDetailRepository.create(data)

    @staticmethod
    def update_product_detail(detail_id, data):
        return ProductDetailRepository.update(detail_id, data)

    @staticmethod
    def delete_product_detail(detail_id):
        return ProductDetailRepository.delete(detail_id)
