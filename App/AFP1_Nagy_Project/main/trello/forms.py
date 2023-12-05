from django import forms

class TrelloCardForm(forms.Form):
    card_name = forms.CharField(label='Card Name', max_length=255)
    card_description = forms.CharField(label='Card Description', widget=forms.Textarea)