from django.db import models

from .Location import Location
from .EffectGroup import EffectGroup

from api.mixins.EntityBase import EntityBase

PLAYER = 'PLAYER'
BOT = 'BOT'
MASTER = 'MASTER'

TYPE_CHOICES = (
    (PLAYER, PLAYER),
    (BOT, BOT),
    (MASTER, MASTER)
)


class Faction(EntityBase):
    image = models.FileField(upload_to='faction_images', blank=True, null=True, max_length=255)

    start = models.ForeignKey(Location, on_delete=models.SET_NULL, blank=True, null=True)
    type = models.CharField(max_length=255, choices=TYPE_CHOICES, default=TYPE_CHOICES[0][0])

    activity_limit = models.IntegerField(blank=True, null=True)
    resource_limit = models.IntegerField(blank=True, null=True)

    effect_pool = models.ManyToManyField(EffectGroup, related_name='faction_effect_pool')

    def __str__(self):
        return self.name
