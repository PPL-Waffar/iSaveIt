from newsletter.models import Newsletter
from django import forms


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        #required fields
        fields = ['newsletter_text', 'newsletter_picture', 'newsletter_category']
        labels = {
            'newsletter_text': 'Text',
            'newsletter_picture': 'Picture',
            'newsletter_category': 'Category',
        }
        #help text for the fields
        help_texts = {
            'newsletter_text': 'Enter the text for the newsletter',
            'newsletter_picture': 'Upload a picture for the newsletter',
            'newsletter_category': 'Select the category for the newsletter',
        }
        #error messages for the fields
        error_messages = {
            'newsletter_text': {
                'max_length': 'The text is too long',
            },
        }

