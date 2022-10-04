import json
from urllib import response
from django.test import TestCase
from .models import Payment
from django.test import Client

class AddPayment(TestCase):   
    def setup_account(self):
        self.client.post('/user/flu-register-user/',json.dumps({
            'email' : 'test@test.com',
            'name' : 'testwithdjango',
            'password': 'test',
        }),content_type='application/json')

    def test_addpayment(self):
        self.setup_account()
        session = self.client.session
        session['_auth_user_id'] = 'test@test.com'
        session.save()

        response = self.client.post('/payment/flu-add-payment/',json.dumps({
            'session_id': session.session_key,
            'input_payname': 'test',
            'input_payamount': '100',
            'input_paydate': '2020-01-01',
            'input_paymentchoice': 'cash'
        }),content_type='application/json')
        self.assertEqual(response.status_code,200)

class GetPayment(TestCase):
    def setup_account(self):
        self.client.post('/user/flu-register-user/',json.dumps({
            'email' : 'test@test.com',
            'name' : 'testwithdjango',
            'password': 'test',
        }),content_type='application/json')
    
    def test_getpayment(self):
        self.setup_account()
        session = self.client.session
        session['_auth_user_id'] = 'test@test.com'
        session.save()

        response = self.client.post('/payment/flu-add-payment/',json.dumps({
            'session_id': session.session_key,
            'input_payname': 'test',
            'input_payamount': '100',
            'input_paydate': '2020-01-01',
            'input_paymentchoice': 'cash'
        }),content_type='application/json')

        response = self.client.post('/payment/flu-add-payment/',json.dumps({
            'session_id': session.session_key,
            'input_payname': 'test2',
            'input_payamount': '1002',
            'input_paydate': '2022-01-01',
            'input_paymentchoice': 'cash'
        }),content_type='application/json')

        response = self.client.get('/payment/flu-get-payment/',{
            'session_id': session.session_key,
        })

        self.assertEqual(response.status_code,200)

class UpdatePayment(TestCase):
    def setup_account(self):
        self.client.post('/user/flu-register-user/',json.dumps({
            'email' : 'test@test.com',
            'name' : 'testwithdjango',
            'password': 'test',
        }),content_type='application/json')
    
    def test_updatepayment(self):
        self.setup_account()
        session = self.client.session
        session['_auth_user_id'] = 'test@test.com'
        session.save()

        response = self.client.post('/payment/flu-add-payment/',json.dumps({
            'session_id': session.session_key,
            'input_payname': 'test',
            'input_payamount': '100',
            'input_paydate': '2020-01-01',
            'input_paymentchoice': 'cash'
        }),content_type='application/json')

        response = self.client.post('/payment/flu-update-payment/',json.dumps({
            'session_id': session.session_key,
            'input_payname': 'test',
            'input_payamount': '1002',
            'input_paydate': '2023-02-03',
            'input_paymentchoice': 'cash',
        }),content_type='application/json')

        self.assertEqual(response.status_code,200)

class DeletePayment(TestCase):
    def setup_account(self):
        self.client.post('/user/flu-register-user/',json.dumps({
            'email' : 'test@test.com',
            'name' : 'testwithdjango',
            'password': 'test',
        }),content_type='application/json')

    
    def test_deletepayment(self):
        self.setup_account()
        session = self.client.session
        session['_auth_user_id'] = 'test@test.com'
        session.save()

        response = self.client.post('/payment/flu-add-payment/',json.dumps({
            'session_id': session.session_key,
            'input_payname': 'test',
            'input_payamount': '100',
            'input_paydate': '2020-01-01',
            'input_paymentchoice': 'cash'
        }),content_type='application/json')

        #delete payment using http method delete
        response = self.client.delete('/payment/flu-delete-payment/',json.dumps({
            'session_id': session.session_key,
            'input_payname': 'test',
        }),content_type='application/json')

        self.assertEqual(response.status_code,200)
