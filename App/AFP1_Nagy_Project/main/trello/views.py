from django.shortcuts import render
from django.http import HttpResponse
from .forms import TrelloCardForm
import requests
from django.conf import settings

def create_trello_card(request):
    if request.method == 'POST':
        form = TrelloCardForm(request.POST)
        if form.is_valid():
            card_name = form.cleaned_data['card_name']
            card_description = form.cleaned_data['card_description']

            url = "https://api.trello.com/1/cards"
            params = {
                'key': settings.TRELLO_API_KEY,
                'token': settings.TRELLO_API_TOKEN,
                'name': card_name,
                'desc': card_description
            }

            response = requests.post(url, params=params)

            if response.status_code == 200:
                return HttpResponse("Trello card created successfully!")
            else:
                return HttpResponse("Failed to create Trello card.")
    else:
        form = TrelloCardForm()

    return render(request, 'trello.html', {'form': form})