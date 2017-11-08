from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import GameView, GameDetailsView

urlpatterns = {
    url(r'games/(?P<pk>[0-9]+)/$', GameDetailsView.as_view(), name="details"),
    url(r'^games/$', GameView.as_view(), name="create"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
