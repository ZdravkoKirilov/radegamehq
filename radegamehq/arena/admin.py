from django.contrib import admin

from .models import GamePlayer, GameInstance

admin.site.register(GamePlayer)
admin.site.register(GameInstance)
