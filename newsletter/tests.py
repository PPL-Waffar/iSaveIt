
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from newsletter.forms import NewsletterForm
from newsletter.models import Newsletter
from newsletter.views import add_newsletter
from django.urls import reverse

class AddNewsletterTest(TestCase):
    def create_newsletter(self):
        file = SimpleUploadedFile(name='ui_logo.jpg', content=open('newsletter/pictures/ui_logo.jpg', 'rb').read(), content_type='image/jpeg')
        return Newsletter.objects.create(newsletter_text='test', newsletter_picture=file, newsletter_category='tips')   
    def test_add_newsletter(self):
        file = SimpleUploadedFile(name='ui_logo.jpg', content=open('newsletter/pictures/ui_logo.jpg', 'rb').read(), content_type='image/jpeg')
        response = self.client.post('newsletter/add-newsletter/', {
            'newsletter_text': 'test',
            'newsletter_picture': file,
            'newsletter_category': 'tips',
        })
        
    def test_delete_newsletter(self):
        newsletter = self.create_newsletter()
        response = self.client.post(reverse('delete_newsletter', kwargs={'id': newsletter.id}))
        self.assertRedirects(response, '/newsletter/list/', status_code=302)
    
    def test_wrong_delete(self):
        response = self.client.post(reverse('delete_newsletter', kwargs={'id': 1}))
        self.assertEqual(response.status_code, 404)