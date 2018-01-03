from django.contrib import admin

from .models import Game, BoardField, MapLocation, \
    Map, MapPath, Resource, FieldIncome, FieldCost, Faction, FactionResource, Action, ActionConfig

admin.site.register(Game)
admin.site.register(BoardField)
admin.site.register(MapLocation)
admin.site.register(Map)
admin.site.register(MapPath)
admin.site.register(Resource)
admin.site.register(FieldIncome)
admin.site.register(FieldCost)
admin.site.register(Faction)
admin.site.register(FactionResource)
admin.site.register(Action)
admin.site.register(ActionConfig)
