from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api.views.Choice import ChoiceView, ChoiceDetailsView
from api.views.Stage import StageView, StageDetailsView
from api.views.Round import RoundView, RoundDetailsView
from api.views.Condition import ConditionView, ConditionDetailsView
from api.views.Path import MapPathView, MapPathDetailsView
from api.views.Slot import SlotView, SlotDetailsView
from api.views.Game import GameView, GameDetailsView
from api.views.Field import BoardFieldView, BoardFieldDetailsView
from api.views.Faction import FactionView, FactionDetailsView
from api.views.Action import ActionView, ActionDetailsView
from api.views.Source import SourceView, SourceDetailsView
from .views.Token import TokenView, TokenDetailsView
from .views.Phase import PhaseView, PhaseDetailsView
from .views.Team import TeamView, TeamDetailsView

urlpatterns = {

    url(r'games/(?P<gameid>[0-9]+)/stages/(?P<pk>[0-9]+)/$', StageDetailsView.as_view(),
        name="stage.details"),
    url(r'games/(?P<pk>[0-9]+)/stages/$', StageView.as_view(), name="stage.list"),

    url(r'games/(?P<gameid>[0-9]+)/choices/(?P<pk>[0-9]+)/$', ChoiceDetailsView.as_view(),
        name="choice.details"),
    url(r'games/(?P<pk>[0-9]+)/choices/$', ChoiceView.as_view(), name="choice.list"),

    url(r'games/(?P<gameid>[0-9]+)/rounds/(?P<pk>[0-9]+)/$', RoundDetailsView.as_view(),
        name="round.details"),
    url(r'games/(?P<pk>[0-9]+)/rounds/$', RoundView.as_view(), name="round.list"),

    url(r'games/(?P<gameid>[0-9]+)/conditions/(?P<pk>[0-9]+)/$', ConditionDetailsView.as_view(),
        name="condition.details"),
    url(r'games/(?P<pk>[0-9]+)/conditions/$', ConditionView.as_view(), name="condition.list"),

    url(r'games/(?P<gameid>[0-9]+)/actions/(?P<pk>[0-9]+)/$', ActionDetailsView.as_view(),
        name="action.details"),
    url(r'games/(?P<pk>[0-9]+)/actions/$', ActionView.as_view(), name="action.list"),

    url(r'games/(?P<gameid>[0-9]+)/factions/(?P<pk>[0-9]+)/$', FactionDetailsView.as_view(),
        name="faction.details"),
    url(r'games/(?P<pk>[0-9]+)/factions/$', FactionView.as_view(), name="faction.list"),

    url(r'games/(?P<gameid>[0-9]+)/paths/(?P<pk>[0-9]+)/$', MapPathDetailsView.as_view(),
        name="mappath.details"),
    url(r'games/(?P<pk>[0-9]+)/paths/$', MapPathView.as_view(), name="mappath.list"),

    url(r'games/(?P<gameid>[0-9]+)/slots/(?P<pk>[0-9]+)/$', SlotDetailsView.as_view(),
        name="location.details"),
    url(r'games/(?P<pk>[0-9]+)/slots/$', SlotView.as_view(), name="location.list"),

    url(r'games/(?P<gameid>[0-9]+)/fields/(?P<pk>[0-9]+)/$', BoardFieldDetailsView.as_view(), name="field.details"),
    url(r'games/(?P<pk>[0-9]+)/fields/$', BoardFieldView.as_view(), name="field.list"),

    url(r'games/(?P<gameid>[0-9]+)/sources/(?P<pk>[0-9]+)/$', SourceDetailsView.as_view(),
        name="pool.details"),
    url(r'games/(?P<pk>[0-9]+)/sources/$', SourceView.as_view(), name="pool.list"),

    url(r'games/(?P<gameid>[0-9]+)/tokens/(?P<pk>[0-9]+)/$', TokenDetailsView.as_view(),
        name="token.details"),
    url(r'games/(?P<pk>[0-9]+)/tokens/$', TokenView.as_view(), name="token.list"),

    url(r'games/(?P<gameid>[0-9]+)/phases/(?P<pk>[0-9]+)/$', PhaseDetailsView.as_view(),
        name="phase.details"),
    url(r'games/(?P<pk>[0-9]+)/phases/$', PhaseView.as_view(), name="phase.list"),

    url(r'games/(?P<gameid>[0-9]+)/teams/(?P<pk>[0-9]+)/$', TeamDetailsView.as_view(),
        name="team.details"),
    url(r'games/(?P<pk>[0-9]+)/teams/$', TeamView.as_view(), name="team.list"),

    url(r'games/(?P<pk>[0-9]+)/$', GameDetailsView.as_view(), name="game.details"),
    url(r'^games/$', GameView.as_view(), name="game.list"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
