from django import forms
from .models import Request, Contact

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = '__all__'
        labels = {
            "hming": "",
            "phone_number": "",
            "email": "",
            "domain": "",
            "types": "",
        }
        widgets = {
            "hming": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Name"
            }),
            "phone_number": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Phone number"
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Email"
            }),
            "domain": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Domain name(if you have)"
            }),
            "types": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Type of website would you like."
            })
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        labels = {
            "email": "",
            "title": "",
            "message": "",
        }
        widgets = {
            "email": forms.EmailInput(attrs={
                "class": "input-group mb-3",
                "placeholder": "Email"
            }),
            "title": forms.TextInput(attrs={
                "class": "input-group mb-3",
                "placeholder": "Message title"
            }),
            "message": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Message here"
            })
        }



