from django import forms
from . import models


class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Support
        fields = ['name', 'email', 'message']




