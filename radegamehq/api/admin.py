from django.contrib import admin

from .entities.Path import Path
from .entities.Stage import Stage
from .entities.Choice import Choice, ChoiceOption
from .entities.Condition import Condition, ConditionClause
from .entities.Field import Field
from .entities.Slot import Slot
from .entities.Action import Action, ActionConfig
from .entities.Round import Round
from .entities.Phase import Phase
from .entities.Faction import Faction
from .entities.Source import Source
from .entities.Token import Token
from .entities.Game import Game, Setup
from .entities.ImageAsset import ImageAsset
from .entities.Keyword import Keyword
from .entities.Style import Style
from .entities.Group import Group, GroupItem
from .entities.State import State
from .entities.Expression import Expression
from .entities.Sound import Sound

admin.site.register(Game)
admin.site.register(Field)
admin.site.register(Slot)
admin.site.register(Path)
admin.site.register(Faction)
admin.site.register(Token)
admin.site.register(Action)
admin.site.register(ActionConfig)
admin.site.register(Condition)
admin.site.register(ConditionClause)
admin.site.register(Round)
admin.site.register(Phase)
admin.site.register(Choice)
admin.site.register(ChoiceOption)
admin.site.register(Stage)
admin.site.register(Source)
admin.site.register(Setup)
admin.site.register(ImageAsset)
admin.site.register(Style)
admin.site.register(Keyword)
admin.site.register(Group)
admin.site.register(GroupItem)
admin.site.register(State)
admin.site.register(Expression)
admin.site.register(Sound)
