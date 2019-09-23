from django.conf.urls import url

from .sockets import ArenaConsumer

arena_urlpatterns = [
    url(r'^ws/arena/(?P<game_name>[-\w]+)$', ArenaConsumer),
]
