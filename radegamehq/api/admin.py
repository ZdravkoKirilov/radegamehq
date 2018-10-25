from django.contrib import admin

from api.entities.Path import Path
from api.entities.Location import Location
from api.entities.Stage import Stage
from api.entities.Choice import Choice, ChoiceOption
from api.entities.Condition import Condition, ConditionClause
from api.entities.Field import Field
from api.entities.Resource import Resource
from api.entities.Action import Action, ActionConfig
from api.entities.Round import Round, Phase
from api.entities.Faction import Faction
from api.entities.Stack import Stack, StackItem
from api.entities.Pool import Pool, PoolItem
from .entities.Game import Game

admin.site.register(Game)
admin.site.register(Field)
admin.site.register(Location)
admin.site.register(Path)
admin.site.register(Resource)
admin.site.register(Faction)
admin.site.register(Action)
admin.site.register(ActionConfig)
admin.site.register(Condition)
admin.site.register(ConditionClause)
admin.site.register(Round)
admin.site.register(Phase)
admin.site.register(Choice)
admin.site.register(ChoiceOption)
admin.site.register(Stage)
admin.site.register(Stack)
admin.site.register(StackItem)
admin.site.register(Pool)
admin.site.register(PoolItem)
