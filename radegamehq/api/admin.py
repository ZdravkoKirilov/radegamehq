from django.contrib import admin

from api.entities.Path import Path
from api.entities.Stage import Stage
from api.entities.Choice import Choice, ChoiceOption
from api.entities.Condition import Condition, ConditionClause
from api.entities.Field import Field
from .entities.Slot import Slot
from api.entities.Action import Action, ActionConfig
from api.entities.Round import Round
from api.entities.Phase import Phase
from api.entities.Faction import Faction
from api.entities.Source import Source, SourceItem
from api.entities.Token import Token
from .entities.Game import Game
from .entities.Setup import Setup
from .entities.ImageAsset import ImageAsset

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
admin.site.register(SourceItem)
admin.site.register(Setup)
admin.site.register(ImageAsset)
