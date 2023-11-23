from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Felhasználónév')
    password = forms.CharField(widget=forms.PasswordInput, label='Jelszó')
    pass