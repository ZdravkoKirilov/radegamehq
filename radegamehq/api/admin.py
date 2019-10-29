from django.contrib import admin

from .entities.Path import Path
from .entities.Stage import Stage
from .entities.Choice import Choice, ChoiceOption, ChoiceTip
from .entities.Condition import Condition
from .entities.Slot import Slot, SlotHandler, SlotItem
from .entities.Action import Action, ActionConfig
from .entities.Round import Round, PhaseSlot
from .entities.Phase import Phase
from .entities.Faction import Faction
from .entities.Token import Token
from .entities.Game import Game, GameLanguage
from .entities.ImageAsset import ImageAsset
from .entities.Keyword import Keyword
from .entities.Style import Style
from .entities.State import State
from .entities.Expression import Expression
from .entities.Sound import Sound
from .entities.Setup import Setup, RoundSlot
from .entities.Animation import Animation, AnimationStep
from .entities.Handler import Handler
from .entities.Transition import Transition
from .entities.Text import Text, Translation
from .entities.Sonata import Sonata, SonataStep
from .entities.Shape import Shape, ShapePoint

admin.site.register(Game)
admin.site.register(GameLanguage)
admin.site.register(Text)
admin.site.register(Shape)
admin.site.register(ShapePoint)
admin.site.register(Translation)
admin.site.register(Transition)
admin.site.register(Sonata)
admin.site.register(SonataStep)
admin.site.register(Slot)
admin.site.register(SlotHandler)
admin.site.register(SlotItem)
admin.site.register(Path)
admin.site.register(Faction)
admin.site.register(Token)
admin.site.register(Action)
admin.site.register(ActionConfig)
admin.site.register(Condition)
admin.site.register(Round)
admin.site.register(PhaseSlot)
admin.site.register(Phase)
admin.site.register(Choice)
admin.site.register(ChoiceOption)
admin.site.register(ChoiceTip)
admin.site.register(Stage)
admin.site.register(Setup)
admin.site.register(RoundSlot)
admin.site.register(ImageAsset)
admin.site.register(Style)
admin.site.register(Keyword)
admin.site.register(State)
admin.site.register(Expression)
admin.site.register(Sound)
admin.site.register(Animation)
admin.site.register(AnimationStep)
admin.site.register(Handler)
