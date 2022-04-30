import os
import enum
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql.json import JSONB
from app.app import db

class Orders(db.Model):
    '''
    This class represents the lca orders table.
    '''

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    email = db.Column(db.String(255))
    phonenumber = db.Column(db.String(255))
    location = db.Column(db.String(255))
    building = db.Column(db.String(255))
    quantity = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime)
    
    def __init__(self, product_id,email,phonenumber,location,building, quantity):
        
        self.product_id = product_id
        self.email = email
        self.phonenumber = phonenumber
        self.location = location
        self.building = building
        self.quantity = quantity

    def __repr__(self):
        return "<Orders: {}>".format(self.id)
    
    