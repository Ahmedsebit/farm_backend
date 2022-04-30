from datetime import datetime
from flask import jsonify
from sqlalchemy import exc, asc
from app.app import db
from app.models.products import Products


def get_products():

    products = []
    try:
        products = Products.query.all()
        if products:
            products = list(map(structure_products, products))
        else:
            products = []
        response = jsonify(products)
        response.status_code = 200
        return response
    except exc.SQLAlchemyError as e:
        response = jsonify([])
        response.status_code = 200
        return response

    
    
def get_product(id):
    
    try:
        product = Products.query.filter_by(id=id).one()
        product = structure_products(product)
    except exc.SQLAlchemyError as e:
        product = {}
    else:
        product = {}
    
    response = jsonify(product)
    response.status_code = 200
    return response

    
def structure_products(product):
    return {
        "id": product.id,
        "name": product.name,
        "description": product.description,
        "image_url": product.image_url,
        "price": product.price,
        "created_at": product.created_at
    }
    
    
def create_product(name, description, image_url, price):
    
    try:
        new_product = Products(name, description, image_url, price)
        db.session.add(new_product)
        db.session.commit()
        response = jsonify({"message":"created"})
        response.status_code = 201
        return response
    except exc.SQLAlchemyError as e:
        response = jsonify({"message":"Error occured, product hasnt been added"})
        response.status_code = 201
        return response
    else:
        response = jsonify({"message":"Error occured, product hasnt been added"})
        response.status_code = 201
        return response