from cgi import test
import json
from django.test import TestCase

from pocket.views import add_pocket

content_type = 'application/json'
add_pocket_url = '/pocket/add-pocket/'

class ViewFinancialReportTest(TestCase):
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

    def test_viewfinancialreport(self):
        self.setup_account()
        session = self.client.session
        session['_auth_user_id'] = 'test@test.com'
        session.save()

        self.client.post(add_pocket_url,json.dumps({
            'session_id' : session.session_key,
            'input_pocketname' : 'testpocket',
            'input_pocketbudget' : 1000,
        }),content_type=content_type)

        self.client.post(add_pocket_url,json.dumps({
            'session_id' : session.session_key,
            'input_pocketname' : 'testpocket2',
            'input_pocketbudget' : 2000,
        }),content_type=content_type)

        self.client.post(add_pocket_url,json.dumps({
            'session_id' : session.session_key,
            'input_pocketname' : 'testpocket3',
            'input_pocketbudget' : 3000,
        }),content_type=content_type)

        self.client.post('/expense/add-expense/',json.dumps({
            'session_id' : session.session_key,
            'expense_name' : 'test',
            'expense_amount' : 1000,
            'expense_date' : '2021-01-03',
            'expense_type' : 'Lend Money',
            'expense_person' : 'raka',
            'expense_payment_choice' : 'Cash',
            'expense_pocket' : 'testpocket',
        }),content_type=content_type)

        self.client.post('/expense/add-expense/',json.dumps({
            'session_id' : session.session_key,
            'expense_name' : 'test2',
            'expense_amount' : 2000,
            'expense_date' : '2021-01-02',
            'expense_type' : 'Debt',
            'expense_person' : 'raka2',
            'expense_payment_choice' : 'Cash',
            'expense_pocket' : 'testpocket',
        }),content_type=content_type)

        response = self.client.get('/financialreport/view-financial-report/',{
            'session_id': session.session_key,
        })

        self.assertEqual(json.loads(response.content)['total_income'], '"Rp 0"')
        self.assertEqual(response.status_code,200)

        #negative tests
        self.assertNotEqual(json.loads(response.content)['total_income'], 5000)
        self.assertNotEqual(response.status_code,400)


