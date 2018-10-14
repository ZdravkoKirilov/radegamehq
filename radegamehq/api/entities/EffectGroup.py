from django.db import models

from api.entities.Game import Game
from .EffectStack import EffectStack

MODE_CHOICES = (
    ('DRAW', 'DRAW'),
    ('AUTO_TRIGGER', 'AUTO_TRIGGER')
)

PICK_CHOICES = (
    ('RANDOM', 'RANDOM'),
    ('CHOICE', 'CHOICE')
)

QUOTA_CHOICES = (
    ('REPEATING', 'REPEATING'),
    ('ONCE', 'ONCE')
)


class EffectGroup(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    mode = models.TextField(choices=MODE_CHOICES, default=MODE_CHOICES[0][0])

    pick = models.CharField(choices=PICK_CHOICES, max_length=255, default=PICK_CHOICES[0][1])

    quota = models.CharField(choices=QUOTA_CHOICES, max_length=255, default=QUOTA_CHOICES[0][0])

    min_cap = models.IntegerField(null=True, blank=True)
    max_cap = models.IntegerField(null=True, blank=True)
    random_cap = models.BooleanField(default=False)

    allow_same_pick = models.BooleanField(default=False)


class EffectGroupItem(models.Model):
    owner = models.ForeignKey(EffectGroup, on_delete=models.CASCADE)

    action = models.ForeignKey('Action', on_delete=models.CASCADE, null=True, blank=True)
    condition = models.ForeignKey('Condition', on_delete=models.CASCADE, null=True, blank=True)

    cost = models.ForeignKey(EffectStack, on_delete=models.SET_NULL, null=True, blank=True)  # price to buy
    quota = models.IntegerField(default=1)  # how many will be available
    restriction = models.ManyToManyField(EffectStack, related_name='effect_item_restriction')
