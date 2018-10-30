from django.db import models

from .Resource import Resource
from .Stack import Stack

from api.mixins.EntityBase import EntityBase

TYPE_CHOICES = (
    ('MOVE', 'MOVE'),
    ('WIN_GAME', 'WIN_GAME'),
    ('LOSE_GAME', 'LOSE_GAME'),
    ('ALTER_RESOURCE', 'ALTER_RESOURCE'),  # resource
    ('DRAW', 'DRAW'),  # can be used also for income instead of 'COLLECT'
    ('REDIRECT', 'REDIRECT'),
    ('DROP', 'DROP'),  # drop entity onto field award
    ('LOAD', 'LOAD'),  # drop entity onto field cost / lay trap
    ('GAMBLE', 'GAMBLE'),
    ('ALTER_KEYWORDS', 'ALTER_KEYWORDS')  # + / -  prefix, string based
)

TARGET_CHOICES = (
    ('PLAYER', 'PLAYER'),
    ('OTHER_PLAYER', 'OTHER_PLAYER'),
    ('SELF', 'SELF'),
    ('ACTIVE_PLAYER', 'ACTIVE_PLAYER'),
    ('FACTION', 'FACTION'),
    ('KEYWORD', 'KEYWORD'),
    ('TOKEN', 'TOKEN'),
    ('ACTIVE_TOKEN', 'ACTIVE_TOKEN'),
    ('OTHER_TOKEN', 'OTHER_TOKEN')
)

ACTION_MODES = (
    ('TRAP', 'TRAP'),
    ('TRIGGER', 'TRIGGER'),
    ('HYBRID', 'HYBRID'),  # both trap and trigger
    ('AUTO', 'AUTO')  # for internal, 'hidden' logic
)


class Action(EntityBase):
    image = models.ImageField(upload_to='action_images', blank=True, null=True, max_length=None)

    cost = models.ManyToManyField(Stack, related_name='action_cost', blank=True)  #  cost to play
    condition = models.ManyToManyField(Stack, related_name='action_condition',
                                       blank=True)  # enables you to play it

    restricted = models.ManyToManyField(Stack, related_name='action_restricted',
                                        blank=True)  # who cant have it in hand: IS_FACTION, others implicitly can
    allowed = models.ManyToManyField(Stack, related_name='action_allowed',
                                     blank=True)  # who can have it in hand: IS_FACTION, others implicitly cant

    mode = models.CharField(choices=ACTION_MODES, default=ACTION_MODES[0][1], max_length=255)

    def __str__(self):
        return "{}".format(self.name)


class ActionConfig(models.Model):
    owner = models.ForeignKey(Action, blank=True, null=True, on_delete=models.CASCADE, related_name='configs')

    type = models.CharField(max_length=255, blank=False, choices=TYPE_CHOICES)
    target = models.CharField(max_length=255, blank=False, choices=TARGET_CHOICES)

    condition = models.ForeignKey('Condition', on_delete=models.CASCADE, null=True,
                                  blank=True)
    choice = models.ForeignKey('Choice', on_delete=models.CASCADE, null=True,
                               blank=True)
    faction = models.ForeignKey('Faction', on_delete=models.CASCADE, null=True,
                                blank=True)
    token = models.ForeignKey('Token', on_delete=models.CASCADE, null=True,
                              blank=True)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, blank=True,
                                 null=True)
    action = models.ForeignKey(Action, on_delete=models.CASCADE, related_name='action_config_action', blank=True,
                               null=True)

    keywords = models.CharField(max_length=255, null=True, blank=True)

    value = models.TextField(null=True, blank=True)

    amount = models.IntegerField(blank=True, null=True, default=0)
    max_amount = models.IntegerField(blank=True, null=True, default=0)
    min_amount = models.IntegerField(blank=True, null=True, default=0)
    random_amount = models.NullBooleanField(default=False)

    def __str__(self):
        return "Config_{}_{}".format(self.owner.name, self.type)
