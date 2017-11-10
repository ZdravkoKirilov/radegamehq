from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import GameView, GameDetailsView, BoardFieldView, BoardFieldDetailsView

urlpatterns = {
    url(r'games/(?P<id>[0-9]+)/fields/(?P<pk>[0-9]+)/$', BoardFieldDetailsView.as_view(), name="field.details"),
    url(r'games/(?P<pk>[0-9]+)/fields/$', BoardFieldView.as_view(), name="field.list"),
    url(r'games/(?P<pk>[0-9]+)/$', GameDetailsView.as_view(), name="game.details"),
    url(r'^games/$', GameView.as_view(), name="game.list"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
