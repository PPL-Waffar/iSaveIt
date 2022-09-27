import json
from urllib import response
from django.test import TestCase
from .models import Pocket

class AddPocketTest(TestCase):
    def test_add_pocket(self):
        data = {'pocket_name': 'test_pocket', 'pocket_budget': 100}
        response = self.client.post('/pocket/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'isSuccessful': True})

class DeletePocketTest(TestCase):
    def create_pocket(self):
        pocket = Pocket.objects.create(pocket_name='transportation', pocket_budget=300000)
        return pocket
    
    def test_delete_pocket(self):
        pocket = self.create_pocket()
        pk = pocket.pk
        self.assertTrue(Pocket.objects.filter(pk=pk).exists())
        data = {'primary_key': pk}
        response = self.client.post('/pocket/delete/', json.dumps(data), content_type='application/json')
        self.assertFalse(Pocket.objects.filter(pk=pk).exists())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'isSuccessful': True})

class EditPocketTest(TestCase):
    def create_pocket(self):
        pocket = Pocket.objects.create(pocket_name='transportation', pocket_budget=300000)
        return pocket
    
    def test_edit_pocket(self):
        pocket = self.create_pocket()
        pk = pocket.pk
        self.assertTrue(Pocket.objects.filter(pk=pk).exists())
        data = {'primary_key': pk, 'pocket_name': 'food', 'pocket_budget': 900000}
        response = self.client.post('/pocket/edit/', json.dumps(data), content_type='application/json')
        pocket = Pocket.objects.get(pk=pk)
        self.assertEqual(pocket.pocket_name, 'food')
        self.assertEqual(pocket.pocket_budget, 900000)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'isSuccessful': True})


        
