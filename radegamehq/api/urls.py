from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import GameView, GameDetailsView, BoardFieldView, BoardFieldDetailsView, MapLocationView, \
    MapLocationDetailsView, MapView, MapDetailsView, MapPathView, MapPathDetailsView, ResourceView, ResourceDetailsView, \
    FactionView, FactionDetailsView, ActivityView, ActivityDetailsView, QuestView, QuestDetailsView, RoundView, \
    RoundDetailsView, TriviaView, TriviaDetailsView, StageView, StageDetailsView

urlpatterns = {

    url(r'games/(?P<gameid>[0-9]+)/stages/(?P<pk>[0-9]+)/$', StageDetailsView.as_view(),
        name="stage.details"),
    url(r'games/(?P<pk>[0-9]+)/stages/$', StageView.as_view(), name="stage.list"),

    url(r'games/(?P<gameid>[0-9]+)/trivia/(?P<pk>[0-9]+)/$', TriviaDetailsView.as_view(),
        name="trivia.details"),
    url(r'games/(?P<pk>[0-9]+)/trivia/$', TriviaView.as_view(), name="trivia.list"),

    url(r'games/(?P<gameid>[0-9]+)/rounds/(?P<pk>[0-9]+)/$', RoundDetailsView.as_view(),
        name="round.details"),
    url(r'games/(?P<pk>[0-9]+)/rounds/$', RoundView.as_view(), name="round.list"),

    url(r'games/(?P<gameid>[0-9]+)/quests/(?P<pk>[0-9]+)/$', QuestDetailsView.as_view(),
        name="quest.details"),
    url(r'games/(?P<pk>[0-9]+)/quests/$', QuestView.as_view(), name="quest.list"),

    url(r'games/(?P<gameid>[0-9]+)/actions/(?P<pk>[0-9]+)/$', ActivityDetailsView.as_view(),
        name="action.details"),
    url(r'games/(?P<pk>[0-9]+)/actions/$', ActivityView.as_view(), name="action.list"),

    url(r'games/(?P<gameid>[0-9]+)/factions/(?P<pk>[0-9]+)/$', FactionDetailsView.as_view(),
        name="faction.details"),
    url(r'games/(?P<pk>[0-9]+)/factions/$', FactionView.as_view(), name="faction.list"),

    url(r'games/(?P<gameid>[0-9]+)/resources/(?P<pk>[0-9]+)/$', ResourceDetailsView.as_view(),
        name="resource.details"),
    url(r'games/(?P<pk>[0-9]+)/resources/$', ResourceView.as_view(), name="resource.list"),

    url(r'games/(?P<gameid>[0-9]+)/paths/(?P<pk>[0-9]+)/$', MapPathDetailsView.as_view(),
        name="mappath.details"),
    url(r'games/(?P<pk>[0-9]+)/paths/$', MapPathView.as_view(), name="mappath.list"),

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
