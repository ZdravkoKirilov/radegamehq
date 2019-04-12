from django.db import models

from ..mixins.EntityBase import EntityBase


class Group(EntityBase, models.Model):

    def __str__(self):
        return "{}".format(self.name)
