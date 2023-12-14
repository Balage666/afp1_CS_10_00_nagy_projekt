from django import forms

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
    

