from django.db import models
from ..mixins.EntityBase import EntityBase, WithSettings


class Phase(EntityBase, WithSettings):

    turn_cycles = models.IntegerField(blank=True, null=True, default=1)

    def __str__(self):
        return 'Phase_{}'.format(self.name)
