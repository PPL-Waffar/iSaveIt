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

class GetPocketTest(TestCase):
    def setup_account(self):
        self.client.post('/user/flu-register-user/',json.dumps({
            'email' : 'test@test.com',
            'name' : 'testwithdjango',
            'password': 'test',
        }),content_type='application/json')

    def test_getpocket(self):
        self.setup_account()
        session = self.client.session
        session['_auth_user_id'] = 'test@test.com'
        session.save()

        response = self.client.post('/pocket/add-pocket/',json.dumps({
            'session_id' : session.session_key,
            'input_pocketname' : 'testpocket',
            'input_pocketbudget' : 1000,
        }),content_type='application/json')


        response = self.client.post('/pocket/add-pocket/',json.dumps({
            'session_id' : session.session_key,
            'input_pocketname' : 'testpocket2',
            'input_pocketbudget' : 2000,
        }),content_type='application/json')

        response = self.client.get('/pocket/get-pocket/',{
            'session_id': session.session_key,
        })

        self.assertEqual(response.status_code, 200)

class DeletePocketTest(TestCase):
    def setup_account(self):
        self.client.post('/user/flu-register-user/',json.dumps({
            'email' : 'test@test.com',
            'name' : 'testwithdjango',
            'password': 'test',
        }),content_type='application/json')

    def test_delete_pocket(self):
        self.setup_account()
        session = self.client.session
        session['_auth_user_id'] = 'test@test.com'
        session.save()

        response = self.client.post('/pocket/add-pocket/',json.dumps({
            'session_id': session.session_key,
            'input_pocketname' : 'testpocket',
            'input_pocketbudget' : 1000,
        }),content_type='application/json')

        response = self.client.delete('/pocket/delete-pocket/',json.dumps({
            'session_id': session.session_key,
        }),content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        

class EditPocketTest(TestCase):
    def setup_account(self):
        self.client.post('/user/flu-register-user/',json.dumps({
            'email' : 'test@test.com',
            'name' : 'testwithdjango',
            'password': 'test',
        }),content_type='application/json')

    def test_edit_pocket(self):
        self.setup_account()
        session = self.client.session
        session['_auth_user_id'] = 'test@test.com'
        session.save()

        response = self.client.post('/pocket/add-pocket/',json.dumps({
            'session_id': session.session_key,
            'input_pocketname' : 'testpocket',
            'input_pocketbudget' : 1000,
        }),content_type='application/json')

        response = self.client.post('/pocket/update-pocket/',json.dumps({
            'session_id': session.session_key,
            'input_pocketname' : 'testpocket',
            'input_pocketbudget' : 3000,
        }),content_type='application/json')

class TotalPocketTest(TestCase):
    def setup_account(self):
        self.client.post('/user/flu-register-user/',json.dumps({
            'email' : 'test@test.com',
            'name' : 'testwithdjango',
            'password': 'test',
        }),content_type='application/json')

    def test_total_pocket(self):
        self.setup_account()
        session = self.client.session
        session['_auth_user_id'] = 'test@test.com'
        session.save()

        self.client.post('/pocket/add-pocket/',json.dumps({
            'session_id': session.session_key,
            'input_pocketname' : 'testpocket',
            'input_pocketbudget' : 1000,
        }),content_type='application/json')

        self.client.post('/pocket/add-pocket/',json.dumps({
            'session_id': session.session_key,
            'input_pocketname' : 'testpocket2',
            'input_pocketbudget' : 2000,
        }),content_type='application/json')

        self.client.post('/pocket/add-pocket/',json.dumps({
            'session_id': session.session_key,
            'input_pocketname' : 'testpocket3',
            'input_pocketbudget' : 3000,
        }),content_type='application/json')

        print('test')

        response = self.client.get('/pocket/total-pocket/',{
            'session_id': session.session_key,
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content)['total_pocket_budget'], 6000)