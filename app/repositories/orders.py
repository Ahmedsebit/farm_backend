from datetime import datetime
from flask import jsonify
from sqlalchemy import exc, asc
from app.app import db
from app.models.orders import Orders


def get_user_orders(email):

    orders = []
    try:
        orders = Orders.query.filter_by(email=email).all()
        if orders:
            orders = list(map(structure_orders, orders))
        else:
            orders = []
        response = jsonify(orders)
        response.status_code = 200
        return response
    except exc.SQLAlchemyError as e:
        response = jsonify([])
        response.status_code = 200
        return response

    
    
def get_order(id):
    
    try:
        order = Orders.query.filter_by(id=id).one()
        order = structure_orders(order)
        response = jsonify(order)
        response.status_code = 200
        return response
    except exc.SQLAlchemyError as e:
        order = {}
        response = jsonify(order)
        response.status_code = 200
        return response


    
def structure_orders(order):
    return {
        "id" : order.id,
        "product_name" : order.product_id,
        "email" : order.email,
        "phonenumber" : order.phonenumber,
        "location" : order.location,
        "building" : order.building,
        "quantity" : order.quantity
    }
    
    
def create_order(product_id, email, phonenumber, location, building, quantity):
    
    try:
        new_order = Orders(product_id,email,phonenumber,location,building, quantity)
        db.session.add(new_order)
        db.session.commit()
        response = jsonify({"message":"created"})
        response.status_code = 201
        return response
    except exc.SQLAlchemyError as e:
        response = jsonify({"message":"Error occured, order hasnt been added"})
        response.status_code = 201
        return response