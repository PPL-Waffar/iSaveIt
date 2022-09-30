import json
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
    def test_your_test(self):
        python_dict = {
            
                "input_payname": "test payment",
                "input_payamount": 10000,
                "input_paydate": '2022-10-25',
                "input_paymentchoice": 'cash'
        }
        response = self.client.post('/payment/flu-add-payment/',
                                    json.dumps(python_dict),
                                    content_type="application/json")
        response = self.client.get('/payment/flu-get-payment/')
        self.assertEqual(response.status_code, 200)