from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    return render(request, 'index.html')

def documentation(request):
    return render(request, 'documentation.html')

def trello_cards(request):
    return render(request, 'trello_cards.html')

def code(request):
    return render(request, 'code.html')

def profile(request):
    return render(request, 'profile.html')