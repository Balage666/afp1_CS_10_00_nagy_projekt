from django.urls import path
from . import views
urlpatterns = [
    path('index/', views.index, name='index'),
    path('documentation/', views.documentation, name='documentation'),
    path('trello_cards/', views.trello_cards, name='trello_cards'),
    path('code/', views.code, name='code'),
    path('profile/', views.profile, name='profile'),
    path('logout_view/', views.logout_view, name='logout_view'),
]

