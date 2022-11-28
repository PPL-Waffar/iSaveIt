import json
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from newsletter.models import Newsletter
from newsletter.views import add_newsletter, view_detail_newsletter

class AddNewsletterTest(TestCase):
    def test_add_newsletter(self):
        test_image = SimpleUploadedFile(name='ui_logo.jpg', content=open('newsletter/pictures/ui_logo.jpg', 'rb').read(), content_type='image/jpeg')
        response = add_newsletter((self.client.post(
            '/add-newsletter/', {
                'newsletter_text': 'test',
                'newsletter_picture': test_image,
                'newsletter_category': 'tips'
                })).wsgi_request)
        self.assertEqual(response.status_code, 200)

    def test_add_newsletter_negative(self):
        test_image = SimpleUploadedFile(name='ui_logo.jpg', content=open('newsletter/pictures/ui_logo.jpg', 'rb').read(), content_type='image/jpeg')
        response = add_newsletter((self.client.post(
            '/add-newsletter/', {
                'newsletter_text': 'test',
                'newsletter_picture': test_image,
                'newsletter_category': 'tips'
                })).wsgi_request)
        self.assertNotEqual(response.status_code, 404)

    def test_view_detail_newsletter(self):
        test_image = SimpleUploadedFile(name='ui_logo.jpg', content=open('newsletter/pictures/ui_logo.jpg', 'rb').read(), content_type='image/jpeg')
        add_newsletter((self.client.post(
            '/add-newsletter/', {
                'newsletter_text': 'test',
                'newsletter_picture': test_image,
                'newsletter_category': 'tips'
                })).wsgi_request)
        newsletter_id = Newsletter.objects.get(newsletter_text='test').id
        response = view_detail_newsletter((self.client.get(
            '/view-detail-newsletter/id=' + str(newsletter_id) + '/')).wsgi_request, newsletter_id)
        self.assertEqual(response.status_code, 200)
    
    def test_view_detail_newsletter_negative(self):
        test_image = SimpleUploadedFile(name='ui_logo.jpg', content=open('newsletter/pictures/ui_logo.jpg', 'rb').read(), content_type='image/jpeg')
        add_newsletter((self.client.post(
            '/add-newsletter/', {
                'newsletter_text': 'test',
                'newsletter_picture': test_image,
                'newsletter_category': 'tips'
                })).wsgi_request)
        newsletter_id = Newsletter.objects.get(newsletter_text='test').id
        response = view_detail_newsletter((self.client.get(
            '/view-detail-newsletter/id=' + str(newsletter_id) + '/')).wsgi_request, newsletter_id)
        self.assertNotEqual(response.status_code, 200)
