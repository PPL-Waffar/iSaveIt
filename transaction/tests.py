from django.test import TestCase
import json

from transaction.models import Transaction

class TransactionTest(TestCase):
    def setup_account(self):
        self.client.post('/user/flu-register-user/',json.dumps({
            'email' : 'test@test.com',
            'name' : 'testwithdjango',
            'password': 'test',
        }),content_type='application/json')

    def test_input_transaction(self):
        self.setup_account()
        session = self.client.session
        session['_auth_user_id'] = 'test@test.com'
        session.save()

        response = self.client.post('/pocket/add-pocket/',json.dumps({
            'session_id' : session.session_key,
            'input_pocketname' : 'testpocket',
            'input_pocketbudget' : 1000,
        }),content_type='application/json')

        response = self.client.post('/transaction/input-transaction/',json.dumps({
            'session_id' : session.session_key,
            'input_transaction_payment_name' : 'warteg',
            'input_transaction_amount' : 200,
            'input_transaction_date' : '2023-05-11',
            'input_transaction_transaction_type' : 'Expense',
            'input_transaction_payment_type' : 'cash',
            'input_transaction_pocket' : 'testpocket',
        }),content_type='application/json')
        self.assertEqual(response.status_code, 200)
