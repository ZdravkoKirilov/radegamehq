from django.db import models

from ..mixins.EntityBase import EntityBase


class Stage(EntityBase, models.Model):

    width = models.IntegerField()
    height = models.IntegerField()

    def __str__(self):
        return "{}".format(self.name)
