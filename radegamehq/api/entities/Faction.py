from django.db import models

from .Pool import Pool

from api.mixins.EntityBase import EntityBase

PLAYER = 'PLAYER'
BOT = 'BOT'

TYPE_CHOICES = (
    (PLAYER, PLAYER),
    (BOT, BOT),
)


# type "Master" is not needed, action restriction/condition combined with keywords is enough:
#  the Master can have entirely different Actions


class Faction(EntityBase):
    image = models.FileField(upload_to='faction_images', blank=True, null=True, max_length=None)

    type = models.CharField(max_length=255, choices=TYPE_CHOICES, default=TYPE_CHOICES[0][0])

    stage = models.ForeignKey('Stage', on_delete=models.SET_NULL, null=True, blank=True)

    income = models.ManyToManyField('Stack', blank=True)

    effect_pool = models.ManyToManyField(Pool, related_name='faction_effect_pool', blank=True)

    def __str__(self):
        return self.name

