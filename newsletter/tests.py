
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from newsletter.views import add_newsletter
from django.urls import reverse

class AddNewsletterTest(TestCase):
    def create_newsletter(self):
        file = SimpleUploadedFile(name='ui_logo.jpg', content=open('newsletter/pictures/ui_logo.jpg', 'rb').read(), content_type='image/jpeg')
        response = self.client.post('newsletter/add-newsletter/', {
            'newsletter_text': 'test',
            'newsletter_picture': file,
            'newsletter_category': 'tips',
        })
        

    def test_get_list_newsletter(self):
        
        new_picture = SimpleUploadedFile(name='ui_logo.jpg', content=open('newsletter/pictures/ui_logo.jpg', 'rb').read(), content_type='image/jpeg')
        return Newsletter.objects.create(newsletter_text='test', newsletter_picture=file, newsletter_category='tips')   
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
        file = SimpleUploadedFile(name='ui_logo.jpg', content=open('newsletter/pictures/ui_logo.jpg', 'rb').read(), content_type='image/jpeg')
        response = self.client.post('newsletter/add-newsletter/', {
            'newsletter_text': 'test',
            'newsletter_picture': new_picture,
            'newsletter_category': 'tips',
        })
        
    def test_delete_newsletter(self):
        newsletter = self.create_newsletter()
        response = self.client.post(reverse('delete_newsletter', kwargs={'id': newsletter.id}))
        self.assertRedirects(response, '/newsletter/list/', status_code=302)
    
    def test_wrong_delete(self):
        response = self.client.post(reverse('delete_newsletter', kwargs={'id': 1}))
        self.assertNotEqual(response.status_code, 200)
