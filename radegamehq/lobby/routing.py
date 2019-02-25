from django.conf.urls import url

from . import consumers

lobby_urlpatterns = [
    url(r'^ws/lobbies/(?P<lobby_name>[^/]+)/$', consumers.LobbyConsumer),
]
