from django.db import models

from api.entities.Game import Game
from .EffectStack import EffectStack

MODE_CHOICES = (
    ('DRAW', 'DRAW'),
    ('AUTO_TRIGGER', 'AUTO_TRIGGER')
)


class EffectGroup(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    mode = models.TextField(choices=MODE_CHOICES)

    random_pick = models.BooleanField(default=False)
    player_pick = models.BooleanField(default=True)
    min_cap = models.IntegerField(null=True, blank=True)
    max_cap = models.IntegerField(null=True, blank=True)
    random_cap = models.BooleanField(default=False)
    allow_same_pick = models.BooleanField(default=False)


class EffectGroupItem(models.Model):
    owner = models.ForeignKey(EffectGroup, on_delete=models.CASCADE)

    action = models.ForeignKey('Action', on_delete=models.CASCADE, null=True, blank=True)
    condition = models.ForeignKey('Condition', on_delete=models.CASCADE, null=True, blank=True)

    cost = models.ForeignKey(EffectStack, on_delete=models.SET_NULL, null=True, blank=True)
    quota = models.IntegerField(default=1)
    restriction = models.TextField(null=True, blank=True)
