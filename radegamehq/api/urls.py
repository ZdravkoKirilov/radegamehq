from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views.Widget import WidgetView, WidgetDetailsView, NodeView, NodeDetailsView
from .views.Module import ModuleView, ModuleDetailsView
from .views.Game import GameView, GameDetailsView, GameDataView
from .views.Token import TokenView, TokenDetailsView
from .views.ImageAsset import ImageAssetView, ImageAssetDetailsView
from .views.Style import StyleView, StyleDetailsView
from .views.Sound import SoundDetailsView, SoundView
from .views.Expression import ExpressionView, ExpressionDetailsView
from .views.Animation import AnimationView, AnimationDetailsView
from .views.Setup import SetupDetailsView, SetupView
from .views.Text import TextView, TextDetailsView
from .views.Sonata import SonataView, SonataDetailsView
from .views.Shape import ShapeView, ShapeDetailsView
from .views.Sandbox import SandboxView, SandboxDetailsView
from .views.Version import VersionDetailsView, VersionView

urlpatterns = {

    url(r'games/(?P<gameid>[0-9]+)/widgets/(?P<widgetid>[0-9]+)/nodes/(?P<pk>[0-9]+)/$', NodeDetailsView.as_view(),
        name="node.details"),
    url(r'games/(?P<pk>[0-9]+)/widgets/(?P<widgetId>[0-9]+)/nodes/$',
        NodeView.as_view(), name="node.list"),

    url(r'games/(?P<gameid>[0-9]+)/widgets/(?P<pk>[0-9]+)/$', WidgetDetailsView.as_view(),
        name="widget.details"),
    url(r'games/(?P<pk>[0-9]+)/widgets/$',
        WidgetView.as_view(), name="widget.list"),

    url(r'games/(?P<gameid>[0-9]+)/sandboxes/(?P<pk>[0-9]+)/$', SandboxDetailsView.as_view(),
        name="sandbox.details"),
    url(r'games/(?P<pk>[0-9]+)/sandboxes/$',
        SandboxView.as_view(), name="sandbox.list"),


    url(r'games/(?P<gameid>[0-9]+)/modules/(?P<pk>[0-9]+)/$', ModuleDetailsView.as_view(),
        name="module.details"),
    url(r'games/(?P<pk>[0-9]+)/modules/$',
        ModuleView.as_view(), name="module.list"),


    url(r'games/(?P<gameid>[0-9]+)/shapes/(?P<pk>[0-9]+)/$', ShapeDetailsView.as_view(),
        name="shape.details"),
    url(r'games/(?P<pk>[0-9]+)/shapes/$',
        ShapeView.as_view(), name="shape.list"),

    url(r'games/(?P<gameid>[0-9]+)/sonatas/(?P<pk>[0-9]+)/$',
        SonataDetailsView.as_view(), name="sonata.details"),
    url(r'games/(?P<pk>[0-9]+)/sonatas/$',
        SonataView.as_view(), name="sonata.list"),

    url(r'games/(?P<gameid>[0-9]+)/tokens/(?P<pk>[0-9]+)/$', TokenDetailsView.as_view(),
        name="token.details"),
    url(r'games/(?P<pk>[0-9]+)/tokens/$',
        TokenView.as_view(), name="token.list"),

    url(r'games/(?P<gameid>[0-9]+)/styles/(?P<pk>[0-9]+)/$', StyleDetailsView.as_view(),
        name="style.details"),
    url(r'games/(?P<pk>[0-9]+)/styles/$',
        StyleView.as_view(), name="style.list"),

    url(r'games/(?P<gameid>[0-9]+)/sounds/(?P<pk>[0-9]+)/$', SoundDetailsView.as_view(),
        name="sound.details"),
    url(r'games/(?P<pk>[0-9]+)/sounds/$',
        SoundView.as_view(), name="sound.list"),

    url(r'games/(?P<gameid>[0-9]+)/expressions/(?P<pk>[0-9]+)/$', ExpressionDetailsView.as_view(),
        name="expression.details"),
    url(r'games/(?P<pk>[0-9]+)/expressions/$',
        ExpressionView.as_view(), name="expression.list"),

    url(r'games/(?P<gameid>[0-9]+)/animations/(?P<pk>[0-9]+)/$', AnimationDetailsView.as_view(),
        name="animation.details"),
    url(r'games/(?P<pk>[0-9]+)/animations/$',
        AnimationView.as_view(), name="animation.list"),

    url(r'games/(?P<gameid>[0-9]+)/setups/(?P<pk>[0-9]+)/$', SetupDetailsView.as_view(),
        name="setup.details"),
    url(r'games/(?P<pk>[0-9]+)/setups/$',
        SetupView.as_view(), name="setup.list"),

    url(r'games/(?P<gameid>[0-9]+)/imageassets/(?P<pk>[0-9]+)/$', ImageAssetDetailsView.as_view(),
        name="imageasset.details"),
    url(r'games/(?P<pk>[0-9]+)/imageassets/$',
        ImageAssetView.as_view(), name="imageasset.list"),

    url(r'games/(?P<gameid>[0-9]+)/texts/(?P<pk>[0-9]+)/$', TextDetailsView.as_view(),
        name="text.details"),
    url(r'games/(?P<pk>[0-9]+)/texts/$', TextView.as_view(), name="text.list"),




    # path('games/<int:pk>/data/', GameDataView.as_view(), name="game.data"),
    url(r'games/(?P<pk>[0-9]+)/data/$',
        GameDataView.as_view(), name="game.data"),
    url(r'games/(?P<pk>[0-9]+)/$',
        GameDetailsView.as_view(), name="game.details"),
    url(r'^games/$', GameView.as_view(), name="game.list"),

    url(r'games/(?P<gameid>[0-9]+)/versions/(?P<pk>[0-9]+)/$', VersionDetailsView.as_view(),
        name="version.details"),
    url(r'games/(?P<pk>[0-9]+)/versions/$',
        VersionView.as_view(), name="version.list"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
