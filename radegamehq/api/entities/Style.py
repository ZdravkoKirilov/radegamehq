from django.db import models

from ..mixins.EntityBase import EntityBase


class Style(EntityBase, models.Model):

    def __str__(self):
        return "{}".format(self.name)
