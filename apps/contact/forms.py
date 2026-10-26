from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "subject", "message"]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Your full name",
                    "autocomplete": "name",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "placeholder": "you@example.com",
                    "autocomplete": "email",
                }
            ),
            "subject": forms.TextInput(
                attrs={
                    "placeholder": "What is your message about?",
                }
            ),
            "message": forms.Textarea(
                attrs={
                    "placeholder": "Write your message here...",
                    "rows": 6,
                }
            ),
        }