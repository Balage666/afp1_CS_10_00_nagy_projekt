from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.http import HttpResponse
from .forms import TrelloCardForm
from .forms import CreateListForm
from .forms import ChangeCardLocationForm
import requests
from .settings_api import TRELLO_API_KEY,TRELLO_API_TOKEN,BOARD_ID
from .forms import UserProfileForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from .forms import CustomPasswordChangeForm

@login_required(redirect_field_name="bejelentkezes_szukseges")
def index(request):
    message = request.GET.get('message', None)
    if (message):
        return render(request, 'index.html', {'message': message})
    else:
        return render(request, 'index.html')

@login_required(redirect_field_name="bejelentkezes_szukseges")
def documentation(request):
    message = request.GET.get('message', None)
    if (message):
        return render(request, 'documentation.html', {'message': message})
    else:
        return render(request, 'documentation.html')

@login_required(redirect_field_name="bejelentkezes_szukseges")
def trello_cards(request):
    message = request.GET.get('message', None)
    if (message):
        return render(request, 'trello_cards.html', {'message': message})
    else:
        return render(request, 'trello_cards.html')

@login_required(redirect_field_name="bejelentkezes_szukseges")
def code(request):
    message = request.GET.get('message', None)
    if (message):
        return render(request, 'code.html', {'message': message})
    else:
        return render(request, 'code.html')

@login_required(redirect_field_name="bejelentkezes_szukseges")
def profile(request):
    message = request.GET.get('message', None)
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user)

    return render(request, 'profile.html', {'form': form})
    if (message):
        return render(request, 'profile.html', {'message': message})
    else:
        return render(request, 'profile.html') 

@login_required(redirect_field_name="bejelentkezes_szukseges")
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(redirect_field_name="bejelentkezes_szukseges")
def create_trello_card(request):
    form = TrelloCardForm()
    if request.method == 'POST':
        form = TrelloCardForm(request.POST)
        card_name = form.data['card_name']
        card_description = form.data['card_description']
        
        url = f"https://api.trello.com/1/cards?key={TRELLO_API_KEY}&token={TRELLO_API_TOKEN}&name={card_name}&desc={card_description}&idList={get_default_list_id(BOARD_ID,TRELLO_API_KEY,TRELLO_API_TOKEN)}"

        response = requests.post(url)

        if response.status_code == 200:
            return HttpResponse("Trello card created successfully!")
        else:
            return HttpResponse(response.status_code)
    else:
        form = TrelloCardForm()

    return render(request, 'trello.html', {'form': form})
        
def get_trello_lists(board_id, api_key, api_token):

    url = f"https://api.trello.com/1/boards/{board_id}/lists"
    params = {'id':board_id,'key': api_key, 'token': api_token}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        trello_lists = response.json()
        choices = [(trello_list['id'], trello_list['name']) for trello_list in trello_lists]
        return choices
    else:
        return []

def get_default_list_id(board_id,api_key,api_token):
    
    url = f"https://api.trello.com/1/boards/{board_id}/lists"
    params = {'id':board_id,'key': api_key, 'token': api_token}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        trello_lists = response.json()
        if trello_lists:
            first_list_id = trello_lists[0]['id']
            return first_list_id
    else:
        return []
    
def get_trello_cards(board_id, api_key, api_token):

    url = f"https://api.trello.com/1/boards/{board_id}/cards"
    params = {'id':board_id,'key': api_key, 'token': api_token}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        trello_lists = response.json()
        choices_cards = [(trello_list['id'], trello_list['name']) for trello_list in trello_lists]
        return choices_cards
    else:
        return []
    
@login_required(redirect_field_name="bejelentkezes_szukseges")
def move_cards(request):
    form = ChangeCardLocationForm()
    if request.method == 'GET':
        lists = get_trello_lists(BOARD_ID, TRELLO_API_KEY, TRELLO_API_TOKEN)
        cards = get_trello_cards(BOARD_ID, TRELLO_API_KEY, TRELLO_API_TOKEN)

        form = ChangeCardLocationForm(initial={'list_id': lists[0], 'card_id': cards[0]}, lists=lists, cards=cards)


        return render(request, 'trello_card_location.html', {'form3': form, 'lists': lists, 'cards': cards})
    elif request.method == 'POST':
        lists = get_trello_lists(BOARD_ID, TRELLO_API_KEY, TRELLO_API_TOKEN)
        cards = get_trello_cards(BOARD_ID, TRELLO_API_KEY, TRELLO_API_TOKEN)
        form = ChangeCardLocationForm(request.POST)
        card = form.data['card_id']
        new_list = form.data['list_id']
        url = f'https://api.trello.com/1/cards/{card}?idList={new_list}&key={TRELLO_API_KEY}&token={TRELLO_API_TOKEN}'

        response = requests.put(url)
        form = ChangeCardLocationForm(initial={'list_id': lists[0], 'card_id': cards[0]}, lists=lists, cards=cards)
        if response.status_code == 200:
            return render(request, 'trello_card_location.html', {'form3': form, 'lists': lists, 'cards': cards})
        else:
            return render(request, 'trello_card_location.html', {'form3': form, 'lists': lists, 'cards': cards})
        
@login_required(redirect_field_name="bejelentkezes_szukseges")       
def create_trello_list(request):
    form2 = CreateListForm()  

    if request.method == 'POST':
        form2 = CreateListForm(request.POST)
        nev = form2.data['list_name']
        url = f"https://api.trello.com/1/lists?name={nev}&idBoard={BOARD_ID}&key={TRELLO_API_KEY}&token={TRELLO_API_TOKEN}"

        response = requests.post(url)

        if response.status_code == 200:
            return HttpResponse(f"Új lista létrehozva: {nev})")
        else:
            return HttpResponse(f"Hiba a lista létrehozása során.")
    
    return render(request, 'trello_list.html', {'form2': form2})

@login_required(redirect_field_name="bejelentkezes_szukseges")
def change_data(request):
    user = request.user

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user)
    
    return render(request, 'change_data.html', {'form': form})

from django.contrib.auth import update_session_auth_hash

@login_required(redirect_field_name="bejelentkezes_szukseges")
def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'A jelszó sikeresen megváltozott!')
            return redirect('profile')
        else:
            for field in form.errors:
                for error in form.errors[field]:
                    messages.error(request, f"{field}: {error}")
    else:
        form = CustomPasswordChangeForm(user=request.user)
    return render(request, 'change_password.html', {'form': form})