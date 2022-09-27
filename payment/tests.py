import json
from django.test import TestCase
from .models import *
from django.test import Client

# Create your tests here.
class AddPayment(TestCase):   
    def test_your_test(self):
        python_dict = {
            
                "input_payname": "8a40135230f21bdb0130f21c255c0007",
                "input_payamount": 999,
                "input_paydate": '2006-10-25',
                "input_paymentchoice": 'cash'
        }
        response = self.client.post('/payment/flu-add-payment/',
                                    json.dumps(python_dict),
                                    content_type="application/json")
        self.assertEqual(response.status_code, 200)

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