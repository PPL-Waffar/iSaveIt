from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from newsletter.forms import NewsletterForm

class AddNewsletterTest(TestCase):
    def test_add_newsletter(self):
        file = SimpleUploadedFile(name='ui_logo.jpg', content=open('newsletter/pictures/ui_logo.jpg', 'rb').read(), content_type='image/jpeg')

        post_dict = {
            'newsletter_text': 'This is a test newsletter',
            'newsletter_picture': file,
            'newsletter_category': 'tips',
        }

        form = NewsletterForm(post_dict)
        self.assertEqual(form.is_valid(), True)

    def test_negative_add_newsletter(self):
        file = SimpleUploadedFile(name='ui_logo.jpg', content=open('newsletter/pictures/ui_logo.jpg', 'rb').read(), content_type='image/jpeg')

        post_dict = {
            'newsletter_text': 'This is a test newsletter',
            'newsletter_picture': file,
            'newsletter_category': 'tips',
        }

        form = NewsletterForm(post_dict)

        self.assertNotEqual(form.is_valid(), False)

    def test_add_newsletter_file(self):
        file = SimpleUploadedFile(name='ui_logo.jpg', content=open('newsletter/pictures/ui_logo.jpg', 'rb').read(), content_type='image/jpeg')

        post_dict = {
            'newsletter_text': 'This is a test newsletter',
            'newsletter_picture': file,
            'newsletter_category': 'tips',
        }

        form = NewsletterForm(post_dict)
        
        self.assertEqual(post_dict['newsletter_picture'].name, 'ui_logo.jpg')

