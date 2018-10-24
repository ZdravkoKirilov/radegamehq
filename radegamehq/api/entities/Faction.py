from django.db import models

from .Location import Location
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

    # limit fields are not needed: enforced via effect_pool conditions instead

    effect_pool = models.ManyToManyField(Pool, related_name='faction_effect_pool')

    def __str__(self):
        return self.name


class Token(models.Model):
    owner = models.ForeignKey(Faction, on_delete=models.CASCADE, null=True, blank=True)

    start = models.ForeignKey(Location, on_delete=models.SET_NULL, blank=True, null=True)

    image = models.ImageField(upload_to='token_images', blank=True, null=True, max_length=None)
    name = models.CharField(max_length=255)

    # limit fields are not needed: enforced via effect_pool conditions instead

    effect_pool = models.ManyToManyField(Pool, related_name='token_effect_pool')
