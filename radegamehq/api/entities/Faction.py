from django.db import models

from api.entities.Game import Game
from api.entities.Resource import Resource


class FactionTermination(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    faction = models.ForeignKey('Faction', on_delete=models.CASCADE)
    quest = models.ForeignKey('Quest', on_delete=models.CASCADE)


class Faction(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True)
    image = models.FileField(upload_to='faction_images', blank=True, null=True, max_length=200)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    resources = models.ManyToManyField(Resource, blank=True, through='FactionResource')
    income = models.ManyToManyField(Resource, blank=True, through='FactionIncome', related_name='faction_income')

    def __str__(self):
        return self.name


class FactionResource(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    faction = models.ForeignKey(Faction, on_delete=models.CASCADE, related_name='faction_resource')
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return "{}_{}".format(self.faction.name, self.resource.name)


class FactionIncome(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    faction = models.ForeignKey(Faction, on_delete=models.CASCADE, related_name='faction_income')
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return "{}_{}".format(self.faction.name, self.resource.name)