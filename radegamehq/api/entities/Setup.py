from django.db import models

from ..mixins.EntityBase import EntityBase


class Setup(EntityBase):
    min_players = models.IntegerField(null=True, blank=True)
    max_players = models.IntegerField(null=True, blank=True)
    recommended_age = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.name)


class RoundSlot(models.Model):
    owner = models.ForeignKey(Setup, on_delete=models.CASCADE, related_name='rounds', blank=True, null=True)
    round = models.ForeignKey('Round', on_delete=models.CASCADE)
    done = models.ForeignKey('Expression', on_delete=models.SET_NULL, null=True, blank=True)
