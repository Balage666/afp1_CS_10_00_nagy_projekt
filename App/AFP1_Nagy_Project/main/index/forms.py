from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm as DjangoPasswordChangeForm

class UserProfileForm(forms.ModelForm):

    username = forms.CharField(
        max_length=150,
        help_text="",
        label="Felhasználónév",
        
    )
    first_name = forms.CharField(
        label="Keresztnév",
    )
    last_name = forms.CharField(
        label="Vezetéknév",
    )
    email = forms.EmailField(
        max_length=254,
        help_text="",
        label="Email-cím",
    )


    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
        )


class CustomPasswordChangeForm(DjangoPasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(CustomPasswordChangeForm, self).__init__(*args, **kwargs)
        
        self.fields['new_password1'] = forms.CharField(
            widget=forms.PasswordInput(),
            help_text="",
            label="Új jelszó"
        )

        self.fields['new_password2'] = forms.CharField(
            widget=forms.PasswordInput(),
            help_text="",
            label="Új jelszó mégegyszer"
        )

        self.fields['old_password'] = forms.CharField(
            widget=forms.PasswordInput(),
            help_text="",
            label="Régi jelszó"
        )

    class Meta:
        model = User
        fields = (
            "old_password",
            "new_password1",
            "new_password2",
        )



