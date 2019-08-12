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
from .entities.Token import Token
from .entities.Game import Game
from .entities.ImageAsset import ImageAsset
from .entities.Keyword import Keyword
from .entities.Style import Style
from .entities.State import State
from .entities.Expression import Expression
from .entities.Sound import Sound
from .entities.Setup import Setup
from .entities.Animation import Animation
from .entities.Handler import Handler

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
admin.site.register(Setup)
admin.site.register(ImageAsset)
admin.site.register(Style)
admin.site.register(Keyword)
admin.site.register(State)
admin.site.register(Expression)
admin.site.register(Sound)
admin.site.register(Animation)
admin.site.register(Handler)
