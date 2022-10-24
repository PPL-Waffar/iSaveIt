import json
from django.test import TestCase

content_type = 'application/json'

class GetExpense(TestCase):
    def setup_account(self):
        self.client.post('/user/flu-register-user/',json.dumps({
            'email' : 'test@test.com',
            'name' : 'testwithdjango',
            'password': 'test',
        }),content_type=content_type)

        self.client.post('/user/flu-register-user/',json.dumps({
            'email' : 'test2@test.com',
            'name' : 'test2withdjango',
            'password': 'test2',
        }),content_type=content_type)

    def test_getexpense(self):
        self.setup_account()
        session = self.client.session
        session['_auth_user_id'] = 'test@test.com'
        session.save()

        self.client.post('/pocket/add-pocket/',json.dumps({
            'session_id' : session.session_key,
            'input_pocketname' : 'testpocket',
            'input_pocketbudget' : 1000,
        }),content_type=content_type)

        self.client.post('/expense/add-expense/',json.dumps({
            'session_id' : session.session_key,
            'expense_name' : 'test',
            'expense_amount' : 100,
            'expense_date' : '2021-01-01',
            'expense_type' : 'Lend Money',
            'expense_person' : 'raka',
            'expense_payment_choice' : 'Cash',
            'expense_pocket' : 'testpocket',
        }),content_type=content_type)

        self.client.post('/expense/add-expense/',json.dumps({
            'session_id' : session.session_key,
            'expense_name' : 'test2',
            'expense_amount' : 1002,
            'expense_date' : '2021-01-02',
            'expense_type' : 'Debt',
            'expense_person' : 'raka2',
            'expense_payment_choice' : 'Cash',
            'expense_pocket' : 'testpocket',
        }),content_type=content_type)

        response = self.client.get('/expense/view-expense/',{
            'session_id': session.session_key,
        })

        self.assertEqual(response.status_code,200)
    
    def test_failedgetexpense(self):
        self.setup_account()
        session = self.client.session
        session['_auth_user_id'] = 'test@test.com'
        session.save()

        self.client.post('/pocket/add-pocket/',json.dumps({
            'session_id' : session.session_key,
            'input_pocketname' : 'testpocket',
            'input_pocketbudget' : 1000,
        }),content_type=content_type)

        self.client.post('/expense/add-expense/',json.dumps({
            'session_id' : session.session_key,
            'expense_name' : 'test',
            'expense_amount' : 100,
            'expense_date' : '2021-01-01',
            'expense_type' : 'Lend Money',
            'expense_person' : 'raka',
            'expense_payment_choice' : 'Cash',
            'expense_pocket' : 'testpocket',
        }),content_type=content_type)

        self.client.post('/expense/add-expense/',json.dumps({
            'session_id' : session.session_key,
            'expense_name' : 'test2',
            'expense_amount' : 1002,
            'expense_date' : '2021-01-02',
            'expense_type' : 'Debt',
            'expense_person' : 'raka2',
            'expense_payment_choice' : 'Cash',
            'expense_pocket' : 'testpocket',
        }),content_type=content_type)

        response = self.client.get('/expense/view-expense/',{
            'session_id': session.session_key,
        })

        session = self.client.session
        session['_auth_user_id'] = 'test2@test.com'
        session.save()

        self.client.post('/pocket/add-pocket/',json.dumps({
            'session_id' : session.session_key,
            'input_pocketname' : 'testpocket2',
            'input_pocketbudget' : 1000,
        }),content_type=content_type)

        response2 = self.client.get('/expense/view-expense/',{
            'session_id': session.session_key,
        })
        
        self.assertNotEqual(response2.content,response.content)