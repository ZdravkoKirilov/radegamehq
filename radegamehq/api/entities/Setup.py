from django.db import models

from ..mixins.EntityBase import EntityBase


class Setup(EntityBase):
    min_players = models.IntegerField(null=True, blank=True)
    max_players = models.IntegerField(null=True, blank=True)
    recommended_age = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.name)
