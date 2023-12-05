from django.urls import path
from .views import create_trello_card

urlpatterns = [
    path('trello/', create_trello_card, name='create_trello_card'),
]