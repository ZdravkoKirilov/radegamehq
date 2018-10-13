from django.db import models

from .Game import Game

RELATIONS = (
    ('AND', 'AND'),
    ('OR', 'OR')
)


class EffectStack(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    action = models.ForeignKey('Action', on_delete=models.CASCADE, null=True, blank=True)
    condition = models.ForeignKey('Condition', on_delete=models.CASCADE, null=True, blank=True)

    relation = models.TextField(choices=RELATIONS, default=RELATIONS[0][0])
