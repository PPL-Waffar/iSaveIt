import json
from django.test import TestCase

class AddPocketTest(TestCase):
    def test_add_pocket(self):
        data = {'pocket_name': 'test_pocket', 'pocket_budget': 100}
        response = self.client.post('/pocket/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'isSuccessful': True})

