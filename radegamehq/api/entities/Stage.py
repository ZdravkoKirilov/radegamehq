from django.db import models

from ..mixins.EntityBase import EntityBase


class Stage(EntityBase, models.Model):

    width = models.IntegerField()
    height = models.IntegerField()

    populate_by = models.ForeignKey('Expression', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.name)
