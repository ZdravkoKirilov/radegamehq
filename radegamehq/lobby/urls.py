from django.urls import path
from .views import LobbyListView, LobbyDetailsView, PlayerListView, PlayerDetailsView

urlpatterns = [
    path('lobbies/<str:pk>/players/<str:player>', PlayerDetailsView.as_view(), name='players_details'),
    path('lobbies/<str:pk>/players', PlayerListView.as_view(), name='players_list'),
    path('lobbies/', LobbyListView.as_view(), name='lobby_list'),
    path('lobbies/<str:pk>', LobbyDetailsView.as_view(), name='lobby_details'),
]
