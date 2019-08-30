from django.urls import path
from .views import LobbyListView, LobbyDetailsView, PlayerListView, PlayerDetailsView, NewGameView

urlpatterns = [
    path('lobbies/<str:pk>/players/<str:player>', PlayerDetailsView.as_view(), name='players_details'),
    path('lobbies/<str:pk>/players', PlayerListView.as_view(), name='players_list'),
    path('lobbies/<str:pk>/create', NewGameView.as_view(), name='game_create'),
    path('all_players', PlayerListView.as_view(), name='all_players_list'),
    path('lobbies/', LobbyListView.as_view(), name='lobby_list'),
    path('lobbies/<str:pk>', LobbyDetailsView.as_view(), name='lobby_details'),
]
