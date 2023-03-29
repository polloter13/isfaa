from django.forms import ModelForm, TextInput, EmailInput
from .models import Message


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={
                'class': 'name-input',
                'placeholder': 'Ad',
            }),
            'email': EmailInput(attrs={
                'class': 'email-input',
                'placeholder': 'E-poçt',
            }),
        }
