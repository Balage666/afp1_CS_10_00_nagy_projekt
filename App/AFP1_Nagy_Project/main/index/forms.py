from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm as DjangoPasswordChangeForm

class TrelloCardForm(forms.Form):
    card_name = forms.CharField(label='A kártya neve', max_length=255, required=True)
    card_description = forms.CharField(label='A kártya leírása:', widget=forms.Textarea,required=True)
    

class CreateListForm(forms.Form):
   list_name = forms.CharField(label='A lista neve:', max_length=255, required=True)

class ChangeCardLocationForm(forms.Form):
    list_id = forms.ChoiceField(choices=[], label='Lista neve')
    card_id = forms.ChoiceField(choices=[], label='Kártya neve')

    def __init__(self, *args, **kwargs):
        lists = kwargs.pop('lists', [])
        cards = kwargs.pop('cards', [])
        super(ChangeCardLocationForm, self).__init__(*args, **kwargs)
        self.fields['list_id'].choices = lists
        self.fields['card_id'].choices = cards
    
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
