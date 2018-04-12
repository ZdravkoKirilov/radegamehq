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
    WIN_GAME = 'WIN_GAME'
    LOSE_GAME = 'LOSE_GAME'
    MOVE = 'MOVE'
    COLLECT_RESOURCES = 'COLLECT_RESOURCES'
    ALTER_RESOURCE = 'ALTER_RESOURCE'
    PREPARE_RESOURCE = 'PREPARE_RESOURCE'
    STORE_RESOURCE = 'STORE_RESOURCE'
    REQUEST_HINT = 'REQUEST_HINT'
    GIVE_HINT = 'GIVE_HINT'
    DRAW = 'DRAW'

    TYPE_CHOICES = (
        (MOVE, 'MOVE'),
        (WIN_GAME, 'WIN_GAME'),
        (LOSE_GAME, 'LOSE_GAME'),
        (COLLECT_RESOURCES, 'COLLECT_RESOURCES'),
        (ALTER_RESOURCE, 'ALTER_RESOURCE'),
        (PREPARE_RESOURCE, 'PREPARE_RESOURCE'),
        (STORE_RESOURCE, 'STORE_RESOURCE'),
        (REQUEST_HINT, 'REQUEST_HINT'),
        (GIVE_HINT, 'GIVE_HINT'),
        (DRAW, 'DRAW')
    )

    TRIGGER = 'TRIGGER'
    AUTO_TRIGGER = 'AUTO_TRIGGER'

    MODE_CHOICES = (
        (TRIGGER, 'TRIGGER'),
        (AUTO_TRIGGER, 'AUTO_TRIGGER'),
    )

    FIELD = 'FIELD'
    PLAYER = 'PLAYER'
    ACTIVE_PLAYER = 'ACTIVE_PLAYER'
    SELF = 'SELF'
    OTHER_PLAYER = 'OTHER_PLAYER'

    TARGET_CHOICES = (
        (FIELD, 'FIELD'),
        (PLAYER, 'PLAYER'),
        (OTHER_PLAYER, 'OTHER_PLAYER'),
        (SELF, 'SELF'),
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


class ActivityCost(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    amount = models.IntegerField()

    def __str__(self):
        return "Cost_{}_{}".format(self.activity.name, self.resource.name)
