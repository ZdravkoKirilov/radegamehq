from django.db import models
from ..mixins.EntityBase import EntityBase


class Faction(EntityBase):
    slots = models.ManyToManyField('Slot', blank=True, related_name='slotss_%(class)ss')

    def __str__(self):
        return self.name
