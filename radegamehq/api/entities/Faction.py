from django.db import models

from .Game import Game
from .Resource import Resource
from .Field import Field

PLAYER = 'PLAYER'
BOT = 'BOT'
MASTER = 'MASTER'

TYPE_CHOICES = (
    (PLAYER, PLAYER),
    (BOT, BOT),
    (MASTER, MASTER)
)


class Faction(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True, null=True)
    keywords = models.CharField(max_length=255, blank=True, null=True)
    image = models.FileField(upload_to='faction_images', blank=True, null=True, max_length=255)
    start = models.ForeignKey(Field, on_delete=models.SET_NULL, blank=True, null=True)
    type = models.CharField(max_length=255, choices=TYPE_CHOICES, default=TYPE_CHOICES[0][0])
    activity_limit = models.IntegerField(blank=True, null=True)
    resource_limit = models.IntegerField(blank=True, null=True)

    resources = models.ManyToManyField(Resource, blank=True, through='FactionResource')
    income = models.ManyToManyField(Resource, blank=True, through='FactionIncome', related_name='faction_income')
    activities = models.ManyToManyField('Activity', blank=True, through='ActivityQuota', related_name='faction_quota')

    def __str__(self):
        return self.name


class FactionResource(models.Model):
    faction = models.ForeignKey(Faction, on_delete=models.CASCADE, related_name='faction_resource')
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    amount = models.IntegerField()

    def __str__(self):
        return "{}_{}".format(self.faction.name, self.resource.name)


class FactionIncome(models.Model):
    faction = models.ForeignKey(Faction, on_delete=models.CASCADE, related_name='faction_income')
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    amount = models.IntegerField()

    def __str__(self):
        return "{}_{}".format(self.faction.name, self.resource.name)
