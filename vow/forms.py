from django import forms
from.models import customers, Agent, VOW
from django.contrib.auth.forms import AuthenticationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from datetime import date

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)

class CustomerUpdateForm(forms.ModelForm):
    class Meta:
        model = customers
        fields = [
            'name',
            'age',
            'agent',
            'email',
            'classes',
        ]
        labels = {
            'agent': 'staff'
        }

class VowUpdateForm(forms.ModelForm):
    class Meta:
        model = VOW
        fields = (
            'Affirmation',
            'agent',
            'date',
        ) 