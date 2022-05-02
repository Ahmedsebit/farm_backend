import json
import unittest
from pathlib import Path
from app.app import create_app, db
from app.models.products import Products
from app.models.orders import Orders


class ModelsTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.file = open(Path('tests/istockphoto-467346706-612x612.jpeg'), 'rb')
        
        with self.app.app_context():
            db.session.close()
            db.drop_all()
            db.create_all()
        
    def add_product(self):
        product = Products("Egg plant", "Egg plant", "2022-04-30 17:05:58.826019.pdf", 10.0)
        db.session.add(product)
        db.session.commit()
        
        
    def add_orders(self):
        orders = Orders(1, "ahmedamedy@gmail.com", "254701874389", "Nairobi Olympic Estate", "h17", 5)
        db.session.add(orders)
        db.session.commit()
        
           
    def test_add_products(self):

        headers = {'Content-type': 'application/json'}
        data = dict(
                    name = "test_name.jpeg",
                    description = "testing transporter name",
                    price = "testing one",
                    file = self.file
                    )
        response = self.client().post('/api/farm_backend/v1/products', 
                                        data = data,
                                        headers = headers
                                    )
        self.assertEqual(201, response.status_code)
        
    
    def test_add_products_invalid_name(self):
    
        headers = {'Content-type': 'application/json'}
        response = self.client().post('/api/farm_backend/v1/products', 
                                        data = dict(
                                                    description = "testing transporter name",
                                                    price = "testing one",
                                                    file = self.file
                                                    ),
                                        headers = headers
                                    )
        self.assertEqual(400, response.status_code)
        
    
    def test_add_products_invalid_description(self):
    
        headers = {'Content-type': 'application/json'}
        response = self.client().post('/api/farm_backend/v1/products', 
                                        data = dict(
                                                    name = "test_name.jpeg",
                                                    price = "testing one",
                                                    file = self.file
                                                    ),
                                        headers = headers
                                    )
        self.assertEqual(400, response.status_code)
        
        
    def test_add_products_invalid_price(self):
    
        headers = {'Content-type': 'application/json'}
        response = self.client().post('/api/farm_backend/v1/products', 
                                        data = dict(
                                                    name = "test_name.jpeg",
                                                    description = "testing transporter name",
                                                    file = self.file
                                                    ),
                                        headers = headers
                                    )
        self.assertEqual(400, response.status_code)
        
    
    def test_add_products_invalid_file(self):
    
        headers = {'Content-type': 'application/json'}
        response = self.client().post('/api/farm_backend/v1/products', 
                                        data = dict(
                                                    name = "test_name.jpeg",
                                                    description = "testing transporter name",
                                                    price = "testing one"
                                                    ),
                                        headers = headers
                                    )
        self.assertEqual(400, response.status_code)
        
          
    def test_get_products(self):
        
        self.add_product()
        headers = {'Content-type': 'application/json'}

        response = self.client().get('/api/farm_backend/v1/products', headers=headers)
        self.assertEqual(200, response.status_code)
    
    
    
    def test_get_product(self):
        
        self.add_product()
        headers = {'Content-type': 'application/json'}
        response = self.client().get('/api/farm_backend/v1/products/1', headers=headers)
        self.assertEqual(200, response.status_code)
        
    
    def test_add_oders(self):
        
        headers = {'Content-type': 'application/json'}
        response = self.client().post('/api/farm_backend/v1/orders', 
                                        data = {
                                                "product_id":1,
                                                "email":"ahmedamedy@gmail.com",
                                                "phonenumber":"254701874389",
                                                "location":"Nairobi Olympic Estate",
                                                "building":"h17",
                                                "quantity":5,
                                        },
                                        headers = headers
                                    )
        self.assertEqual(201, response.status_code)
        
    
    def test_add_oders_missing_product_id(self):
        
        headers = {'Content-type': 'application/json'}
        response = self.client().post('/api/farm_backend/v1/orders', 
                                        data = {
                                                "email":"ahmedamedy@gmail.com",
                                                "phonenumber":"254701874389",
                                                "location":"Nairobi Olympic Estate",
                                                "building":"h17",
                                                "quantity":5,
                                        },
                                        headers = headers
                                    )
        self.assertEqual(400, response.status_code)
        
        
    def test_add_oders_missing_email(self):
        
        headers = {'Content-type': 'application/json'}
        response = self.client().post('/api/farm_backend/v1/orders', 
                                        data = {
                                                "product_id":1,
                                                "phonenumber":"254701874389",
                                                "location":"Nairobi Olympic Estate",
                                                "building":"h17",
                                                "quantity":5,
                                        },
                                        headers = headers
                                    )
        self.assertEqual(400, response.status_code)
        
        
    def test_add_oders_missing_location(self):
        
        headers = {'Content-type': 'application/json'}
        response = self.client().post('/api/farm_backend/v1/orders', 
                                        data = {
                                                "product_id":1,
                                                "email":"ahmedamedy@gmail.com",
                                                "phonenumber":"254701874389",
                                                "building":"h17",
                                                "quantity":5,
                                        },
                                        headers = headers
                                    )
        self.assertEqual(400, response.status_code)
        
        
    def test_add_oders_missing_phone_number(self):
        
        headers = {'Content-type': 'application/json'}
        response = self.client().post('/api/farm_backend/v1/orders', 
                                        data = {
                                                "product_id":1,
                                                "email":"ahmedamedy@gmail.com",
                                                "location":"Nairobi Olympic Estate",
                                                "building":"h17",
                                                "quantity":5,
                                        },
                                        headers = headers
                                    )
        self.assertEqual(400, response.status_code)


    def test_add_oders_missing_building(self):
        
        headers = {'Content-type': 'application/json'}
        response = self.client().post('/api/farm_backend/v1/orders', 
                                        data = {
                                                "product_id":1,
                                                "email":"ahmedamedy@gmail.com",
                                                "phonenumber":"254701874389",
                                                "location":"Nairobi Olympic Estate",
                                                "quantity":5,
                                        },
                                        headers = headers
                                    )
        self.assertEqual(400, response.status_code)
        
        
    def test_add_oders_missing_quantity(self):
        
        headers = {'Content-type': 'application/json'}
        response = self.client().post('/api/farm_backend/v1/orders', 
                                        data = {
                                                "product_id":1,
                                                "email":"ahmedamedy@gmail.com",
                                                "phonenumber":"254701874389",
                                                "location":"Nairobi Olympic Estate",
                                                "building":"h17",
                                        },
                                        headers = headers
                                    )
        self.assertEqual(400, response.status_code)
        
        
        
    def test_get_user_orders(self):
        self.add_product()
        self.add_orders()
        headers = {'Content-type': 'application/json'}

        response = self.client().get('/api/farm_backend/v1/orders/user/ahmedamedy@gmail.com', headers=headers)
        self.assertEqual(200, response.status_code)
    
    
    def test_get_order(self):

        headers = {'Content-type': 'application/json'}

        response = self.client().get('/api/farm_backend/v1/orders/1', headers=headers)
        self.assertEqual(200, response.status_code)