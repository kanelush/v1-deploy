from django import forms
from .models import ContactForm


class ContactModelForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = [
            'name', 
            'subject', 
            'description',
            
        ]

