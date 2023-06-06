#!/usr/bin/python3

import unittest
from flask import session
from app import app

class FlaskAppTestCase(unittest.TestCase):
    
    def setUp(self):
        app.testing = True
        app.secret_key = 'test_secret_key'
        self.app = app.test_client()
        with app.test_request_context():
            session['email'] = 'test@example.com'
    
    def test_landing_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Landing Page', response.data)
    
    def test_home_page(self):
        response = self.app.get('/home', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Fresh Basket', response.data)
    
    def test_recipe_page(self):
        response = self.app.get('/recipe')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Frb: Recipe', response.data)
    
    def test_products_page(self):
        response = self.app.get('/products')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Products Page', response.data)
    
    def test_signup_page(self):
        response = self.app.get('/signup')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Sign Up', response.data)
    
    def test_signin_page(self):
        response = self.app.get('/signin')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Sign In', response.data)
    
    def test_profile_page(self):
        response = self.app.get('/profile', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'FRB: Profile', response.data)
    
    def test_signout_page(self):
        response = self.app.get('/signout')
        self.assertEqual(response.status_code, 302)
    
    def test_search_page(self):
        response = self.app.get('/search')
        self.assertEqual(response.status_code, 302)
    
    def test_cart_page(self):
        response = self.app.get('/cart')
        self.assertEqual(response.status_code, 302)
    
    def test_add_to_cart(self):
        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'test@example.com'
            response = client.post('/add_to_cart', data={'product_id': '123'}, follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, {'status': 'success'})
    
    def test_remove_from_cart(self):
        response = self.app.post('/remove_from_cart', data={'product_id': '123'})
        self.assertEqual(response.status_code, 302)
    
    def test_checkout_page(self):
        response = self.app.get('/checkout')
        self.assertEqual(response.status_code, 302)
    
    def test_place_order(self):
        response = self.app.post('/place_order')
        self.assertEqual(response.status_code, 302)


if __name__ == '__main__':
    unittest.main()