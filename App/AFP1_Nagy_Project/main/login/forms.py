from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        label="Felhasználónév",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "style": "background-color: #fff; border: none;",
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "style": "background-color: #fff; border: none;",
        }),
        label="Jelszó"
    )