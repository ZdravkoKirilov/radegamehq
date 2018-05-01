from django.db import models

from .Game import Game
from .Resource import Resource

WIN_GAME = 'WIN_GAME'
LOSE_GAME = 'LOSE_GAME'
MOVE = 'MOVE'
COLLECT = 'COLLECT'
ALTER = 'ALTER'
DRAW = 'DRAW'
TRIGGER_QUEST = 'TRIGGER_QUEST'
TRIGGER_TRIVIA = 'TRIGGER_TRIVIA'
CANCEL = 'CANCEL'

TYPE_CHOICES = (
    (MOVE, MOVE),
    (WIN_GAME, WIN_GAME),
    (LOSE_GAME, LOSE_GAME),
    (COLLECT, COLLECT),
    (ALTER, ALTER),
    (DRAW, DRAW),
    (TRIGGER_QUEST, TRIGGER_QUEST),
    (TRIGGER_TRIVIA, TRIGGER_TRIVIA),
    (CANCEL, CANCEL)
)

TRIGGER = 'TRIGGER'
PASSIVE = 'PASSIVE'

MODE_CHOICES = (
    (TRIGGER, TRIGGER),
    (PASSIVE, PASSIVE),
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

DISTRIBUTED = 'DISTRIBUTED'
LIMITED = 'LIMITED'

QUOTA_TYPES = (
    (DISTRIBUTED, DISTRIBUTED),
    (LIMITED, LIMITED)
)


class Activity(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True)
    keywords = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='activity_images', blank=True, null=True, max_length=None)
    mode = models.CharField(max_length=255, choices=MODE_CHOICES, default=MODE_CHOICES[0][0])

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name_plural = 'Activities'


class ActivityConfig(models.Model):
    type = models.CharField(max_length=255, blank=False, choices=TYPE_CHOICES)
    target = models.CharField(max_length=255, blank=False, choices=TARGET_CHOICES)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='configs')
    quest = models.ForeignKey('Quest', on_delete=models.CASCADE, related_name="activity_quest", null=True, blank=True)
    trivia = models.ForeignKey('Trivia', on_delete=models.CASCADE, related_name="activity_trivia", null=True,
                               blank=True)
    faction = models.ForeignKey('Faction', on_delete=models.CASCADE, related_name="activity_faction", null=True,
                                blank=True)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, related_name='config_resource', blank=True,
                                 null=True)
    keyword = models.CharField(max_length=255, null=True, blank=True)
    amount = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return "Config_{}_{}".format(self.activity.name, self.type)


class ActivityCost(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='cost')
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, blank=True, null=True)
    keyword = models.CharField(max_length=255, blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return "Cost_{}_{}".format(self.activity.name, self.resource.name)


class ActivityQuota(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='quota')
    faction = models.ForeignKey('Faction', on_delete=models.CASCADE, related_name='faction_quota', null=True,
                                blank=True)
    field = models.ForeignKey('Field', on_delete=models.CASCADE, related_name='field_quota', null=True,
                              blank=True)
    round = models.ForeignKey('Round', on_delete=models.CASCADE, related_name='round_quota', null=True,
                              blank=True)
    filter = models.CharField(max_length=255, null=True, blank=True)
    renewable = models.BooleanField(default=False)
    auto_trigger = models.BooleanField(default=False)
    amount = models.IntegerField(blank=True, null=True)
    type = models.CharField(choices=QUOTA_TYPES, max_length=255, default=QUOTA_TYPES[0][0])
