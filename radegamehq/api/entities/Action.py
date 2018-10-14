from django.db import models

from .Resource import Resource
from .EffectStack import EffectStack

from api.mixins.EntityBase import EntityBase

WIN_GAME = 'WIN_GAME'
LOSE_GAME = 'LOSE_GAME'
MOVE = 'MOVE'
COLLECT = 'COLLECT'
ALTER = 'ALTER'
DRAW = 'DRAW'
TRIGGER_QUEST = 'TRIGGER_QUEST'
TRIGGER_TRIVIA = 'TRIGGER_TRIVIA'
CANCEL = 'CANCEL'
REDIRECT = 'REDIRECT'

TYPE_CHOICES = (
    (MOVE, MOVE),
    (WIN_GAME, WIN_GAME),
    (LOSE_GAME, LOSE_GAME),
    (COLLECT, COLLECT),
    (ALTER, ALTER),
    (DRAW, DRAW),
    (TRIGGER_QUEST, TRIGGER_QUEST),
    (TRIGGER_TRIVIA, TRIGGER_TRIVIA),
    (CANCEL, CANCEL),
    (REDIRECT, REDIRECT)
)

PLAYER = 'PLAYER'
ACTIVE_PLAYER = 'ACTIVE_PLAYER'
SELF = 'SELF'
OTHER_PLAYER = 'OTHER_PLAYER'
FACTION = 'FACTION'
KEYWORD = 'KEYWORD'

TARGET_CHOICES = (
    (PLAYER, PLAYER),
    (OTHER_PLAYER, OTHER_PLAYER),
    (SELF, SELF),
    (ACTIVE_PLAYER, ACTIVE_PLAYER),
    (FACTION, FACTION),
    (KEYWORD, KEYWORD)
)


class Action(EntityBase):
    image = models.ImageField(upload_to='action_images', blank=True, null=True, max_length=None)

    cost = models.ManyToManyField(EffectStack, related_name='action_cost', null=True, blank=True)
    limitation = models.ManyToManyField(EffectStack, related_name='action_limitation', null=True, blank=True)

    restriction = models.ManyToManyField(EffectStack, related_name='action_restriction', null=True, blank=True)
    trap_mode = models.NullBooleanField(default=False)

    def __str__(self):
        return "{}".format(self.name)


class ActionConfig(models.Model):
    owner = models.ForeignKey(Action, on_delete=models.CASCADE, related_name='configs')

    type = models.CharField(max_length=255, blank=False, choices=TYPE_CHOICES)
    target = models.CharField(max_length=255, blank=False, choices=TARGET_CHOICES)

    condition = models.ForeignKey('Condition', on_delete=models.CASCADE, related_name="action_condition", null=True,
                                  blank=True)
    choice = models.ForeignKey('Choice', on_delete=models.CASCADE, related_name="action_choice", null=True,
                               blank=True)
    faction = models.ForeignKey('Faction', on_delete=models.CASCADE, related_name="action_faction", null=True,
                                blank=True)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, related_name='action_config_resource', blank=True,
                                 null=True)

    keywords = models.CharField(max_length=255, null=True, blank=True)
    amount = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return "Config_{}_{}".format(self.owner.name, self.type)
