from django.db import models

from .Source import Source

from api.mixins.EntityBase import EntityBase


class Team(EntityBase):
    image = models.FileField(upload_to='team_images', blank=True, null=True, max_length=None)

    min_players = models.IntegerField(default=1)
    max_players = models.IntegerField(default=1)

    effect_pool = models.ManyToManyField(Source, related_name='team_effect_pool', blank=True)

    income = models.ManyToManyField('Stack', blank=True)

    def __str__(self):
        return self.name
