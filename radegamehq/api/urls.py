from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api.views.Choice import ChoiceView, ChoiceDetailsView
from api.views.Stage import StageView, StageDetailsView
from api.views.Round import RoundView, RoundDetailsView
from api.views.Resource import ResourceView, ResourceDetailsView
from api.views.Condition import ConditionView, ConditionDetailsView
from api.views.Path import MapPathView, MapPathDetailsView
from api.views.Location import MapLocationView, MapLocationDetailsView
from api.views.Game import GameView, GameDetailsView
from api.views.Field import BoardFieldView, BoardFieldDetailsView
from api.views.Faction import FactionView, FactionDetailsView
from api.views.Action import ActionView, ActionDetailsView
from api.views.EffectStack import EffectStackView, EffectStackDetailsView
from api.views.EffectGroup import EffectGroupView, EffectGroupDetailsView

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

    url(r'games/(?P<gameid>[0-9]+)/resources/(?P<pk>[0-9]+)/$', ResourceDetailsView.as_view(),
        name="resource.details"),
    url(r'games/(?P<pk>[0-9]+)/resources/$', ResourceView.as_view(), name="resource.list"),

    url(r'games/(?P<gameid>[0-9]+)/paths/(?P<pk>[0-9]+)/$', MapPathDetailsView.as_view(),
        name="mappath.details"),
    url(r'games/(?P<pk>[0-9]+)/paths/$', MapPathView.as_view(), name="mappath.list"),

    url(r'games/(?P<gameid>[0-9]+)/locations/(?P<pk>[0-9]+)/$', MapLocationDetailsView.as_view(),
        name="location.details"),
    url(r'games/(?P<pk>[0-9]+)/locations/$', MapLocationView.as_view(), name="location.list"),

    url(r'games/(?P<gameid>[0-9]+)/fields/(?P<pk>[0-9]+)/$', BoardFieldDetailsView.as_view(), name="field.details"),
    url(r'games/(?P<pk>[0-9]+)/fields/$', BoardFieldView.as_view(), name="field.list"),

    url(r'games/(?P<gameid>[0-9]+)/effect-stacks/(?P<pk>[0-9]+)/$', EffectStackDetailsView.as_view(),
        name="effect_stack.details"),
    url(r'games/(?P<pk>[0-9]+)/effect-stacks/$', EffectStackView.as_view(), name="effect_stack.list"),

    url(r'games/(?P<gameid>[0-9]+)/effect-groups/(?P<pk>[0-9]+)/$', EffectGroupDetailsView.as_view(),
        name="effect_group.details"),
    url(r'games/(?P<pk>[0-9]+)/effect-groups/$', EffectGroupView.as_view(), name="effect_group.list"),

    url(r'games/(?P<pk>[0-9]+)/$', GameDetailsView.as_view(), name="game.details"),
    url(r'^games/$', GameView.as_view(), name="game.list"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
