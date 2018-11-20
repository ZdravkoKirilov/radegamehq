from django.db import models

from api.mixins.EntityBase import EntityBase

TYPE_CHOICES = (
    ('WIN_GAME', 'WIN_GAME'),
    ('LOSE_GAME', 'LOSE_GAME'),

    ('MOVE', 'MOVE'),
    ('HOP', 'HOP'),

    ('DRAW', 'DRAW'),
    ('REVEAL', 'REVEAL'),
    ('RETURN', 'RETURN'),
    ('DISCARD', 'DISCARD'),
    ('DROP', 'DROP'),

    ('ALTER', 'ALTER'),

    ('GAIN', 'GAIN'),
    ('CLOSE', 'CLOSE'),

    ('GAMBLE', 'GAMBLE'),

    ('BID', 'BID'),

)

TARGET_CHOICES = (
    ('PLAYER', 'PLAYER'),
    ('FACTION', 'FACTION'),
    ('KEYWORD', 'KEYWORD'),
    ('TEAM', 'TEAM'),
    ('TOKEN', 'TOKEN'),
    ('SLOT', 'SLOT'),
    ('PATH', 'PATH'),
)

TARGET_TYPES = (
    ('SELF', 'SELF'),
    ('ACTIVE', 'ACTIVE'),
    ('OTHER_TARGET', 'OTHER_TARGET'),
    ('TARGET', 'TARGET'),
    ('INVOLVED', 'INVOLVED'),
    ('OTHER_INVOLVED', 'OTHER_INVOLVED'),
    ('OPPONENT', 'OPPONENT'),
    ('TEAMMATE', 'TEAMMATE'),
    ('ALL_FRIENDLY', 'ALL_FRIENDLY'),
    ('TARGET_FRIENDLY', 'TARGET_FRIENDLY'),
    ('ALL_ENEMY', 'ALL_ENEMY'),
    ('TARGET_ENEMY', 'TARGET_ENEMY'),
)

ACTION_MODES = (
    ('TRIGGER', 'TRIGGER'),
    ('HYBRID', 'HYBRID'),  # both trap and trigger
    ('AUTO', 'AUTO'),  # for internal, 'hidden' logic
    ('PASSIVE', 'PASSIVE'),
)

COMPUTED = (
    ('HOP_RANGE', 'HOP_RANGE'),
    ('BID_DIFFERENCE', 'BID_DIFFERENCE'),
)


class Action(EntityBase):
    image = models.ImageField(upload_to='action_images', blank=True, null=True, max_length=None)

    cost = models.ManyToManyField('Source', related_name='action_cost', blank=True)  # cost to play

    condition = models.ManyToManyField('Condition', related_name='action_condition',
                                       blank=True)  # enables you to play it

    restricted = models.ManyToManyField('Condition', related_name='action_restricted',
                                        blank=True)  # who cant have it in hand: IS_FACTION, others implicitly can
    allowed = models.ManyToManyField('Condition', related_name='action_allowed',
                                     blank=True)  # who can have it in hand: IS_FACTION, others implicitly cant

    settings = models.ManyToManyField('Condition', related_name='action_settings', blank=True)

    mode = models.CharField(choices=ACTION_MODES, default=ACTION_MODES[0][1], max_length=255)

    reveal_cost = models.ManyToManyField('Source', null=True, blank=True)
    reveal_slots = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return "{}".format(self.name)


class ActionConfig(models.Model):
    owner = models.ForeignKey(Action, blank=True, null=True, on_delete=models.CASCADE, related_name='configs')

    type = models.CharField(max_length=255, blank=False, choices=TYPE_CHOICES)
    target = models.CharField(max_length=255, blank=False, choices=TARGET_CHOICES)
    target_type = models.CharField(max_length=255, blank=True, null=True, choices=TARGET_TYPES)

    condition = models.ForeignKey('Condition', on_delete=models.CASCADE, null=True,
                                  blank=True)
    choice = models.ForeignKey('Choice', on_delete=models.CASCADE, null=True,
                               blank=True)
    faction = models.ForeignKey('Faction', on_delete=models.CASCADE, null=True,
                                blank=True)
    token = models.ForeignKey('Token', on_delete=models.CASCADE, null=True,
                              blank=True)
    action = models.ForeignKey(Action, on_delete=models.CASCADE, related_name='action_config_action', blank=True,
                               null=True)

    keywords = models.CharField(max_length=255, null=True, blank=True)

    value = models.CharField(null=True, blank=True, max_length=255)
    computed_value = models.CharField(null=True, blank=True, choices=COMPUTED, max_length=255)

    amount = models.IntegerField(blank=True, null=True, default=0)
    max_amount = models.IntegerField(blank=True, null=True, default=0)
    min_amount = models.IntegerField(blank=True, null=True, default=0)
    random_amount = models.BooleanField(blank=True, null=True, default=False)

    def __str__(self):
        return "Config_{}_{}".format(self.owner.name, self.type)
