from django.contrib import admin

from .entities.Widget import Widget, WidgetNode, NodeHandler
from .entities.Choice import Choice, ChoiceOption, ChoiceTip
from .entities.Condition import Condition
from .entities.Module import Module
from .entities.Token import Token
from .entities.Game import Game, GameLanguage
from .entities.ImageAsset import ImageAsset
from .entities.Style import Style
from .entities.Expression import Expression
from .entities.Sound import Sound
from .entities.Setup import Setup
from .entities.Animation import Animation, AnimationStep
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
admin.site.register(WidgetNode)
admin.site.register(NodeHandler)
admin.site.register(Token)
admin.site.register(Condition)
admin.site.register(Module)
admin.site.register(Choice)
admin.site.register(ChoiceOption)
admin.site.register(ChoiceTip)
admin.site.register(Widget)
admin.site.register(Setup)
admin.site.register(ImageAsset)
admin.site.register(Style)
admin.site.register(Expression)
admin.site.register(Sound)
admin.site.register(Animation)
admin.site.register(AnimationStep)
