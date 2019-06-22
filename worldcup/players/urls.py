from django.urls import path

from . import views

urlpatterns = [
    path('', views.players_page, name='players_page'),
    path('insert', views.insert_player_details, name='insert'),
    path('get_players', views.get_players, name='get_players'),
    path('addPlayerPage', views.add_player_page, name='add_player_page'),
]
