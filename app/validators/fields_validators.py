from flask import json as jsonify
from app.validators.input_validators import (
    validate_string, 
    validate_integer, 
    validate_email, 
    validate_phone_number,
    )


def validate_request(fields):
    
    items = {
        "product_id":"integer",
        "phonenumber":"phonenumber",
        "email":"email",
        "location": "string",
        "building": "string",
        "quantity": "integer",
        "name": "string",
        "description": "string",
        "price": "integer",
    }
    
    response = None
    for key, value in fields.items():
        
        if items[key] == 'string':
            if validate_string(value) == False:
                return False, key
        elif items[key] == 'integer':
            if validate_integer(value) == False:
                return False, key
        elif items[key] == 'email':
            if validate_email(value) == False:
                return False, key
        elif items[key] == 'phonenumber':
            if validate_phone_number(value) == False:
                return False, key
       
    return True