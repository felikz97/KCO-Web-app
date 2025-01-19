from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usar

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Usar
        fields = ['username', 'name',  'email', 'Adm',  'password1', 'password2']