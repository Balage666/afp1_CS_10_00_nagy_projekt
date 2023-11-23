from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=150, help_text='', label='Felhasználónév')
    first_name = forms.CharField(label='Keresztnév')
    last_name = forms.CharField(label='Vezetéknév')
    email = forms.EmailField(max_length=254, help_text='', label='Email-cím')
    password1 = forms.CharField( widget=forms.PasswordInput, help_text='', label='Jelszó')
    password2 = forms.CharField( widget=forms.PasswordInput, help_text='', label='Jelszó újra')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')