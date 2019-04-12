from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views.Choice import ChoiceView, ChoiceDetailsView
from .views.Stage import StageView, StageDetailsView
from .views.Round import RoundView, RoundDetailsView
from .views.Condition import ConditionView, ConditionDetailsView
from .views.Path import MapPathView, MapPathDetailsView
from .views.Slot import SlotView, SlotDetailsView
from .views.Game import GameView, GameDetailsView, GameDataView
from .views.Field import BoardFieldView, BoardFieldDetailsView
from .views.Faction import FactionView, FactionDetailsView
from .views.Action import ActionView, ActionDetailsView
from .views.Source import SourceView, SourceDetailsView
from .views.Token import TokenView, TokenDetailsView
from .views.Phase import PhaseView, PhaseDetailsView
from .views.Team import TeamView, TeamDetailsView
from .views.ImageAsset import ImageAssetView, ImageAssetDetailsView
from .views.Keyword import KeywordView, KeywordDetailsView
from .views.Style import StyleView, StyleDetailsView
from .views.Group import GroupView, GroupDetailsView

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

    url(r'games/(?P<gameid>[0-9]+)/groups/(?P<pk>[0-9]+)/$', GroupDetailsView.as_view(),
        name="group.details"),
    url(r'games/(?P<pk>[0-9]+)/groups/$', GroupView.as_view(), name="group.list"),

    url(r'games/(?P<gameid>[0-9]+)/keywords/(?P<pk>[0-9]+)/$', KeywordDetailsView.as_view(),
        name="keywords.details"),
    url(r'games/(?P<pk>[0-9]+)/keywords/$', KeywordView.as_view(), name="keywords.list"),

    url(r'games/(?P<gameid>[0-9]+)/styles/(?P<pk>[0-9]+)/$', StyleDetailsView.as_view(),
        name="style.details"),
    url(r'games/(?P<pk>[0-9]+)/styles/$', StyleView.as_view(), name="style.list"),

    # path('games/<int:pk>/data/', GameDataView.as_view(), name="game.data"),
    url(r'games/(?P<pk>[0-9]+)/data/$', GameDataView.as_view(), name="game.data"),
    url(r'games/(?P<pk>[0-9]+)/$', GameDetailsView.as_view(), name="game.details"),
    url(r'^games/$', GameView.as_view(), name="game.list"),

    url(r'games/(?P<gameid>[0-9]+)/imageassets/(?P<pk>[0-9]+)/$', ImageAssetDetailsView.as_view(),
        name="imageasset.details"),
    url(r'games/(?P<pk>[0-9]+)/imageassets/$', ImageAssetView.as_view(), name="imageasset.list"),

}

urlpatterns = format_suffix_patterns(urlpatterns)
