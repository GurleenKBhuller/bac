# contact/forms.py
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField(max_length=500)
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'textarea', 'rows': 3, 'cols': 10}), required=True
    )