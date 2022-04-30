import json
from flask import Blueprint, request, jsonify
from app.repositories.products import get_products, get_product, create_product
from app.repositories.orders import create_order, get_order, get_user_orders
from app.validators.fields_validators import validate_request
from app.utils.uploads import upload_files


farm_backend_v1_api_bp = Blueprint(
    'farm_backend_v1_api_bp', __name__,
)


@farm_backend_v1_api_bp.route('/products', methods=['GET'])
def get_products_api():
    
    return get_products()


@farm_backend_v1_api_bp.route('/products/<int:id>', methods=['GET'])
def get_product_api(id):
    
    return get_product(id)


@farm_backend_v1_api_bp.route('/products', methods=['POST'])
def add_product_api():
    
    data = request.data
    validated_product_request = validate_request(data)
    
    if not validated_product_request[0]:
        response = jsonify({"message":f'Missing or invalid field {validated_product_request[1]}'})
        response.status_code = 400
        return response
    
    file = data.get("file")
    file_url = upload_files(file) 
    return create_product(
                    data.get("name"), 
                    data.get("description"), 
                    file_url, 
                    data.get("price"),
                    )


@farm_backend_v1_api_bp.route('/orders/user/<string:email>', methods=['GET'])
def get_user_orders_api(email):
    
    return get_user_orders(email)


@farm_backend_v1_api_bp.route('/orders/<int:id>', methods=['GET'])
def get_order_api(id):
    
    return get_order(id)


@farm_backend_v1_api_bp.route('/orders', methods=['POST'])
def add_order_api():
    
    data = request.data
    validated_order_request = validate_request(data)
    
    if not validated_order_request[0]:
        response = jsonify({"message":f'Missing or invalid field {validated_order_request[1]}'})
        response.status_code = 400
        return response
    
    product_id = data.get("product_id")
    email = data.get("email")
    phonenumber = data.get("phonenumber")
    location = data.get("location")
    building = data.get("building")
    quantity = data.get("quantity")
    return create_order(product_id, email, phonenumber, location, building, quantity)