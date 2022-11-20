from newsletter.models import Newsletter
from django import forms


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ('__all__')