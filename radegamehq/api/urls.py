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
from .views.Token import TokenView, TokenDetailsView
from .views.Phase import PhaseView, PhaseDetailsView
from .views.Team import TeamView, TeamDetailsView
from .views.ImageAsset import ImageAssetView, ImageAssetDetailsView
from .views.Keyword import KeywordView, KeywordDetailsView
from .views.Style import StyleView, StyleDetailsView
from .views.Sound import SoundDetailsView, SoundView
from .views.State import StateDetailsView, StateView
from .views.Expression import ExpressionView, ExpressionDetailsView
from .views.Animation import AnimationView, AnimationDetailsView
from .views.Handler import HandlerView, HandlerDetailsView
from .views.Setup import SetupDetailsView, SetupView

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

    url(r'games/(?P<gameid>[0-9]+)/tokens/(?P<pk>[0-9]+)/$', TokenDetailsView.as_view(),
        name="token.details"),
    url(r'games/(?P<pk>[0-9]+)/tokens/$', TokenView.as_view(), name="token.list"),

    url(r'games/(?P<gameid>[0-9]+)/phases/(?P<pk>[0-9]+)/$', PhaseDetailsView.as_view(),
        name="phase.details"),
    url(r'games/(?P<pk>[0-9]+)/phases/$', PhaseView.as_view(), name="phase.list"),

    url(r'games/(?P<gameid>[0-9]+)/teams/(?P<pk>[0-9]+)/$', TeamDetailsView.as_view(),
        name="team.details"),
    url(r'games/(?P<pk>[0-9]+)/teams/$', TeamView.as_view(), name="team.list"),

    url(r'games/(?P<gameid>[0-9]+)/keywords/(?P<pk>[0-9]+)/$', KeywordDetailsView.as_view(),
        name="keywords.details"),
    url(r'games/(?P<pk>[0-9]+)/keywords/$', KeywordView.as_view(), name="keywords.list"),

    url(r'games/(?P<gameid>[0-9]+)/styles/(?P<pk>[0-9]+)/$', StyleDetailsView.as_view(),
        name="style.details"),
    url(r'games/(?P<pk>[0-9]+)/styles/$', StyleView.as_view(), name="style.list"),

    url(r'games/(?P<gameid>[0-9]+)/sounds/(?P<pk>[0-9]+)/$', SoundDetailsView.as_view(),
        name="sound.details"),
    url(r'games/(?P<pk>[0-9]+)/sounds/$', SoundView.as_view(), name="sound.list"),

    url(r'games/(?P<gameid>[0-9]+)/states/(?P<pk>[0-9]+)/$', StateDetailsView.as_view(),
        name="state.details"),
    url(r'games/(?P<pk>[0-9]+)/states/$', StateView.as_view(), name="state.list"),

    url(r'games/(?P<gameid>[0-9]+)/expressions/(?P<pk>[0-9]+)/$', ExpressionDetailsView.as_view(),
        name="expression.details"),
    url(r'games/(?P<pk>[0-9]+)/expressions/$', ExpressionView.as_view(), name="expression.list"),

    url(r'games/(?P<gameid>[0-9]+)/animations/(?P<pk>[0-9]+)/$', AnimationDetailsView.as_view(),
        name="animation.details"),
    url(r'games/(?P<pk>[0-9]+)/animations/$', AnimationView.as_view(), name="animation.list"),

    url(r'games/(?P<gameid>[0-9]+)/handlers/(?P<pk>[0-9]+)/$', HandlerDetailsView.as_view(),
        name="handler.details"),
    url(r'games/(?P<pk>[0-9]+)/handlers/$', HandlerView.as_view(), name="handler.list"),

    url(r'games/(?P<gameid>[0-9]+)/setups/(?P<pk>[0-9]+)/$', SetupDetailsView.as_view(),
        name="setup.details"),
    url(r'games/(?P<pk>[0-9]+)/setups/$', SetupView.as_view(), name="setup.list"),

    # path('games/<int:pk>/data/', GameDataView.as_view(), name="game.data"),
    url(r'games/(?P<pk>[0-9]+)/data/$', GameDataView.as_view(), name="game.data"),
    url(r'games/(?P<pk>[0-9]+)/$', GameDetailsView.as_view(), name="game.details"),
    url(r'^games/$', GameView.as_view(), name="game.list"),

    url(r'games/(?P<gameid>[0-9]+)/imageassets/(?P<pk>[0-9]+)/$', ImageAssetDetailsView.as_view(),
        name="imageasset.details"),
    url(r'games/(?P<pk>[0-9]+)/imageassets/$', ImageAssetView.as_view(), name="imageasset.list"),

}

urlpatterns = format_suffix_patterns(urlpatterns)
