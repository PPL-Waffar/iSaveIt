from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from newsletter.views import add_newsletter

class AddNewsletterTest(TestCase):
    def test_add_newsletter(self):
        file = SimpleUploadedFile(name='ui_logo.jpg', content=open('newsletter/pictures/ui_logo.jpg', 'rb').read(), content_type='image/jpeg')
        response = add_newsletter((self.client.post(
            '/add-newsletter/', {
                'newsletter_text': 'test',
                'newsletter_picture': file,
                'newsletter_category': 'tips'
                })).wsgi_request)
        self.assertEqual(response.status_code, 200)

    def test_add_newsletter(self):
        file = SimpleUploadedFile(name='ui_logo.jpg', content=open('newsletter/pictures/ui_logo.jpg', 'rb').read(), content_type='image/jpeg')
        response = add_newsletter((self.client.post(
            '/add-newsletter/', {
                'newsletter_text': 'test',
                'newsletter_picture': file,
                'newsletter_category': 'tips'
                })).wsgi_request)
        self.assertNotEqual(response.status_code, 404)