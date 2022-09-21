from django import forms
from .models import Pocket

class PocketForm(forms.ModelForm):
    class Meta:
        model = Pocket
        fields = "__all__"
