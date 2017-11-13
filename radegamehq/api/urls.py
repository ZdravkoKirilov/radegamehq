from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import GameView, GameDetailsView, BoardFieldView, BoardFieldDetailsView, MapLocationView, \
    MapLocationDetailsView, MapView, MapDetailsView

urlpatterns = {
    url(r'games/(?P<gameid>[0-9]+)/maps/(?P<pk>[0-9]+)/$', MapDetailsView.as_view(),
        name="map.details"),
    url(r'games/(?P<pk>[0-9]+)/maps/$', MapView.as_view(), name="map.list"),

    url(r'games/(?P<gameid>[0-9]+)/locations/(?P<pk>[0-9]+)/$', MapLocationDetailsView.as_view(),
        name="location.details"),
    url(r'games/(?P<pk>[0-9]+)/locations/$', MapLocationView.as_view(), name="location.list"),

    url(r'games/(?P<gameid>[0-9]+)/fields/(?P<pk>[0-9]+)/$', BoardFieldDetailsView.as_view(), name="field.details"),
    url(r'games/(?P<pk>[0-9]+)/fields/$', BoardFieldView.as_view(), name="field.list"),

    url(r'games/(?P<pk>[0-9]+)/$', GameDetailsView.as_view(), name="game.details"),
    url(r'^games/$', GameView.as_view(), name="game.list"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
