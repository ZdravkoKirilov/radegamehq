from django.urls import path
from .views import GameInstanceView, ActiveGamesView

urlpatterns = [
    path('arena/active-game/<str:public_id>', GameInstanceView.as_view(), name='game_instance'),
    path('arena/active-games/<str:user_id>', ActiveGamesView.as_view(), name='active_games')
]
