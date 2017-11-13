from django.contrib import admin

from .models import Game, BoardField, MapLocation, Map

admin.site.register(Game)
admin.site.register(BoardField)
admin.site.register(MapLocation)
admin.site.register(Map)
