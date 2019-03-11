from django.conf.urls import url

from .consumers.Lobbies import LobbiesConsumer
from .consumers.Lobby import LobbyConsumer

lobby_urlpatterns = [
    url(r'^ws/lobbies/(?P<lobby_name>[^/]+)/$', LobbyConsumer),
    url(r'^ws/lobbies', LobbiesConsumer),
]
