from django.urls import path
from . import views
from .views import create_trello_card,create_trello_list,move_cards
urlpatterns = [
    path('index/', views.index, name='index'),
    path('documentation/', views.documentation, name='documentation'),
    path('code/', views.code, name='code'),
    path('profile/', views.profile, name='profile'),
    path('logout_view/', views.logout_view, name='logout_view'),
    path('trello/', create_trello_card, name='trello'),
    path('trello_list/', create_trello_list, name='trello_list'),
    path('trello_card_location/',move_cards, name='trello_card_location'),
    path('change_data/', views.change_data, name='change_data'),
    path('change_password/', views.change_password, name='change_password'),
]

