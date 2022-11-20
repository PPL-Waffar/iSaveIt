from audioop import reverse
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from newsletter.forms import NewsletterForm
from newsletter.models import Newsletter
from newsletter.views import add_newsletter

class AddNewsletterTest(TestCase):
    def test_add_newsletter(self):
        file = SimpleUploadedFile(name='ui_logo.jpg', content=open('newsletter/pictures/ui_logo.jpg', 'rb').read(), content_type='image/jpeg')
        response = self.client.post('newsletter/add-newsletter/', {
            'newsletter_text': 'test',
            'newsletter_picture': file,
            'newsletter_category': 'tips',
        })

