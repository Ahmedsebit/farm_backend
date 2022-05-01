from flask import json as jsonify
from app.validators.input_validators import (
    validate_string, 
    validate_integer, 
    validate_email, 
    validate_phone_number,
    )


def validate_product_fields(data):
    
    all_fields = ["description", "name", "price"]
    fields = [key for key, value in data.items()]
    missing_fields = None
    
    for i in all_fields:
        if i not in fields:
            if not missing_fields:
                missing_fields = i
            else:
                f'{missing_fields} {i}'
                
    return missing_fields


def validate_order_fields(data):
    all_fields = ["product_id", "email", "phonenumber", "location", "building", "quantity"]
    fields = [key for key, value in data.items()]
    missing_fields = None
    
    for i in all_fields:
        if i not in fields:
            if not missing_fields:
                missing_fields = i
            else:
                f'{missing_fields} {i}'
                
    return missing_fields


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
       
    return True, "OK"