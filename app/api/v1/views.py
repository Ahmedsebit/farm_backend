import json
from flask import Blueprint, request
from app.repositories.products import get_products, get_product, create_product
from app.utils.uploads import upload_files


farm_backend_v1_api_bp = Blueprint(
    'farm_backend_v1_api_bp', __name__,
)


@farm_backend_v1_api_bp.route('/products', methods=['GET'])
def get_products_api():
    return get_products()


@farm_backend_v1_api_bp.route('/products', methods=['POST'])
def add_product_api():
    data = request.data
    
    file = data.get("file")
    file_url = upload_files(file) 
    return create_product(
                    data.get("name"), 
                    data.get("description"), 
                    file_url, 
                    data.get("price"),
                    )

@farm_backend_v1_api_bp.route('/products/<int:id>', methods=['GET'])
def get_product_api(id):
    return get_product(id)
