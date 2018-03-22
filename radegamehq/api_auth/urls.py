from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateLocalUserView, GetTokenView

urlpatterns = {
    url(r'local/register', CreateLocalUserView.as_view()),
    url(r'local/login', GetTokenView.as_view())
}

urlpatterns = format_suffix_patterns(urlpatterns)