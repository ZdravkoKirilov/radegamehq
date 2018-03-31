from django.db import models

from api.entities.Game import Game
from .Resource import Resource


class Activity(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    image = models.FileField(upload_to='activity_images', blank=True, null=True, max_length=200)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name_plural = 'Activities'


class ActivityConfig(models.Model):
    ATTACK_FIELD = 'ATTACK_FIELD'
    DEFEND_FIELD = 'DEFEND_FIELD'
    MINE_RESOURCES = 'MINE_RESOURCES'
    CANCEL_ATTACK_FIELD = 'CANCEL_ATTACK_FIELD'
    CANCEL_DEFEND_FIELD = 'CANCEL_DEFEND_FIELD'
    CANCEL_MINE_RESOURCE = 'CANCEL_MINE_RESOURCE'
    ALTER_RESOURCE = 'ALTER_RESOURCE'
    STEAL_QUEST = 'STEAL_QUEST'
    DISCARD_QUEST = 'DISCARD_QUEST'
    DRAW_QUEST = 'DRAW_QUEST'
    STEAL_ACTIVITY = 'STEAL_ACTIVITY'
    DISCARD_ACTIVITY = 'DISCARD_ACTIVITY'
    CANCEL_ACTIVITY = 'CANCEL_ACTIVITY'
    PEEK_QUESTS = 'PEEK_QUESTS'
    PEEK_ACTIVITIES = 'PEEK_ACTIVITIES'

    TYPE_CHOICES = (
        (ATTACK_FIELD, 'ATTACK_FIELD'),
        (DEFEND_FIELD, 'DEFEND_FIELD'),
        (MINE_RESOURCES, 'MINE_RESOURCES'),
        (CANCEL_ATTACK_FIELD, 'CANCEL_ATTACK_FIELD'),
        (CANCEL_DEFEND_FIELD, 'CANCEL_DEFEND_FIELD'),
        (CANCEL_MINE_RESOURCE, 'CANCEL_MINE_RESOURCE'),
        (ALTER_RESOURCE, 'ALTER_RESOURCE'),
        (STEAL_QUEST, 'STEAL_QUEST'),
        (DISCARD_QUEST, 'DISCARD_QUEST'),
        (DRAW_QUEST, 'DRAW_QUEST'),
        (STEAL_ACTIVITY, 'STEAL_ACTIVITY'),
        (DISCARD_ACTIVITY, 'DISCARD_ACTIVITY'),
        (CANCEL_ACTIVITY, 'CANCEL_ACTIVITY'),
        (PEEK_QUESTS, 'PEEK_QUESTS'),
        (PEEK_ACTIVITIES, 'PEEK_ACTIVITIES'),
    )

    TRIGGER = 'TRIGGER'
    PASSIVE = 'PASSIVE'
    HIDDEN = 'HIDDEN'

    MODE_CHOICES = (
        (TRIGGER, 'TRIGGER'),
        (PASSIVE, 'PASSIVE'),
        (HIDDEN, 'HIDDEN'),
    )

    FIELD = 'FIELD'
    PLAYER = 'PLAYER'
    OTHER_PLAYER = 'OTHER_PLAYER'
    SELF = 'SELF'
    ACTIVE_FIELD = 'ACTIVE_FIELD'
    ACTIVE_PLAYER = 'ACTIVE_PLAYER'

    TARGET_CHOICES = (
        (FIELD, 'FIELD'),
        (PLAYER, 'PLAYER'),
        (OTHER_PLAYER, 'OTHER_PLAYER'),
        (SELF, 'SELF'),
        (ACTIVE_FIELD, 'ACTIVE_FIELD'),
        (ACTIVE_PLAYER, 'ACTIVE_PLAYER')
    )

    type = models.CharField(max_length=255, blank=False, choices=TYPE_CHOICES)
    mode = models.CharField(max_length=255, blank=False, choices=MODE_CHOICES)
    target = models.CharField(max_length=255, blank=False, choices=TARGET_CHOICES)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='config')
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, related_name='config_resource', blank=True,
                                 null=True)
    amount = models.IntegerField(blank=True, null=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}_{}".format(self.activity.name, self.type)