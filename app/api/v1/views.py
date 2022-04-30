import json
from flask import Blueprint, request, jsonify


farm_backend_v1_api_bp = Blueprint(
    'farm_backend_v1_api_bp', __name__,
)


@farm_backend_v1_api_bp.route('/api/test', methods=['GET'])
def test_api():
    response = jsonify({"message": "OK"})
    response.status_code = 200
    return response

