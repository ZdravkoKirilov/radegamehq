from django.db import models
from ..mixins.EntityBase import EntityBase


class Faction(EntityBase):
    stages = models.ManyToManyField('Stage', blank=True, related_name='stages_%(class)ss')

    def __str__(self):
        return self.name
