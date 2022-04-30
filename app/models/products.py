import os
import enum
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql.json import JSONB
from app.app import db

class Products(db.Model):
    '''
    This class represents the lca products table.
    '''

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))
    image_url = db.Column(db.String(255))
    price = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime)
    
    def __init__(self, name, description, image_url, price):
        
        self.name = name
        self.description = description
        self.image_url = image_url
        self.price = price

    def __repr__(self):
        return "<Products: {}>".format(self.id)
    
    