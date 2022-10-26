from django.test import TestCase
import json
# Create your tests here.
class EditAccountTest(TestCase):
    def setup_account(self):
        self.client.post('/user/flu-register-user/',json.dumps({
            'email' : 'test@test.com',
            'name' : 'testwithdjango',
            'password': 'test',
        }),content_type='application/json')
    def edit_account(self):

        self.setup_account()
        session = self.client.session
        session['_auth_user_id'] = 'test@test.com'
        session.save()
        response = self.client.post('/user/flu-edit-profile/',json.dumps({
            'session_id' : session.session_key,
            'name' : 'testpocket',
            'password' : 'awe',
        }),content_type='application/json')
        self.assertEqual(response.status_code, 200)
