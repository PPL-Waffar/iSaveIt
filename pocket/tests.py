import json
from django.test import TestCase
class AddPocketTest(TestCase):
    def setup_account(self):
        self.client.post('/user/flu-register-user/',json.dumps({
            'email' : 'test@test.com',
            'name' : 'testwithdjango',
            'password': 'test',
        }),content_type='application/json')

    def test_addpocket(self):
        self.setup_account()
        session = self.client.session
        session['_auth_user_id'] = 'test@test.com'
        session.save()

        response = self.client.post('/pocket/add-pocket/',json.dumps({
            'session_id' : session.session_key,
            'input_pocketname' : 'testpocket',
            'input_pocketbudget' : 1000,
        }),content_type='application/json')

        self.assertEqual(response.status_code, 200)
