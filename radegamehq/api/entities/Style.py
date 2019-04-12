from django.db import models

from ..mixins.EntityBase import EntityBase


class Style(EntityBase, models.Model):

    frame = models.IntegerField(null=True, blank=True)
    rotation = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return "{}".format(self.name)
