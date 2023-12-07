from django import forms
from .models import Contact

# to include 3 fields
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'notes'] 

