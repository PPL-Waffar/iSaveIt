import json
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from newsletter.models import Newsletter
from newsletter.views import add_newsletter, view_detail_newsletter

image_name = 'ui_logo.jpg'
image_path = 'newsletter/pictures/ui_logo.jpg'
image_type = 'image/jpeg'
add_newsletter_url = '/add-newsletter/'


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
        test_image = SimpleUploadedFile(name=image_name, content=open(image_path, 'rb').read(), content_type=image_type)
        response = add_newsletter((self.client.post(
            add_newsletter_url, {
                'newsletter_text': 'test',
                'newsletter_picture': test_image,
                'newsletter_category': 'tips'
                })).wsgi_request)
        self.assertEqual(response.status_code, 200)

    def test_add_newsletter_negative(self):
        test_image = SimpleUploadedFile(name=image_name, content=open(image_path, 'rb').read(), content_type=image_type)
        response = add_newsletter((self.client.post(
            add_newsletter_url, {
                'newsletter_text': 'test',
                'newsletter_picture': test_image,
                'newsletter_category': 'tips'
                })).wsgi_request)
        self.assertNotEqual(response.status_code, 404)

    def test_view_detail_newsletter(self):
        test_image = SimpleUploadedFile(name=image_name, content=open(image_path, 'rb').read(), content_type=image_type)
        add_newsletter((self.client.post(
            add_newsletter_url, {
                'newsletter_text': 'test',
                'newsletter_picture': test_image,
                'newsletter_category': 'tips'
                })).wsgi_request)
        newsletter_id = Newsletter.objects.get(newsletter_text='test').id
        response = view_detail_newsletter((self.client.get(
            '/view-detail-newsletter/id=' + str(newsletter_id) + '/')).wsgi_request, newsletter_id)
        self.assertEqual(response.status_code, 200)

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

    
    def test_view_detail_newsletter_negative(self):
        test_image = SimpleUploadedFile(name=image_name, content=open(image_path, 'rb').read(), content_type=image_type)
        add_newsletter((self.client.post(
            add_newsletter_url, {
                'newsletter_text': 'test',
                'newsletter_picture': test_image,
                'newsletter_category': 'tips'
                })).wsgi_request)
        newsletter_id = Newsletter.objects.get(newsletter_text='test').id
        response = view_detail_newsletter((self.client.get(
            '/view-detail-newsletter/id=' + str(newsletter_id) + '/')).wsgi_request, newsletter_id)
        self.assertNotEqual(response.status_code, 404)